import asyncio
import logging
import os

import discord
from disckit.utils import MainEmbed
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

_logger: logging.Logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"Logged in as: {bot.user}")


@bot.command()
async def menu(ctx: commands.Context[commands.Bot]) -> None:
    embed = MainEmbed(
        title="Help Menu",
        description="A menu of everything helpful.",
    )
    embed.add_field(name="Utility", value=" ", inline=False)
    embed.add_field(name="`menu`", value="Displays the help menu.")
    embed.add_field(name="Fun", value=" ", inline=False)
    embed.add_field(name="`echo`", value="Repeats what you say.")

    await ctx.send(embed=embed)


@bot.command()
async def echo(ctx: commands.Context[commands.Bot], arg: str) -> None:
    embed = MainEmbed(description=arg)

    await ctx.send(embed=embed)


async def main() -> None:
    """
    Main function to run the bot with any additional setup if needed.
    """
    TOKEN = os.getenv("DEVELOPER_TOKEN")
    if TOKEN is None:
        raise ValueError("DEVELOPER_TOKEN environment variable is not set")

    await bot.start(TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        _logger.info("KeyboardInterrupt detected.")
    except Exception as e:
        _logger.exception(f"An error occurred: {e}")
