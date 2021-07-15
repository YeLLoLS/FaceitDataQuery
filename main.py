import discord
import os
import csv
import json
from discord.ext import commands
import random
import asyncio
import time
from datetime import datetime, timedelta
from faceit_data import FaceitData
from profile import profile

key_api = os.environ['api_key']


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():

    print(f"{bot.user} logged in now!")

    await bot.change_presence(activity=discord.Game(name="Ochii din umbra."))

@bot.event
async def on_message(message):

    if message.author.bot == False:
      
        await bot.process_commands(message)

    else:

      return

@bot.command()
async def search_player(ctx, player_name: str, game: str):
    items = profile(player_name, game)
    print(items)




my_secret = os.environ['SECRET']
bot.run(my_secret)