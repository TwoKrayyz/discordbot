import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"Logged in as: {bot.user}")


@bot.command()
async def menu(ctx: commands.Context[commands.Bot]) -> None:
    embed = discord.Embed(
        title="Help Menu",
        description="A menu of everything helpful.",
        color=0x37352C,
    )
    embed.add_field(name="Utility", value=" ", inline=False)
    embed.add_field(name="`menu`", value="Displays the help menu.")
    embed.add_field(name="Fun", value=" ", inline=False)
    embed.add_field(name="`echo`", value="Repeats what you say.")

    await ctx.send(embed=embed)


@bot.command()
async def echo(ctx: commands.Context[commands.Bot], arg: str) -> None:
    embed = discord.Embed(description=arg, color=0x37352C)

    await ctx.send(embed=embed)


TOKEN = os.getenv("DEVELOPER_TOKEN")
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")
bot.run(TOKEN)
