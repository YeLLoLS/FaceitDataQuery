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
import secrets

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
    with open('importante.json', 'r') as f:
        importante = json.load(f)

    lvl_img = importante['levels'][f'{items[3]}']
    steam_profile = 'https://steamcommunity.com/profiles/{}/'.format(items[18])
    colors_list = importante['colors']
    random_color = hex(int(secrets.choice(colors_list)))
    embed = discord.Embed(title='Steam profile', url=steam_profile, color=int(random_color, 16))
    embed.set_thumbnail(url=f'{lvl_img}')
    embed.set_author(name = f'{items[1]}', icon_url = f'{items[8]}')
    

    embed.add_field(name='Profil', value= items[8], inline=True)
    await ctx.send(content=None, embed=embed)



my_secret = os.environ['SECRET']
bot.run(my_secret)