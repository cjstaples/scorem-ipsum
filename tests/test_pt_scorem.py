#!/usr/bin/env python
#
#   SCOREM
#
"""
test_scorem
----------

Tests for the `scoremipsum` module.
"""
import json

import pytest

import scoremipsum
from scoremipsum import data
from scoremipsum.data import TEAMS_NFL_AFC_EAST
from scoremipsum.ops import sports
from scoremipsum.schedule import generate_games_from_schedule, generate_schedule_single_pairs
from scoremipsum.score import (generate_score_anyball, generate_score_hockey,
                               generate_score_football, generate_score_baseball, generate_score_basketball)
from scoremipsum.util.conversion import convert_game_result_to_json
from scoremipsum.util.support import is_valid_json
from scoremipsum.util.team import get_team_data


@pytest.fixture()
def teamlist_nfl_afc_east():
    return TEAMS_NFL_AFC_EAST


def test_data_get_teamlist_nfl_afc_east():
    assert data.TEAMS_NFL_AFC_EAST == ['Patriots', 'Bills', 'Dolphins', 'Jets']


def test_data_get_via_fixture_teamlist_nfl_afc_east(teamlist_nfl_afc_east):
    assert data.TEAMS_NFL_AFC_EAST == teamlist_nfl_afc_east


def test_game_get_team_default_values():
    team_data = get_team_data()
    assert team_data == {'Offense': 2, 'Defense': 2, 'Special': 2}


def test_game_get_teamlist_default():
    assert scoremipsum.data.TEAMS_DEFAULT == ['Advancers', 'Battlers', 'Clashers', 'Destroyers', 'Engineers',
                                              'Fighters', 'Guardians', 'Harriers']


def test_score_generate_score_anyball():
    """
        simulated result_score for single game of anyball (imaginary)

    :return:
    """
    # return 2 ints, range 0-99
    game_score = generate_score_anyball()
    assert 100 > game_score[0] >= 0
    assert 100 > game_score[1] >= 0
    print(f"\nresult_score = {game_score}")


def test_score_generate_score_baseball():
    """
        simulated result_score for single game of anyball (imaginary)

    :return:
    """
    # return 2 ints, range 0-99
    game_score = generate_score_baseball()
    assert 100 > game_score[0] >= 0
    assert 100 > game_score[1] >= 0
    print(f"\nresult_score = {game_score}")


def test_score_generate_score_basketball():
    """
        simulated result_score for single game of anyball (imaginary)

    :return:
    """
    # return 2 ints, range 0-149
    game_score = generate_score_basketball()
    assert 150 > game_score[0] >= 0
    assert 150 > game_score[1] >= 0
    print(f"\nresult_score = {game_score}")


def test_score_generate_score_football():
    """
        simulated result_score for single game of football
        nfl record for single team result_score is 73
        nfl record for both teams combined result_score is 113
    :return:
    """
    # return 2 ints, range 0-74, total < 120
    # this will be weighted for realism and tests adjusted
    game_score = generate_score_football()
    assert 75 > game_score[0] >= 0
    assert 75 > game_score[1] >= 0
    assert 120 > (game_score[0] + game_score[1]) >= 0
    print(f"\nresult_score = {game_score}")


def test_score_generate_score_hockey():
    """
        simulated result_score for single game of hockey
        nhl record for single team result_score is 16
        nhl record for both teams combined result_score is 21
    :return:
    """
    # return 2 ints, range 0-16, total < 22
    # this will be weighted for realism and tests adjusted
    game_score = generate_score_hockey()
    assert 17 > game_score[0] >= 0
    assert 17 > game_score[1] >= 0
    assert 22 > (game_score[0] + game_score[1]) >= 0
    print(f"\nresult_score = {game_score}")


# test invalid until delivery of US111: SCOREM - Specify and Enforce "Away - Home" in Schedule
@pytest.mark.skip(reason='US111')
def test_generate_schedule_single_pairs():
    schedule_set = ('always_team_AWAY', 'always_team_HOME')
    schedule = generate_schedule_single_pairs(schedule_set)
    assert schedule[0][0] == 'always_team_AWAY'
    assert schedule[0][1] == 'always_team_HOME'


def test_generate_games_from_schedule():
    schedule_set = ('always_team_AWAY', 'always_team_HOME')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_results = \
        generate_games_from_schedule(schedule, gametype='anyball')
    assert game_results is not None


def test_get_supported_sports_from_root():
    sports_list = sports()
    assert sports_list == ['anyball', 'baseball', 'basketball', 'football', 'hockey']


def test_get_supported_sports_from_util():
    sports_list = scoremipsum.util.support.get_supported_sports()
    assert sports_list == ['anyball', 'baseball', 'basketball', 'football', 'hockey']


def test_is_supported_anyball():
    assert scoremipsum.util.support.check_support_anyball() is True


def test_is_supported_baseball():
    assert scoremipsum.util.support.check_support_baseball() is True


def test_is_supported_basketball():
    assert scoremipsum.util.support.check_support_basketball() is True


def test_is_supported_football():
    assert scoremipsum.util.support.check_support_football() is True


def test_is_supported_hockey():
    assert scoremipsum.util.support.check_support_hockey() is True


def test_result_single_anyball():
    # schedule_set = ('Anyball_Away', 'Anyball_Home')
    schedule_set = ('Anyball_Team_AA', 'Anyball_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='anyball')
    assert len(schedule_set) // 2 == len(game_generation_results)

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    # assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
    print(f"{game_results_json=}")

    is_good_json = is_valid_json(game_results_json)
    assert is_good_json is True
    # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "anyball"


def test_result_single_baseball():
    # schedule_set = ('Baseball_Away', 'Baseball_Home')
    schedule_set = ('Baseball_Team_AA', 'Baseball_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='baseball')
    assert len(schedule_set) // 2 == len(game_generation_results)

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='baseball')
    print(f"{game_results_json=}")

    is_good_json = is_valid_json(game_results_json)
    assert is_good_json is True
    # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "baseball"


def test_result_single_basketball():
    # schedule_set = ('Basketball_Away', 'Basketball_Home')
    schedule_set = ('Basketball_Team_AA', 'Basketball_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='basketball')
    assert len(schedule_set) // 2 == len(game_generation_results)

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='basketball')
    print(f"{game_results_json=}")

    is_good_json = is_valid_json(game_results_json)
    assert is_good_json is True
    # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "basketball"


def test_result_single_football():
    # schedule_set = ('Football_Away', 'Football_Home')
    schedule_set = ('Football_Team_AA', 'Football_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='football')
    assert len(schedule_set) // 2 == len(game_generation_results)
    # print(f"{game_generation_results=}")

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
    print(f"{game_results_json=}")

    is_good_json = is_valid_json(game_results_json)
    assert is_good_json is True
    # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "football"


def test_result_single_hockey():
    # schedule_set = ('Hockey_Away', 'Hockey_Home')
    schedule_set = ('Hockey_Team_AA', 'Hockey_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='hockey')
    assert len(schedule_set) // 2 == len(game_generation_results)
    # print(f"{game_generation_results=}")

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
    print(f"{game_results_json=}")

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "hockey"


def test_result_multiple_anyball():
    schedule_set = ('AA', 'BB', 'CC', 'DD')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='anyball')
    assert len(schedule_set) // 2 == len(game_generation_results)
    # print(f"{game_generation_results=}")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
    print(f"{multi_game_results_json=}")

    gametype = json.loads(multi_game_results_json)[0]["gametype"]
    assert gametype == "anyball"


def test_result_multiple_baseball():
    schedule_set = data.TEAMS_MLB_AL_EAST
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='baseball')
    assert len(schedule_set) // 2 == len(game_generation_results)
    # print(f"{game_generation_results=}")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='baseball')
    print(f"{multi_game_results_json=}")

    gametype = json.loads(multi_game_results_json)[0]["gametype"]
    assert gametype == "baseball"


def test_result_multiple_basketball():
    schedule_set = data.TEAMS_NBA_EASTERN_CENTRAL
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='basketball')
    assert len(schedule_set) // 2 == len(game_generation_results)
    # print(f"{game_generation_results=}")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='basketball')
    print(f"{multi_game_results_json=}")

    gametype = json.loads(multi_game_results_json)[0]["gametype"]
    assert gametype == "basketball"


def test_result_multiple_football():
    schedule_set = data.TEAMS_NFL_AFC_EAST
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='football')
    assert len(schedule_set) // 2 == len(game_generation_results)
    # print(f"{game_generation_results=}")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
    print(f"{multi_game_results_json=}")

    gametype = json.loads(multi_game_results_json)[0]["gametype"]
    assert gametype == "football"


def test_result_multiple_hockey():
    schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        generate_games_from_schedule(schedule, gametype='hockey')
    assert len(schedule_set) // 2 == len(game_generation_results)
    # print(f"{game_generation_results=}")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
    print(f"{multi_game_results_json=}")

    gametype = json.loads(multi_game_results_json)[0]["gametype"]
    assert gametype == "hockey"


def test_schedule_all_pairs():
    schedule_set = ('AA', 'BB', 'CC', 'DD')
    schedule = scoremipsum.schedule.generate_schedule_all_pairs(schedule_set)
    schedule_expected = \
        [('AA', 'BB'), ('AA', 'CC'), ('AA', 'DD'),
         ('BB', 'CC'), ('BB', 'DD'), ('CC', 'DD')]
    assert schedule == schedule_expected
    print(f"\nschedule = {schedule}")


def test_schedule_single_pairs():
    schedule_set = ('AA', 'BB', 'CC', 'DD')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    assert len(sorted(schedule)) == 2
    print(f"\nschedule = {schedule}")


def test_schedule_single_pairs_default():
    schedule_set = scoremipsum.data.TEAMS_DEFAULT
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    assert len(sorted(schedule)) == 4
    print(f"\ndefault teams schedule = {schedule}")


def test_schedule_single_pairs_mlb_al_east():
    schedule_set = data.TEAMS_MLB_AL_EAST
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    assert len(sorted(schedule)) == 2
    for game in schedule:
        for team in game:
            assert team in data.TEAMS_MLB_AL_EAST
    print(f"\nmlb al east schedule = {schedule}")


def test_schedule_single_pairs_nfl_afc_east():
    schedule_set = data.TEAMS_NFL_AFC_EAST
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    assert len(sorted(schedule)) == 2
    for game in schedule:
        for team in game:
            assert team in data.TEAMS_NFL_AFC_EAST
    print(f"\nnfl afc east schedule = {schedule}")


def test_schedule_single_pairs_nhl_eastern_atlantic():
    schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    assert len(sorted(schedule)) == 4
    for game in schedule:
        for team in game:
            assert team in data.TEAMS_NHL_EASTERN_ATLANTIC
    print(f"\nnhl eastern atlantic schedule = {schedule}")


if __name__ == '__main__':
    import sys

    sys.exit()
