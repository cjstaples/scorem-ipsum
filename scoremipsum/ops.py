#
#   SCOREM
#
"""
Scorem
----------

Scorem functions for the `scoremipsum` module.
"""
from scoremipsum.schedule import generate_schedule_single_pairs, generate_games_from_schedule
from scoremipsum.util.conversion import convert_game_result_to_json
from scoremipsum.util.support import get_supported_sports
from scoremipsum.util.team import get_default_teamlist_from_gametype


def game(gametype=None):
    # print(f"game({gametype=}) not yet implemented !")
    print(f"game({gametype=}) ... ")

    # DE5: game(gametype=foo) gives incorrect teams in results.
    #   error here, wrong teamlist for schedule when gametype is not None
    # teamlist = data.TEAMS_DEFAULT
    teamlist = get_default_teamlist_from_gametype(gametype)

    schedule = generate_schedule_single_pairs(teamlist)
    game_generation_results = generate_games_from_schedule(schedule, gametype=gametype)
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
    print("== help()")
    print("-" * 9)
    print("== Use the following commands to get started quickly:")
    print("== ")
    print("==       ops.sportsball()")
    print("==           Displays 'Sportsball' as a sanity check")
    print("== ")
    print("==       ops.help()")
    print("==           Displays this content")
    print("== ")
    print("==       ops.commands()")
    print("==           Displays a list of supported commands")
    print("==           e.g. commands=['commands', 'game', 'help', 'sports', 'sportsball']")
    print("== ")
    print("==       ops.sports()")
    print("==           Displays a list of supported sports")
    print("==           e.g. sports=['anyball', 'baseball', 'basketball', 'football', 'hockey']")
    print("== ")
    print("==       ops.game()")
    print("==           Generates game scores for default sport, using default generic team list")
    print("==           Returns JSON object")
    print("==           Syntax:")
    print("==               results = ops.game()")
    print("== ")
    print("==       ops.game(gametype='<gametype>')")
    print("==           Generates game scores for selected sport, using default team list from that sport")
    print("==           Returns JSON object")
    print("==           Syntax:")
    print("==               results = ops.game(gametype='hockey')")
    print("== ")

    print("-" * 80)


def sportsball():
    print("== sportsball !")
    print("-" * 80)


def sports():
    sports_list = get_supported_sports()
    return sports_list
