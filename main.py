from discord.ext import commands, tasks
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from config.settings import (
    BANK_IP,
    BANK_PROTOCOL,
    BOT_ACCOUNT_NUMBER,
    DISCORD_TOKEN,
    MONGO_DB_NAME,
    MONGO_HOST,
    MONGO_PORT
)
from utils.discord import generate_verification_code, send_embed, send_verification_message
from utils.network import fetch
from utils.thenewboston import is_valid_account_number

bot = commands.Bot(command_prefix='>')

mongo = MongoClient(MONGO_HOST, MONGO_PORT)
database = mongo[MONGO_DB_NAME]

DEPOSITS = database['deposits']
REGISTRATIONS = database['registrations']
USERS = database['users']

"""
DEPOSIT
    _id: "7ca8d42a-80fd-4d8b-987a-470a3725d098"
    amount: 1
    block_id: "a24f8d90-0502-4b16-84c4-a123962989e9"
    confirmation_checks: 1
    is_confirmed: true
    memo: "7OJYUJ9K"
    sender: "a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f"

REGISTRATION
    _id: 310922051613491868
    account_number: "a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f"
    verification_code: "7OJYUJ9K"

USER
    _id: 310922051613491868
    account_number: "a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f"
    balance: 0
"""


def check_deposits():
    """
    Fetch bank transactions from bank
    Insert new deposits into database
    """

    next_url = (
        f'{BANK_PROTOCOL}://{BANK_IP}/bank_transactions'
        f'?recipient={BOT_ACCOUNT_NUMBER}'
        f'&ordering=block__created_date'
    )

    while next_url:
        data = fetch(url=next_url, headers={})
        bank_transactions = data['results']
        next_url = data['next']

        for bank_transaction in bank_transactions:

            try:
                DEPOSITS.insert_one({
                    '_id': bank_transaction['id'],
                    'amount': bank_transaction['amount'],
                    'block_id': bank_transaction['block']['id'],
                    'confirmation_checks': 0,
                    'is_confirmed': False,
                    'memo': bank_transaction['memo'],
                    'sender': bank_transaction['block']['sender']
                })
            except DuplicateKeyError:
                break


@tasks.loop(seconds=5.0)
async def poll_blockchain():
    """
    Poll blockchain for new transactions/deposits sent to the bot account
    Only accept confirmed transactions
    """

    print('Polling blockchain...')
    check_deposits()
    # check_confirmations()


@bot.event
async def on_ready():
    """
    Start polling blockchain
    """

    print('Ready')
    poll_blockchain.start()


@bot.command()
async def register(ctx, account_number):
    """
    >register a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f
    """

    if not is_valid_account_number(account_number):
        await send_embed(
            ctx=ctx,
            title='Invalid',
            description='Invalid account number.'
        )
        return

    user = USERS.find_one({'account_number': account_number})

    if user:
        await send_embed(
            ctx=ctx,
            title='Already Registered',
            description=f'The account {account_number} is already registered.'
        )
        return

    discord_user_id = ctx.author.id
    verification_code = generate_verification_code()

    results = REGISTRATIONS.update_one(
        {'_id': discord_user_id},
        {
            '$set': {
                'account_number': account_number,
                'verification_code': verification_code
            }
        },
        upsert=True
    )

    if results.modified_count:
        await send_embed(
            ctx=ctx,
            title='Registration Updated',
            description=(
                'Your registration has been updated. '
                'To complete registration, follow the instructions sent via DM.'
            )
        )
    else:
        await send_embed(
            ctx=ctx,
            title='Registration Created',
            description=(
                'Registration created. '
                'To complete registration, follow the instructions sent via DM.'
            )
        )

    await send_verification_message(
        ctx=ctx,
        registration_account_number=account_number,
        registration_verification_code=verification_code
    )


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
