from faceit_data import FaceitData
import os

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
    elo = info_stats['games']['csgo']['faceit_elo']
    nickName = profil['nickname']
    status = profil['status']
    nameGame = profil['games'][0]['name']
    gameSkill = profil['games'][0]['skill_level']
    country = profil['country']
    verified = profil['verified']
    avatar = profil['avatar']

    return idPlayer, nickName, gameSkill, nameGame, elo, status, country, verified, avatar