#
#   SCOREM
#
"""
Scorem
----------

Scorem functions for the `scorem` module.
"""
import inspect
import scorem
from scorem.util import get_supported_sports


def game(gametype=None):
    print("game() not yet implemented !")


def commands():
    method_list = [func for func in dir(scorem.scorem) if callable(getattr(scorem.scorem, func)) and not func.startswith("_") and not func.startswith("get_")]
    return method_list


def help():
    print("help() not yet implemented !")


def sportsball():
    print("== sportsball !")
    print("-"*80)


def sports():
    sports_list = get_supported_sports()
    return sports_list
