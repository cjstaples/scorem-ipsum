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
from scoremipsum.util.support import get_supported_sports, get_command_list, get_help_content
from scoremipsum.util.team import get_default_teamlist_from_gametype


def game(gametype=None):
    if not gametype:
        gametype = 'anyball'
    teamlist = get_default_teamlist_from_gametype(gametype)
    schedule = generate_schedule_single_pairs(teamlist)
    game_generation_results = generate_games_from_schedule(schedule, gametype=gametype)
    game_results_json = convert_game_result_to_json(game_generation_results, gametype=gametype)
    return game_results_json


def commands():
    command_list = get_command_list()
    return command_list


def help():
    help_content = get_help_content()
    print(help_content)


def sportsball():
    print("== sportsball !")
    print("-" * 80)


def sports():
    sports_list = get_supported_sports()
    return sports_list
