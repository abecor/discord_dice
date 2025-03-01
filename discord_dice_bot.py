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
    print("==============")
    print(f"{bot.user} has entered Discord!")
    print("==============")
    
    for guild in bot.guilds:
        print(f"{guild.name}: {guild.id}")
    
    print("==============")

    for channel_id in CHANNEL_IDS:
        try:
            channel = bot.get_channel(int(channel_id))
            if channel:
                print("Got channel...")
            if channel and isinstance(channel, discord.TextChannel):
                print(f"Successfully connected to #{channel.name} in {channel.guild.name}. (ID: {channel.id})")
            else:
                print(f"Could not connect to channel ID {channel_id}. Check CHANNEL_IDS.")
        
        except discord.Forbidden:
            print(f"Forbidden: Bot laccks permission for channel ID {channel_id}")
        except discord.HTTPException:
            print(f"")
    
    print("\n")


@bot.slash_command(guild_ids=guild_ids)
async def r(ctx, text: Option(str, name="roll", description="Roll your dice")): # type: ignore
    '''Rolls dice. "/r roll help" for help.'''
    
    print("==============")
    print("Received command...deferring...")
    
    await ctx.defer()

    try:
        print("==============")
        print("Input: " + text) # nohup logging
        roll = roll_dice.roll(text)
        print("Output: " + roll)

        await ctx.followup.send(roll)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.followup.send("An error occurred while rolling the dice.")


if __name__ == "__main__":
    bot.run(TOKEN) # type: ignore