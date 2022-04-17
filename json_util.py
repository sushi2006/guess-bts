'''
Source:

Author: Suchita 

Mentors: 
    Chaaya
    Harshitha
    Rajasree
'''

import random
import json

FILEPATH = 'score.json'

CURRENT_GAME_INDEX = "192001"
DEFAULT_SCORE = 5

def get_json_data():

    with open(FILEPATH) as json_file:
        data = json.load(json_file)
        
        print(data)

    return data

def store_json_data(data):

    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)

def get_current_game(game_index):

    score_dict = get_json_data()

    if(game_index in score_dict):
        return score_dict[game_index]

    # We will fix this one later
    raise Exception("Data Error")

    # c_city = city_list[random.randint(0, len(city_list))]

    # user_dict[username] = c_city

    # # store into json
    # store_json_data(user_dict)

    # print(ch_meter)
    # return c_city

def increase_score(game_index, player_index, score = DEFAULT_SCORE):
    
    current_game_score_dict = get_current_game(CURRENT_GAME_INDEX)

    player_name = f"player_{player_index}_score"

    current_player_score = current_game_score_dict[player_name]

    current_player_score += score

    current_game_score_dict[player_name] = current_player_score

    full_score_json = get_json_data()

    # update current game 
    full_score_json[game_index] = current_game_score_dict

    store_json_data(full_score_json)

def startpy():

    # current_game_score_dict = get_current_game(CURRENT_GAME_INDEX)
    # print(current_game_score_dict)

    # test1: adding player 1 score by 5
    increase_score(
        CURRENT_GAME_INDEX,
        2, 
        5
    )

    pass


if __name__ == "__main__":
    startpy()
    