#
#   SCOREM
#
"""
game
----------

game functions for the `scoremipsum` module.
"""

import random

from scoremipsum.data import TEAMS_DEFAULT
from scoremipsum.score import generate_score_anyball, generate_score_football, generate_score_hockey
from scoremipsum.util.team import get_team_data


@staticmethod
def get_score_anyball(active_team_data=None, opposing_team_data=None):
    """
    :param active_team_data:
    :param opposing_team_data:
    :return:
    """
    ruleset = {'anyball'}

    if not active_team_data:
        active_team_data = get_team_data()
    if not opposing_team_data:
        opposing_team_data = get_team_data()

    score = generate_score_anyball(ruleset, active_team_data, opposing_team_data)
    return score


@staticmethod
def get_score_football(active_team_data=None, opposing_team_data=None):
    """
    :param active_team_data:
    :param opposing_team_data:
    :return:
    """
    ruleset = {'football'}

    if not active_team_data:
        active_team_data = get_team_data()
    if not opposing_team_data:
        opposing_team_data = get_team_data()

    score = generate_score_football(ruleset, active_team_data, opposing_team_data)
    return score


@staticmethod
def get_score_hockey(active_team_data=None, opposing_team_data=None):
    """
    :param active_team_data:
    :param opposing_team_data:
    :return:
    """
    ruleset = {'hockey'}

    if not active_team_data:
        active_team_data = get_team_data()
    if not opposing_team_data:
        opposing_team_data = get_team_data()

    score = generate_score_hockey(ruleset, active_team_data, opposing_team_data)
    return score


class GameGeneration:
    """
    game generation class for the `scoremipsum` module.
    """

    def __init__(self, teams=None):
        if teams:
            self._teams = teams
        else:
            self._teams = TEAMS_DEFAULT

    def _team(self):
        return random.choice(self._teams)

    # TODO:  figure out why these aren't used, and remove the xget test function
    @staticmethod
    def xget_score_anyball(active_team_data=None, opposing_team_data=None):
        """
        :param active_team_data:
        :param opposing_team_data:
        :return:
        """
        ruleset = {'anyball'}

        if not active_team_data:
            active_team_data = get_team_data()
        if not opposing_team_data:
            opposing_team_data = get_team_data()

        score = generate_score_anyball(ruleset, active_team_data, opposing_team_data)
        return score
