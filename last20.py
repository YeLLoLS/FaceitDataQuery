from faceit_data import FaceitData
import os
import json

key_api = os.environ['api_key']
faceit_data = FaceitData(key_api)

def csgo_last20(player_name):
    game = 'csgo'

    # -------- getting player id -------- #
    player_data = faceit_data.search_players(player_name, game)
    counter = 0
    index_valid = 0
    for el in player_data['items']:
        if el['nickname'] == player_name:
            index_valid = counter
        counter += 1

    idPlayer = player_data['items'][int(index_valid)]['player_id']

    matches = faceit_data.player_matches(player_id=idPlayer, game=game)


    list_ids = []
    for el in matches['items']:
        list_ids.append(faceit_data.match_stats(el['match_id']))

    #matchStats = faceit_data.match_stats()

    index_id = 0
    info_winners = []
    info_match = []
    for el in list_ids:
        team1_players = list_ids[index_id]['rounds'][0]['teams'][0]['players']
        team2_players = list_ids[index_id]['rounds'][0]['teams'][1]['players']
        cnt = 0
        index_player = None
        for el in team1_players:
            if el['player_id'] == idPlayer:
                index_player = cnt
                index_echipa = 0
            cnt += 1

        if index_player == None:
            cnt = 0
            for el in team2_players:
                if el['player_id'] == idPlayer:
                    index_player = cnt
                    index_echipa = 1
                cnt += 1

        #player_name = list_ids[0]['rounds'][0]['teams'][0]['players'][index_player]['nickname']
        player_stats = list_ids[index_id]['rounds'][0]['teams'][0]['players'][index_player]['player_stats']
        winner_team_id = list_ids[index_id]['rounds'][0]['teams'][index_echipa]['team_id']
        info_match.append(player_stats)
        info_winners.append(winner_team_id)
        index_id += 1

    print(info_match)
    print(info_winners)

