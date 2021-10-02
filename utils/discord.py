import discord


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
