#
#   SCOREM
#
"""
Scorem
----------

Scorem functions for the `scoremipsum` module.
"""

from scoremipsum.generation import get_game
from scoremipsum.util.support import get_command_list, get_config, get_help_content, get_sports_supported


def game(gametype=None):
    game_results_json = get_game(gametype=gametype)
    return game_results_json


def commands():
    command_list = get_command_list()
    return command_list


def config():
    # placeholder for config support
    config_settings = get_config()
    return config_settings


def help():
    help_content = get_help_content()
    print(help_content)


def sportsball():
    print("== sportsball !")
    print("-" * 80)


def sports():
    sports_list = get_sports_supported()
    return sports_list
