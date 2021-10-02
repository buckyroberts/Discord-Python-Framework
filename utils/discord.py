import random
import string

import discord

from config.settings import BOT_ACCOUNT_NUMBER


def generate_verification_code():
    """
    Generate random verification code
    """

    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(8))


async def send_embed(*, ctx, title, description):
    """
    Send a simple embed with a title and a description
    """

    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Colour.red()
    )

    await ctx.send(embed=embed)


async def send_verification_message(*, ctx, registration_account_number, registration_verification_code):
    """
    Send verification message DM
    """

    embed = discord.Embed(
        title='Account Registration',
        description='To complete registration please send the following transaction.',
        color=discord.Colour.red()
    )
    embed.add_field(
        name='From',
        value=registration_account_number,
        inline=False
    )
    embed.add_field(
        name='To',
        value=BOT_ACCOUNT_NUMBER,
        inline=False
    )
    embed.add_field(
        name='Memo',
        value=registration_verification_code,
        inline=False
    )
    embed.add_field(
        name='Amount',
        value='1',
        inline=False
    )

    await ctx.author.send(embed=embed)
