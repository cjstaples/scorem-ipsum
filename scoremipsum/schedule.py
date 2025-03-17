import itertools
import random

from scoremipsum.score import generate_score_anyball, generate_score_hockey, generate_score_football, \
    generate_score_baseball, generate_score_basketball
from scoremipsum.util.scheduler import grouper


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
        elif gametype == 'baseball':
            score = generate_score_baseball()
        elif gametype == 'basketball':
            score = generate_score_basketball()
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
