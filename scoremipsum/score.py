import random


def compute_score_anyball():
    score_list = [0, 1, 2, 3, 5, 8, 13, 21]
    score = (random.choice(score_list) + random.choice(score_list)
             + random.choice(score_list) + random.choice(score_list))
    return score


def compute_score_baseball():
    # casual model based roughly on:  https://gregstoll.com/~gregstoll/baseball/runsperinning.html
    # 73% chance of 0 runs
    # 15% chance of 1 run
    #  7% chance of 2 runs
    #  3% chance of 3 runs
    #  2% chance of 4 runs (or more) -- four max is good enough for now
    # BACKLOG US143: Implement a better weighted range here
    score = 0
    score_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 4]
    for inning in range(1, 9):
        score += random.choice(score_list)
    return score


def compute_score_basketball():
    # no model yet, just some random-ish numbers
    score_list = [20, 25, 26, 27, 28, 29, 30, 35]
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


def generate_score_baseball(ruleset=None, active_team=None, opposing_team=None):
    """
    return a result_score for Baseball (US MLB)
    teams are rated 1-5 for Offense / Defense / Pitching, default 2
    result_score generation:
        TBD
    :param ruleset:
    :param active_team:
    :param opposing_team:
    :return:
    """
    if ruleset is None:
        pass

    score_visitors = compute_score_baseball()
    score_home = compute_score_baseball()

    if score_visitors == score_home:
        score_visitors, score_home = score_adjust_tie(score_visitors, score_home, game="baseball")

    score = [score_visitors, score_home]

    return score


def generate_score_basketball(ruleset=None, active_team=None, opposing_team=None):
    """
    return a result_score for Basketball (US NBA)
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

    score_visitors = compute_score_basketball()
    score_home = compute_score_basketball()

    if score_visitors == score_home:
        score_visitors, score_home = score_adjust_tie(score_visitors, score_home, game="basketball")

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

    if game == "baseball":
        tiebreak_score_list = [1, 1, 1, 1, 1, 1, 1, 2, 3, 4]

    if game == "basketball":
        # BACKLOG US144: basketball overtimes need to account for both teams' scores
        tiebreak_score_list = [5, 6, 6, 7, 7, 7, 8, 8, 9]

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
