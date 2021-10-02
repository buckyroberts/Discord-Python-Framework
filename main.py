from discord.ext import commands
from pymongo import MongoClient

from config.settings import (
    DISCORD_TOKEN,
    MONGO_DB_NAME,
    MONGO_HOST,
    MONGO_PORT
)
from utils.discord import send_embed
from utils.thenewboston import is_valid_account_number

bot = commands.Bot(command_prefix='>')

mongo = MongoClient(MONGO_HOST, MONGO_PORT)
database = mongo[MONGO_DB_NAME]

USERS = database['users']


@bot.event
async def on_ready():
    """
    Start polling blockchain
    """

    print('Ready')


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


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
