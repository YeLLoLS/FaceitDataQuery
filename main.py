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
async def search_player(ctx, player_name=None):
    game = 'csgo'
    if player_name == None:
        await ctx.send("You forgot to mention player name!")
    else:
        items = profile(player_name, game)
        print(items) #needed for development only
        with open('importante.json', 'r') as f:
            importante = json.load(f)

        lvl_img = importante['levels'][f'{items[3]}']
        steam_profile = 'https://steamcommunity.com/profiles/{}/'.format(items[18])
        colors_list = importante['colors']
        random_color = hex(int(secrets.choice(colors_list)))
        recent_results = '{} {} {} {} {}'.format(items[12][0], items[12][1], items[12][2], items[12][3], items[12][4])
        
        country_UPPER = items[6]
        country = country_UPPER.lower()
        img_country = importante['flags'][f'{country}']

        embed = discord.Embed(title='Steam profile', url=steam_profile, color=int(random_color, 16))
        embed.set_thumbnail(url=f'{lvl_img}')
        embed.set_author(name = f'{items[1]}', icon_url = f'{items[8]}')
        
        embed.add_field(name='ELO', value= items[4], inline=True)
        embed.add_field(name='Account status', value= items[5], inline=True)
        embed.add_field(name='Verified', value= items[7], inline=True)

        embed.add_field(name='Win Rate %', value= items[9], inline=True)
        embed.add_field(name='Average K/D Ratio', value= items[10], inline=True)
        embed.add_field(name='Average Headshots %', value= items[11], inline=True)

        embed.add_field(name='Recent results', value= recent_results , inline=True)
        embed.add_field(name='Current Win Streak', value= items[14], inline=True)

        if int(items[13]) > 9:
          embed.add_field(name='Longest Win Streak', value= f'{items[13]} :fire:', inline=True)
        else:
          embed.add_field(name='Longest Win Streak', value= f'{items[13]} :zzz:', inline=True)

        embed.add_field(name='Matches', value= items[15] , inline=True)
        embed.add_field(name='Wins', value= items[16], inline=True)
        embed.add_field(name='Loses', value= items[17], inline=True)

        embed.add_field(name='AFK', value= items[19], inline=True)
        embed.add_field(name='LEAVE', value= items[20], inline=True)
        overall = 0
        if 0 <= int(items[9]) <= 65:
            overall = overall + 10
        else:
            overall = overall + 20
        
        if 0.0 <= float(items[10]) <= 1.5:
            overall = overall + 10
        else:
            overall = overall + 20

        if 0 <= int(items[11]) <= 65:
            overall = overall + 10
        else:
            overall = overall + 20

        if 0 <= int(items[15]) <= 60 and int(items[22]) > 2001:
            overall = overall + 40
        elif 0 <= int(items[15]) <= 250 and int(items[22]) > 1851:
            overall = overall + 35
        elif 0 <= int(items[15]) <= 450 and int(items[22]) > 1701:
            overall = overall + 30
        elif int(items[15]) > 450 and int(items[22]) > 0:
            overall = overall + 10
        elif 60 <= int(items[15]) <= 115 and 1251 <= int(items[22]) <= 1551:
            overall = overall + 15
        elif 0 <= int(items[15]) <= 60 and 1251 <= int(items[22]) <= 1551:
            overall = overall + 25
        elif 0 <= int(items[15]) <= 60 and int(items[22]) < 1251:
            overall = overall + 20
        print(overall)
        verdict = ''
        if 85 <= overall <= 100:
            verdict = 'SMURF or CHEATER!!!'
        elif 70 <= overall <= 85:
            verdict = 'SMURF!!!'
        elif overall < 70:
            verdict = 'LEGIT :white_check_mark: :100:'
        
        embed.add_field(name=f'OVERALL POINTS: {overall}', value= verdict, inline=True)

        embed.set_footer(text= f'Country position: {country_UPPER} {items[21]}', icon_url= img_country)

        await ctx.send(content=None, embed=embed)
    

my_secret = os.environ['SECRET']
bot.run(my_secret)