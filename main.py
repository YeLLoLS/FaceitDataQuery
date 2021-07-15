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
    counter = 0
    index_valid = 0         
    faceit_data = FaceitData(key_api)
    players = faceit_data.search_players(player_name, game)
    for el in players["items"]:
      if el['nickname'] == player_name:
#          await ctx.send(f'Jucatorul cu numele {player_name} nu exista!')
          index_valid = counter
      counter = counter + 1
    profil = players["items"][int(index_valid)]
    idPlayer = profil['player_id']
    stats = faceit_data.player_id_details(idPlayer)
    nickName = profil['nickname']
    status = profil['status']
    nameGame = profil['games'][0]['name']
    gameSkill = profil['games'][0]['skill_level']
    country = profil['country']
    verified = profil['verified']
    avatar = profil['avatar']




my_secret = os.environ['SECRET']
bot.run(my_secret)