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
from scoremipsum.generation import get_score_anyball
from scoremipsum.ops import sports
from scoremipsum.score import generate_score_anyball, generate_score_hockey, generate_score_football
from scoremipsum.schedule import generate_games_from_schedule, generate_schedule_all_pairs, generate_schedule_single_pairs, generate_score_anyball, generate_score_hockey, generate_score_football
from scoremipsum.util.conversion import convert_game_result_to_json
from scoremipsum.util.support import is_valid_json
from scoremipsum.util.team import get_team_data, get_default_teamlist_from_gametype

@pytest.fixture()
def teamlist_nfl_afc_east():
    return TEAMS_NFL_AFC_EAST


def test_data_get_teamlist_nfl_afc_east():
    assert data.TEAMS_NFL_AFC_EAST ==  ['Patriots', 'Bills', 'Dolphins', 'Jets']

def test_data_get_via_fixture_teamlist_nfl_afc_east(teamlist_nfl_afc_east):
    assert data.TEAMS_NFL_AFC_EAST == teamlist_nfl_afc_east

def test_game_get_team_default_values():
    team_data = scoremipsum.util.team.get_team_data()
    assert team_data == {'Offense': 2, 'Defense': 2, 'Special': 2}

def test_game_get_teamlist_default():
    assert scoremipsum.data.TEAMS_DEFAULT == ['Advancers', 'Battlers', 'Clashers', 'Destroyers', 'Engineers', 'Fighters', 'Guardians', 'Harriers']

def test_game_get_score_anyball():
    """
        simulated result_score for single game of anyball (imaginary)

    :return:
    """
    # return 2 ints, range 0-99
    score = scoremipsum.score.generate_score_anyball()
    assert 100 > score[0] >= 0
    assert 100 > score[1] >= 0
    print(f"\nresult_score = {score}")

def test_game_get_score_football():
    """
        simulated result_score for single game of football
        nfl record for single team result_score is 73
        nfl record for both teams combined result_score is 113
    :return:
    """
    # return 2 ints, range 0-74, total < 120
    # this will be weighted for realism and tests adjusted
    score = scoremipsum.score.generate_score_football()
    assert 75 > score[0] >= 0
    assert 75 > score[1] >= 0
    assert 120 > (score[0] + score[1]) >= 0
    print(f"\nresult_score = {score}")

def test_game_get_score_hockey():
    """
        simulated result_score for single game of hockey
        nhl record for single team result_score is 16
        nhl record for both teams combined result_score is 21
    :return:
    """
    # return 2 ints, range 0-16, total < 22
    # this will be weighted for realism and tests adjusted
    score = scoremipsum.score.generate_score_hockey()
    assert 17 > score[0] >= 0
    assert 17 > score[1] >= 0
    assert 22 > (score[0] + score[1]) >= 0
    print(f"\nresult_score = {score}")

# test invalid until delivery of US111: SCOREM - Specify and Enforce "Away - Home" in Schedule
@pytest.mark.skip(reason='US111')
def test_generate_schedule_single_pairs():
    schedule_set = ('always_team_AWAY', 'always_team_HOME')
    schedule = scoremipsum.generation.generate_schedule_single_pairs(schedule_set)
    assert schedule[0][0] == 'always_team_AWAY'
    assert schedule[0][1] == 'always_team_HOME'

def test_generate_games_from_schedule():
    schedule_set = ('always_team_AWAY', 'always_team_HOME')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_results = \
        scoremipsum.schedule.generate_games_from_schedule(schedule, gametype='anyball')
    assert game_results is not None

def test_get_supported_sports_from_root():
    sports_list = sports()
    assert sports_list == ['anyball', 'football', 'hockey']

def test_get_supported_sports_from_util():
    sports_list = scoremipsum.util.support.get_supported_sports()
    assert sports_list == ['anyball', 'football', 'hockey']

def test_is_supported_anyball():
    assert True == scoremipsum.util.support.check_support_anyball()

def test_is_supported_baseball():
    assert False == scoremipsum.util.support.check_support_baseball()

def test_is_supported_basketball():
    assert False == scoremipsum.util.support.check_support_basketball()

def test_is_supported_football():
    assert True == scoremipsum.util.support.check_support_football()

def test_is_supported_hockey():
    assert True == scoremipsum.util.support.check_support_hockey()

def test_result_single_anyball():
    # schedule_set = ('Anyball_Away', 'Anyball_Home')
    schedule_set = ('Anyball_Team_AA', 'Anyball_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        scoremipsum.schedule.generate_games_from_schedule(schedule, gametype='anyball')
    assert len(schedule_set) / 2 == len(game_generation_results)

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
    print(f"{game_results_json = }")

    is_good_json = is_valid_json(game_results_json)
    assert is_good_json == True
    # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "anyball"

def test_result_single_football():
    # schedule_set = ('Football_Away', 'Football_Home')
    schedule_set = ('Football_Team_AA', 'Football_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        scoremipsum.schedule.generate_games_from_schedule(schedule, gametype='football')
    assert len(schedule_set) / 2 == len(game_generation_results)
    # print(f"{game_generation_results = }")

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
    print(f"{game_results_json = }")

    is_good_json = is_valid_json(game_results_json)
    assert is_good_json == True
    # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "football"

def test_result_single_hockey():
    # schedule_set = ('Hockey_Away', 'Hockey_Home')
    schedule_set = ('Hockey_Team_AA', 'Hockey_Team_BB')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        scoremipsum.schedule.generate_games_from_schedule(schedule, gametype='hockey')
    assert len(schedule_set) / 2 == len(game_generation_results)
    # print(f"{game_generation_results = }")

    # verify US96: Results reduce ties.  Temporary until ties are permitted.
    assert game_generation_results[0][0][1] != game_generation_results[0][1][1]

    game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
    print(f"{game_results_json = }")

    gametype = json.loads(game_results_json)[0]["gametype"]
    assert gametype == "hockey"

def test_result_multiple_anyball():
    schedule_set = ('AA', 'BB', 'CC', 'DD')
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        scoremipsum.schedule.generate_games_from_schedule(schedule, gametype='anyball')
    assert len(schedule_set) / 2 == len(game_generation_results)
    # print(f"{game_generation_results = }")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
    print(f"{multi_game_results_json = }")

    gametype = json.loads(multi_game_results_json)[0]["gametype"]
    assert gametype == "anyball"

def test_result_multiple_football():
    schedule_set = data.TEAMS_NFL_AFC_EAST
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        scoremipsum.schedule.generate_games_from_schedule(schedule, gametype='football')
    assert len(schedule_set) / 2 == len(game_generation_results)
    # print(f"{game_generation_results = }")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
    print(f"{multi_game_results_json = }")

    gametype = json.loads(multi_game_results_json)[0]["gametype"]
    assert gametype == "football"

def test_result_multiple_hockey():
    schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    game_generation_results = \
        scoremipsum.schedule.generate_games_from_schedule(schedule, gametype='hockey')
    assert len(schedule_set) / 2 == len(game_generation_results)
    # print(f"{game_generation_results = }")

    multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
    print(f"{multi_game_results_json = }")

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

def test_schedule_single_pairs_nfl_afc_east():
    schedule_set = data.TEAMS_NFL_AFC_EAST
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    assert len(sorted(schedule)) == 2
    print(f"\nnfl afc east schedule = {schedule}")

def test_schedule_single_pairs_nhl_eastern_atlantic():
    schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
    schedule = scoremipsum.schedule.generate_schedule_single_pairs(schedule_set)
    assert len(sorted(schedule)) == 4
    print(f"\nnhl eastern atlantic schedule = {schedule}")

if __name__ == '__main__':
    import sys

    sys.exit()
