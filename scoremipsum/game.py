#
#   SCOREM
#
"""
game
----------

game functions for the `scoremipsum` module.
"""

import random
import itertools

from scoremipsum.data import TEAMS_DEFAULT
from scoremipsum.util.scheduler import grouper


def compute_score_anyball():
    score_list = [0, 1, 2, 3, 5, 8, 13, 21]
    score = (random.choice(score_list) + random.choice(score_list)
             + random.choice(score_list) + random.choice(score_list))
    return score


def compute_score_football():
    score_list = [0, 3, 7, 10]
    score = (random.choice(score_list) + random.choice(score_list)
             + random.choice(score_list) + random.choice(score_list))
    return score


def compute_score_hockey():
    score_list = [0, 1, 2]
    score = random.choice(score_list) + random.choice(score_list) + random.choice(score_list)
    return score


def get_team_data(team=None):
    """

    :param team:    identifier for specific team.
                    must also differentiate for specific sport.
    :return:
    """
    team_data = {'Offense': 2, 'Defense': 2, 'Special': 2}
    return team_data


def generate_games_from_schedule(schedule, gametype=None):
    """
    given a schedule and game type
    return a list of game_results with scores

    - needs to implement new schedule data (home / away)

    :param schedule:
    :param gametype:
    :return:
    """
    game_results = []

    print('\ngenerating game results for: ', gametype)
    for game in schedule:
        # print('game: ', game)
        # result_score = generate_score_anyball()

        # *NOTE*
        # match command available at python version 3.10
        # -----------------------------------------------------------------------------
        # match gametype:
        #     case 'hockey':
        #         result_score = generate_score_hockey()
        #     case 'football':
        #         result_score = generate_score_football()
        #     case 'anyball':
        #         result_score = generate_score_anyball()
        #     case _:
        #         result_score = generate_score_anyball()

        #   using anyball as default
        if gametype is None:
            score = generate_score_anyball()
        elif gametype == 'hockey':
            score = generate_score_hockey()
        elif gametype == 'football':
            score = generate_score_football()
        elif gametype == 'anyball':
            score = generate_score_anyball()
        else:
            score = generate_score_anyball()

        # print('-- result_score:', result_score)
        # for team_score in result_score:
        #     print(f'-- {team_score = }:', )

        game_results.append(list(zip(game, score)))

    return game_results


def generate_schedule_all_pairs(teamlist):
    """

    :param teamlist:
    :return:
    """
    # if not teamlist:
    #     return something-hardcoded
    # generate all non-repeating pairs - placeholder algorithm
    pairs = list(itertools.combinations(teamlist, 2))

    # randomly shuffle these pairs
    #   also, change test to account for shuffling
    # random.shuffle(pairs)
    return pairs


def generate_schedule_single_pairs(teamlist):
    """

    :param teamlist:
    :return:
    """
    # if not teamlist:
    #     return something-hardcoded
    # generate first non-repeating pairs - placeholder algorithm
    tmp = list(teamlist)
    randoms = [tmp.pop(random.randrange(len(tmp))) for _ in range(len(teamlist))]
    # print('result: ', randoms)
    pairs = list(grouper(randoms, 2))
    # print('pairs: ', pairs)
    return pairs


def generate_score_anyball(ruleset=None, active_team=None, opposing_team=None):
    """
    return a result_score for Anyball (pseudogame)
    teams are rated 1-5 for Offense / Defense / Special, default 2
    result_score generation:
        actSpecAdj = actSPEC*(0-1)
        oppSpecAdj = oppSPEC*(0-1)
        actScore = actOFF*(0-2) - oppDEF*(0-2) + actSpecAdj, min 0
        oppScore = oppOFF*(0-2) - actDEF*(0-2) + oppSpecAdj, min 0
    :param ruleset:
    :param active_team:
    :param opposing_team:
    :return:
    """
    if ruleset is None:
        pass

    # score = [99, 0]
    score_visitors = compute_score_anyball()
    score_home = compute_score_anyball()

    if score_visitors == score_home:
        score_visitors, score_home = score_adjust_tie(score_visitors, score_home, game="anyball")

    score = [score_visitors, score_home]

    return score


def generate_score_football(ruleset=None, active_team=None, opposing_team=None):
    """
    return a result_score for Football (US NFL)
    teams are rated 1-5 for Offense / Defense / Special, default 2
    result_score generation:
        TBD
    :param ruleset:
    :param active_team:
    :param opposing_team:
    :return:
    """
    if ruleset is None:
        pass

    score_visitors = compute_score_football()
    score_home = compute_score_football()

    if score_visitors == score_home:
        score_visitors, score_home = score_adjust_tie(score_visitors, score_home, game="football")

    score = [score_visitors, score_home]

    return score


def generate_score_hockey(ruleset=None, active_team=None, opposing_team=None):
    """
    return a result_score for Hockey (NHL)
    future:  teams are rated 1-5 for Offense / Defense / Special, default 2
    result_score generation:
        hockey (avg 1.0 goals per period, 3 periods) - 0, 1, 2
    :param ruleset:
    :param active_team:
    :param opposing_team:
    :return:
    """
    if ruleset is None:
        pass

    score_visitors = compute_score_hockey()
    score_home = compute_score_hockey()

    if score_visitors == score_home:
        score_visitors, score_home = score_adjust_tie(score_visitors, score_home, game="hockey")

    score = [score_visitors, score_home]

    return score


def score_adjust_tie(score_visitors, score_home, game=None):
    #  print(f"*** score_adjust_for_tie {score_visitors=} {score_home=} ***")
    tiebreak_score_list = []
    if game is None:
        # don't change result_score for unspecified game
        return score_visitors, score_home

    if game == "anyball":
        # don't change result_score for anyball game! #haha
        return score_visitors, score_home

    if game == "football":
        tiebreak_score_list = [3, 6]

    if game == "hockey":
        # only one option!
        tiebreak_score_list = [1]

    tiebreak_selector = random.randint(0, 1)
    tiebreaker_score = random.choice(tiebreak_score_list)

    if tiebreak_selector:
        score_home += tiebreaker_score
    else:
        score_visitors += tiebreaker_score

    return score_visitors, score_home


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
