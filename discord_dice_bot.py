import discord
from discord.ext import commands
from discord import Option

from dotenv import load_dotenv
import os
import roll_dice


#load .env with token, guild and channel IDS

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_IDS = os.getenv('GUILD_ID').split(",") # type: ignore
guild_ids = []
for id in GUILD_IDS:
    guild_ids.append(int(id))

CHANNEL_IDS = os.getenv('CHANNEL_ID').split(",") # type: ignore

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has entered Discord!")
    for channel_id in CHANNEL_IDS:
        channel = bot.get_channel(int(channel_id))
        if channel and isinstance(channel, discord.TextChannel):
            try:
                print(f"Bot has joined {channel}.")
                for guild in bot.guilds:
                    print(guild)
            except discord.Forbidden:
                print("Bot does not have permission to send messages in this channel.")
            except discord.HTTPException as e:
                print(f"Failed to send message: {e}")
        else:
            print("Channel is not a text channel.")

@bot.slash_command(guild_ids=guild_ids)
async def r(ctx, text: Option(str, name="roll", description="Roll your dice")): # type: ignore
    '''Rolls dice. "/r roll help" for help.'''

    print("==============")
    print("Input: " + text) # nohup logging
    roll = roll_dice.roll(text)
    print("Output: " + roll)

    await ctx.respond(roll)

if __name__ == "__main__":
    bot.run(TOKEN) # type: ignore