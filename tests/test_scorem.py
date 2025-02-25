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
import unittest
from unittest import SkipTest

import scoremipsum
import scoremipsum.scoremipsum
import scoremipsum.util
from scoremipsum import game, data
from scoremipsum.util.conversion import convert_game_result_to_json
from scoremipsum.util.support import is_valid_json


class TestScorem(unittest.TestCase):
    """
        Test Cases for Scorem module
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_game_teams_default(self):
        """

        :return:
        """
        self.assertEqual(game.TEAMS_DEFAULT,
                         ['Advancers', 'Battlers', 'Clashers', 'Destroyers',
                          'Engineers', 'Fighters', 'Guardians', 'Harriers'])

    def test_game_teams_nfl_afc_east(self):
        """

        :return:
        """
        self.assertEqual(data.TEAMS_NFL_AFC_EAST,
                         ['Patriots', 'Bills', 'Dolphins', 'Jets'])

    def test_game_team_name(self):
        """

        :return:
        """

    def test_game_get_team_default_values(self):
        """

        :return:
        """
        data = game.get_team_data()
        self.assertEqual(data, {'Offense': 2, 'Defense': 2, 'Special': 2})

    def test_game_get_score_anyball(self):
        """
            simulated result_score for single game of anyball (imaginary)

        :return:
        """
        # return 2 ints, range 0-99
        score = game.generate_score_anyball()
        assert 100 > score[0] >= 0
        assert 100 > score[1] >= 0
        print(f"\nresult_score = {score}")

    def test_game_get_score_football(self):
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

    def test_game_get_score_hockey(self):
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

    @SkipTest
    # test invalid until delivery of US111: SCOREM - Specify and Enforce "Away - Home" in Schedule
    def test_generate_schedule_single_pairs(self):
        schedule_set = ('always_team_AWAY', 'always_team_HOME')
        schedule = game.generate_schedule_single_pairs(schedule_set)
        assert schedule[0][0] == 'always_team_AWAY'
        assert schedule[0][1] == 'always_team_HOME'

    def test_generate_games_from_schedule(self):
        schedule_set = ('always_team_AWAY', 'always_team_HOME')
        schedule = game.generate_schedule_single_pairs(schedule_set)
        game_results = \
            game.generate_games_from_schedule(schedule, gametype='anyball')

        return

    @SkipTest
    # fix imports to get this working
    def test_get_supported_sports_from_root(self):
        sports_list = scoremipsum.sports()
        self.assertEqual(sports_list, ['anyball', 'football', 'hockey'])

    def test_get_supported_sports_from_util(self):
        sports_list = scoremipsum.util.support.get_supported_sports()
        self.assertEqual(sports_list, ['anyball', 'football', 'hockey'])

    def test_is_supported_anyball(self):
        self.assertEqual(True, scoremipsum.util.support.check_support_anyball(), "Anyball not supported")

    @SkipTest
    def test_is_supported_baseball(self):
        self.assertEqual(True, scoremipsum.util.support.check_support_baseball(), "Baseball not supported")

    @SkipTest
    def test_is_supported_basketball(self):
        self.assertEqual(True, scoremipsum.util.support.check_support_basketball(), "Basketball not supported")

    def test_is_supported_football(self):
        self.assertEqual(True, scoremipsum.util.support.check_support_football(), "Football not supported")

    def test_is_supported_hockey(self):
        self.assertEqual(True, scoremipsum.util.support.check_support_hockey(), "Hockey not supported")

    def test_result_single_anyball(self):
        """
        verify results from anyball
        :return:
        """
        # schedule_set = ('Anyball_Away', 'Anyball_Home')
        schedule_set = ('Anyball_Team_AA', 'Anyball_Team_BB')
        schedule = game.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            game.generate_games_from_schedule(schedule, gametype='anyball')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results = }")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
        print(f"{game_results_json = }")

        is_good_json = is_valid_json(game_results_json)
        self.assertTrue(is_good_json)
        # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "anyball")


    def test_result_single_football(self):
        """

        :return:
        """
        # schedule_set = ('Football_Away', 'Football_Home')
        schedule_set = ('Football_Team_AA', 'Football_Team_BB')
        schedule = game.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            game.generate_games_from_schedule(schedule, gametype='football')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results = }")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
        print(f"{game_results_json = }")

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "football")

    def test_result_single_hockey(self):
        """

        :return:
        """
        # schedule_set = ('Hockey_Away', 'Hockey_Home')
        schedule_set = ('Hockey_Team_AA', 'Hockey_Team_BB')
        schedule = game.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            game.generate_games_from_schedule(schedule, gametype='hockey')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results = }")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
        print(f"{game_results_json = }")

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "hockey")

    def test_result_multiple_anyball(self):
        """
        verify results from anyball
        :return:
        """
        schedule_set = ('AA', 'BB', 'CC', 'DD')
        schedule = game.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            game.generate_games_from_schedule(schedule, gametype='anyball')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results = }")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
        print(f"{multi_game_results_json = }")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "anyball")

    def test_result_multiple_football(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NFL_AFC_EAST
        schedule = game.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            game.generate_games_from_schedule(schedule, gametype='football')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results = }")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
        print(f"{multi_game_results_json = }")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "football")

    def test_result_multiple_hockey(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
        schedule = game.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            game.generate_games_from_schedule(schedule, gametype='hockey')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results = }")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
        print(f"{multi_game_results_json = }")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "hockey")

    def test_schedule_all_pairs(self):
        """

        :return:
        """
        schedule_set = ('AA', 'BB', 'CC', 'DD')
        schedule = game.generate_schedule_all_pairs(schedule_set)
        schedule_expected = \
            [('AA', 'BB'), ('AA', 'CC'), ('AA', 'DD'),
             ('BB', 'CC'), ('BB', 'DD'), ('CC', 'DD')]
        self.assertEqual(schedule, schedule_expected)
        print(f"\nschedule = {schedule}")

    def test_schedule_single_pairs(self):
        """

        :return:
        """
        schedule_set = ('AA', 'BB', 'CC', 'DD')
        schedule = game.generate_schedule_single_pairs(schedule_set)
        self.assertEqual(len(sorted(schedule)), 2)
        print(f"\nschedule = {schedule}")

    def test_schedule_single_pairs_default(self):
        """

        :return:
        """
        schedule_set = game.TEAMS_DEFAULT
        schedule = game.generate_schedule_single_pairs(schedule_set)
        self.assertEqual(len(sorted(schedule)), 4)
        print(f"\ndefault teams schedule = {schedule}")

    def test_schedule_single_pairs_nfl_afc_east(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NFL_AFC_EAST
        schedule = game.generate_schedule_single_pairs(schedule_set)
        self.assertEqual(len(sorted(schedule)), 2)
        print(f"\nnfl afc east schedule = {schedule}")

    def test_schedule_single_pairs_nhl_eastern_atlantic(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
        schedule = game.generate_schedule_single_pairs(schedule_set)
        self.assertEqual(4, len(sorted(schedule)))
        print(f"\nnhl eastern atlantic schedule = {schedule}")


if __name__ == '__main__':
    import sys

    sys.exit(unittest.main())
