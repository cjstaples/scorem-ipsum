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
from scoremipsum import game, data
from scoremipsum.scoremipsum import sports
from scoremipsum.util.conversion import convert_game_result_to_json
from scoremipsum.util.support import is_valid_json
from scoremipsum.data import TEAMS_NFL_AFC_EAST

@pytest.fixture()
def teamlist_nfl_afc_east():
    return TEAMS_NFL_AFC_EAST


def test_data_get_teamlist_nfl_afc_east():
    assert data.TEAMS_NFL_AFC_EAST ==  ['Patriots', 'Bills', 'Dolphins', 'Jets']

def test_data_get_via_fixture_teamlist_nfl_afc_east(teamlist_nfl_afc_east):
    assert data.TEAMS_NFL_AFC_EAST == teamlist_nfl_afc_east

def test_game_get_team_default_values():
    team_data = game.get_team_data()
    assert team_data == {'Offense': 2, 'Defense': 2, 'Special': 2}

def test_game_get_teamlist_default():
    assert game.TEAMS_DEFAULT ==  ['Advancers', 'Battlers', 'Clashers', 'Destroyers', 'Engineers', 'Fighters', 'Guardians', 'Harriers']

def test_game_get_score_anyball():
    """
        simulated result_score for single game of anyball (imaginary)

    :return:
    """
    # return 2 ints, range 0-99
    score = game.generate_score_anyball()
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
    score = game.generate_score_football()
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
    score = game.generate_score_hockey()
    assert 17 > score[0] >= 0
    assert 17 > score[1] >= 0
    assert 22 > (score[0] + score[1]) >= 0
    print(f"\nresult_score = {score}")

# test invalid until delivery of US111: SCOREM - Specify and Enforce "Away - Home" in Schedule
@pytest.mark.skip(reason='US111')
def test_generate_schedule_single_pairs():
    schedule_set = ('always_team_AWAY', 'always_team_HOME')
    schedule = game.generate_schedule_single_pairs(schedule_set)
    assert schedule[0][0] == 'always_team_AWAY'
    assert schedule[0][1] == 'always_team_HOME'

def test_generate_games_from_schedule():
    schedule_set = ('always_team_AWAY', 'always_team_HOME')
    schedule = game.generate_schedule_single_pairs(schedule_set)
    game_results = \
        game.generate_games_from_schedule(schedule, gametype='anyball')
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
