#
#   SCOREM
#
"""
Scorem
----------

Scorem functions for the `scoremipsum` module.
"""
import scoremipsum
from scoremipsum import data
from scoremipsum.util.conversion import convert_game_result_to_json
from scoremipsum.util.support import get_supported_sports


def game(gametype=None):
    # print(f"game({gametype=}) not yet implemented !")
    print(f"game({gametype=}) ... ")
    teamlist = data.TEAMS_DEFAULT
    schedule = scoremipsum.game.generate_schedule_single_pairs(teamlist)
    game_generation_results = scoremipsum.game.generate_games_from_schedule(schedule, gametype=gametype)
    game_results_json = convert_game_result_to_json(game_generation_results, gametype=gametype)
    return game_results_json


def commands():

    # DYNAMIC determination, now returns convert_game_result_to_json() method - mess with this later
    # method_list = [func for func in dir(scoremipsum.scoremipsum) if
    #                callable(getattr(scoremipsum.scoremipsum, func)) and not func.startswith(
    #                    "_") and not func.startswith("get_")]
    # for now, maintain the command list manually
    method_list = ['commands', 'game', 'help', 'sports', 'sportsball']
    return method_list


def help():
    print("== help() not yet implemented !")
    print("-" * 80)


def sportsball():
    print("== sportsball !")
    print("-" * 80)


def sports():
    sports_list = get_supported_sports()
    return sports_list
