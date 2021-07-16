from faceit_data import FaceitData
import os
import json

key_api = os.environ['api_key']
def profile(player_name, game):
    counter = 0
    index_valid = 0         
    faceit_data = FaceitData(key_api)
    players = faceit_data.search_players(player_name, game)
    for el in players["items"]:
      if el['nickname'] == player_name:
          index_valid = counter    
      counter = counter + 1
    profil = players["items"][int(index_valid)]
    idPlayer = profil['player_id']
    info_stats = faceit_data.player_id_details(idPlayer)
    
    ranking = faceit_data.player_ranking_of_game(game, info_stats['games'][f'{game}']['region'], idPlayer, info_stats['country'])

    counter2 = 0
    index_valid2 = 0
    for el in ranking['items']:
        if el['player_id'] == id:
            index_valid2 = counter2
        counter2 = counter2 + 1
    correct_player = ranking['items'][index_valid2]
    country_ranking = correct_player['position']
    stats = faceit_data.player_stats(player_id=idPlayer, game_id='csgo')
    winRate = stats['lifetime']['Win Rate %']
    avgKD = stats['lifetime']['Average K/D Ratio']
    avgHS = stats['lifetime']['Average Headshots %']
    recentResults = stats['lifetime']['Recent Results']
    lose_wins = []
    for el in recentResults:
        if el == '0':
            lose_wins.append(':x:')
        elif el == '1':
            lose_wins.append(':white_check_mark:')
        else:
            print("Unknown element!")
    longestWINstreak = stats['lifetime']['Longest Win Streak']
    currentWINstreak = stats['lifetime']['Current Win Streak']
    matches = stats['lifetime']['Matches']
    wins = stats['lifetime']['Wins']
    loses = str(int(matches) - int(wins))
    with open('importante.json', 'r') as f:
        importante = json.load(f)
    elo = str(info_stats['games']['csgo']['faceit_elo'])
    list_elo = []
    for el in elo:
      list_elo.append(importante['number_emoji'][f'{el}'])
    empty_elo = ''
    for el in list_elo:
        empty_elo = empty_elo + el
    nickName = profil['nickname']
    status = profil['status']
    nameGame = profil['games'][0]['name']
    gameSkill = profil['games'][0]['skill_level']
    country = profil['country']
    verified = profil['verified']
    if verified == True:
        verified = ':white_check_mark:'
    else:
        verified = ':x:'
    avatar = profil['avatar']
    steam_id_64 = info_stats['steam_id_64']
    afk = info_stats['infractions']['afk']
    leaver = info_stats['infractions']['leaver']
    return idPlayer, nickName, nameGame, gameSkill, empty_elo, status, country, verified, avatar, winRate, avgKD, avgHS, lose_wins, longestWINstreak, currentWINstreak, matches, wins, loses, steam_id_64, afk, leaver, country_ranking, elo