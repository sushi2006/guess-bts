

'''
Created on 

Course work: 
    Python for BTS Army
    
@author: BTS Army Colonel Suchi

Source:
    
'''

# Import necessary modules

from os import name
from typing import cast
from flask import Flask, jsonify
from flask import render_template
import json
import random
import util

# Local import
from const import *
import json_util as jungutil

app = Flask(__name__)

def _get_random_bias():

    bts_members = [
        "Jin", 
        "Suga",
        "J-Hope",
        "RM",
        "Jimin",
        "V",
        "Jungkook"
    ]

    bts_members_info = [

        # Jin
        # [
        #     "Jin was born on December 4",
        #     "Jin's nickname is worldwide handsome",
        #     "Jin is the mom of the group",
        #     "Jin is also known as that “third guy from the left”",
        #     "Jin was an exchange student in Australia",
        # ], 
        util.read_file(f'{BASE_DIR_PATH}jin.txt'),

        # Suga
        # [
        #     "Suga's favorite color is white",
        #     "Suga loves to sleep",
        #     "Suga is know as the savage in the group",
        #     "Suga stage names Suga and Agust D,",
        #     "Suga's liconic line is 'In my next life I want to be born as a rock'"
        # ],
        util.read_file(f'{BASE_DIR_PATH}suga.txt'),


        # "J-Hope"
        # [
            # "J-Hope is the Sunshine of the group",
            # "J-Hope is the main dancer of the group",
            # "J-Hope's iconic line is 'I’m your hope, you’re my hope, I’m Jhope'",
            # "J-Hope was a member of the street dance group NEURON.",
            # "J-Hope’s motto is “If you don’t work hard, you’ll never get results”."
        # ],
        util.read_file(f'{BASE_DIR_PATH}J-hope.txt'),

        # RM
        # [
        #     "RM is also known as the God of Destruction",
        #     "RM is the Leader of the group",
        #     "RM favourite singer was Nas",
        #     "RM studied in New Zealand and lived there for 6 months.",
        #     "RM's iconic line is 'Jimin. You got no jams'"
        # ],
        util.read_file(f'{BASE_DIR_PATH}RM.txt'),

        # Jimin
        # [
        #     "Jimin's iconic line is 'Lachimolala'",
        #     "Jimin is famous for little pinky",
        #     "Jimin is the shortest in the group",
        #     "In the dorm, Jimin is in charge of the kitchen.",
        #     "Jimin was ranked 64 places in the “Top 100 Handsome Faces of 2017”",
        #     "When Jimin laughs he either falls on someone or disappears"
        # ],
        util.read_file(f'{BASE_DIR_PATH}Jimin.txt'),

        # V
        # [
        #     "V's nic name is Tae Tae",
        #     "V always thinks out of the box",
        #     "V is also called called an alien",
        #     "V's iconic line is'I'm a GOOD Boy'",
        #     "V knows how to play the saxophone",
        #     "V dedicated his win at Music Bank to his Grandma",
        #     "V is ambidextrous, that is he can write with both hands."
        # ],
        util.read_file(f'{BASE_DIR_PATH}V.txt'),

        # Jungkook
        # [
        #     "Jungkook is known as Golden Maknae",
        #     "Jungkook is good at everything",
        #     "Jungkook knows Taekwondo",
        #     "Jungkook’s favorite color is black ",
        #     "Jungkook iconic line is 'start stage, uh…my heart boom boom'",
        #     "Jungkook's other nicknames are 'Jeon Jungkookie or Kookie'",
        #     "When Jungkook was younger, he want to be a badminton player"
        # ]
        util.read_file(f'{BASE_DIR_PATH}Jungkook.txt')
    ]

    # rand_no = random.randint(0,1)
    rand_no = random.randint(0, len(bts_members)-1)

    img_no = random.randint(0,8)

    member = bts_members[rand_no]

    current_member_info_list = bts_members_info[rand_no]

    info_random_no = random.randint(0, len(current_member_info_list)-1)

    member_info = current_member_info_list[info_random_no]

    return member_info, member, img_no, rand_no

@app.route("/")
def home():
    
    member_info, member, img_no, rand_no = _get_random_bias()

    players = util.get_players()
    return render_template(
        'index2.html', 
        current_bias = member,
        # current_number = img_no,
        current_member_info = member_info,
        current_image = f'static/bts_{member}_{img_no}.jpeg',
        current_rand_no = rand_no,
        game_players = players
    )

@app.route("/random/bias")
def get_random_bias():

    member_info, member, img_no, rand_no = _get_random_bias()

    result_dict = {
        'current_member_info' : member_info,
        'member' : member,
        'img_no' : img_no,
        'rand_no' : rand_no,
        'current_image' : f'static/bts_{member}_{img_no}.jpeg',
    }

    return jsonify(result_dict)

@app.route("/increase/player/<player_index>/score")
def increase_player_score(player_index):

    # 
    player_new_score = jungutil.increase_score(
        CURRENT_GAME_INDEX,
        player_index,
        DEFAULT_SCORE
    )

    result_dict = {
        'error_code' : 0,
        'player_index' : player_index,
        'player_new_score' : player_new_score,
    }

    return jsonify(result_dict)

@app.route('/flag')
def get_flag():

    rand_no = random.randint(0, 8)
    return render_template(
        'index2.html', 
        my_no = rand_no,
        current_image = f'static/bts_{rand_no}.jpeg'
    )

if __name__== "__main__":
    app.run(
        host = "0.0.0.0", 
        debug = True, 
        port = 5003
    )