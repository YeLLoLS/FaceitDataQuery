import discord
import os
import json
from discord.ext import commands
"""import random
import asyncio
import time
from datetime import datetime, timedelta"""
from faceit_data import FaceitData
from profile import profile
from last20 import csgo_last20
from overall_verdict import overallVerdict
import secrets

key_api = os.environ['api_key']

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f"{bot.user} logged in now!")

    await bot.change_presence(activity=discord.Game(name="Ochii din umbra."))


@bot.event
async def on_message(message):
    if not message.author.bot:

        await bot.process_commands(message)

    else:

        return


@bot.command()
async def search_player(ctx, player_name=None):
    game = 'csgo'
    # -------- condition for this command to be executed is that player name is REQUIRED --------#
    if player_name is None:
        await ctx.send("You forgot to mention player name!")
    else:
        # -------- querrying data from faceit using external function (see profile.py) --------#
        items = profile(player_name, game)
        # -------- end --------#

        print(items)  # needed for development only

        # -------- opening json file for reading --------#
        with open('importante.json', 'r') as f:
            importante = json.load(f)
        # -------- end --------#

        # -------- getting lvl image from json file for player's profile --------#
        lvl_img = importante['levels'][f'{items[3]}']
        # -------- end --------#

        # -------- getting game image from json file for player's profile --------#
        game_img = importante['game'][f'{items[2]}']
        # -------- end --------#

        # -------- formatting steam profile url for player's profile --------#
        steam_profile = 'https://steamcommunity.com/profiles/{}/'.format(items[18])
        # -------- end --------#

        # -------- getting a random color for embed message --------#
        colors_list = importante['colors']
        random_color = hex(int(secrets.choice(colors_list)))
        # -------- end --------#

        # -------- formatting the recent results --------#
        bracket = '{} '
        brackets = bracket * len(items[12])
        empty_brackets = ''
        if len(items[12]) == 1:
            empty_brackets = brackets.format(items[12][0])
        elif len(items[12]) == 2:
            empty_brackets = brackets.format(items[12][0], items[12][1])
        elif len(items[12]) == 3:
            empty_brackets = brackets.format(items[12][0], items[12][1], items[12][2])
        elif len(items[12]) == 4:
            empty_brackets = brackets.format(items[12][0], items[12][1], items[12][2], items[12][3])
        elif len(items[12]) == 5:
            empty_brackets = brackets.format(items[12][0], items[12][1], items[12][2], items[12][3], items[12][4])
        else:
            empty_brackets = 'Strange data'
        # -------- end --------#

        # recent_results = '{} {} {} {} {}'.format(items[12][0], items[12][1], items[12][2], items[12][3], items[12][4])

        # -------- getting user's country and assigning png flag --------#
        country_UPPER = items[6]
        img_country = 'https://www.countryflags.io/{}/flat/64.png'.format(country_UPPER)
        # -------- end --------#

        # -------- overall function invoked --------#
        overall_info = overallVerdict(win_rate=int(items[9]), avg_KD=float(items[10]), avg_HS=int(items[11]),
                                      matches=int(items[15]), elo=int(items[22]))
        overall = overall_info[0]
        verdict = overall_info[1]
        # -------- end --------#

        # -------- setting embed message --------#
        embed = discord.Embed(title='Steam profile', url=steam_profile, color=int(random_color, 16))
        embed.set_thumbnail(url=f'{lvl_img}')
        embed.set_author(name=f'{items[1]}', icon_url=f'{items[8]}')

        embed.add_field(name='ELO', value=items[4], inline=True)
        embed.add_field(name='Account status', value=items[5], inline=True)
        embed.add_field(name='Verified', value=items[7], inline=True)

        embed.add_field(name='Win Rate %', value=items[9], inline=True)
        embed.add_field(name='Average K/D Ratio', value=items[10], inline=True)
        embed.add_field(name='Average Headshots %', value=items[11], inline=True)

        embed.add_field(name='Recent results', value=empty_brackets, inline=True)
        embed.add_field(name='Current Win Streak', value=items[14], inline=True)

        if int(items[13]) > 9:
            embed.add_field(name='Longest Win Streak', value=f'{items[13]} :fire:', inline=True)
        else:
            embed.add_field(name='Longest Win Streak', value=f'{items[13]} :zzz:', inline=True)

        embed.add_field(name='Matches', value=items[15], inline=True)
        embed.add_field(name='Wins', value=items[16], inline=True)
        embed.add_field(name='Loses', value=items[17], inline=True)

        embed.add_field(name='AFK', value=items[19], inline=True)
        embed.add_field(name='LEAVE', value=items[20], inline=True)
        embed.add_field(name=f'OVERALL POINTS: {overall}', value=verdict, inline=True)

        embed.set_image(url=game_img)

        embed.set_footer(text=f'Country position: {country_UPPER} {items[21]}', icon_url=img_country)
        # -------- end --------#

        # -------- sending the embed message to channel where the command was executed --------#
        await ctx.send(embed=embed)
        # -------- end --------#

@bot.command()
async def csgolast20(ctx, player_name=None):
    if player_name is None:
        await ctx.send("You forgot to mention player name!")
    else:
         csgo_last20(player_name=player_name)

my_secret = os.environ['SECRET']
bot.run(my_secret)
