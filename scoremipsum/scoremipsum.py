#
#   SCOREM
#
"""
Scorem
----------

Scorem functions for the `scoremipsum` module.
"""
import inspect
import scoremipsum
from scoremipsum.util.support import get_supported_sports


def game(gametype=None):
    print("game() not yet implemented !")


def commands():
    method_list = [func for func in dir(scoremipsum.scoremipsum) if callable(getattr(scoremipsum.scoremipsum, func)) and not func.startswith("_") and not func.startswith("get_")]
    return method_list


def help():
    print("help() not yet implemented !")


def sportsball():
    print("== sportsball !")
    print("-"*80)


def sports():
    sports_list = get_supported_sports()
    return sports_list
