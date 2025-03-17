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
from scoremipsum import data, schedule
from scoremipsum.ops import sports
from scoremipsum.schedule import generate_schedule_single_pairs, generate_games_from_schedule, \
    generate_schedule_all_pairs
from scoremipsum.score import generate_score_anyball, generate_score_football, \
    generate_score_hockey, generate_score_baseball, generate_score_basketball
from scoremipsum.util.conversion import convert_game_result_to_json
from scoremipsum.util.support import is_valid_json
from scoremipsum.util.team import get_team_data


class TestUtScorem(unittest.TestCase):
    """
        Test Cases for Scorem module
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_data_get_teamlist_nfl_afc_east(self):
        """

        :return:
        """
        self.assertEqual(data.TEAMS_NFL_AFC_EAST,
                         ['Patriots', 'Bills', 'Dolphins', 'Jets'])

    def test_game_get_team_default_values(self):
        """

        :return:
        """
        team_data = get_team_data()
        self.assertEqual(team_data, {'Offense': 2, 'Defense': 2, 'Special': 2})

    def test_data_get_teamlist_default(self):
        """

        :return:
        """
        self.assertEqual(data.TEAMS_DEFAULT,
                         ['Advancers', 'Battlers', 'Clashers', 'Destroyers',
                          'Engineers', 'Fighters', 'Guardians', 'Harriers'])

    def test_game_get_score_anyball(self):
        """
            simulated result_score for single game of anyball (imaginary)

        :return:
        """
        # return 2 ints, range 0-99
        game_score = generate_score_anyball()
        assert 100 > game_score[0] >= 0
        assert 100 > game_score[1] >= 0
        print(f"\nresult_score = {game_score}")

    def test_game_get_score_baseball(self):
        """
            simulated result_score for single game of anyball (imaginary)

        :return:
        """
        # return 2 ints, range 0-36
        game_score = generate_score_baseball()
        assert 37 > game_score[0] >= 0
        assert 37 > game_score[1] >= 0
        print(f"\nresult_score = {game_score}")

    def test_game_get_score_basketball(self):
        """
            simulated result_score for single game of anyball (imaginary)

        :return:
        """
        # return 2 ints, range 0-149 (0-140, ot 5-9)
        game_score = generate_score_basketball()
        assert 150 > game_score[0] >= 0
        assert 150 > game_score[1] >= 0
        print(f"\nresult_score = {game_score}")

    def test_game_get_score_football(self):
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

    def test_game_get_score_hockey(self):
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

    @SkipTest
    # test invalid until delivery of US111: SCOREM - Specify and Enforce "Away - Home" in Schedule
    def test_generate_schedule_single_pairs(self):
        schedule_set = ('always_team_AWAY', 'always_team_HOME')
        game_schedule = schedule.generate_schedule_single_pairs(schedule_set)
        assert game_schedule[0][0] == 'always_team_AWAY'
        assert game_schedule[0][1] == 'always_team_HOME'

    def test_generate_games_from_schedule(self):
        schedule_set = ('always_team_AWAY', 'always_team_HOME')
        game_schedule = generate_schedule_single_pairs(schedule_set)
        game_results = \
            generate_games_from_schedule(game_schedule, gametype='anyball')
        assert game_results is not None

    def test_get_supported_sports_from_root(self):
        sports_list = sports()
        self.assertEqual(sports_list, ['anyball', 'baseball', 'basketball', 'football', 'hockey'])

    def test_get_supported_sports_from_util(self):
        sports_list = scoremipsum.util.support.get_supported_sports()
        self.assertEqual(sports_list, ['anyball', 'baseball', 'basketball', 'football', 'hockey'])

    def test_is_supported_anyball(self):
        self.assertEqual(True, scoremipsum.util.support.check_support_anyball(), "Anyball not supported")

    def test_is_supported_baseball(self):
        self.assertEqual(True, scoremipsum.util.support.check_support_baseball(), "Baseball not supported")

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
        game_schedule = generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            generate_games_from_schedule(game_schedule, gametype='anyball')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        # print(f"RES SINGLE ANY {game_generation_results}=")
        # self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
        print(f"{game_results_json=}")

        is_good_json = is_valid_json(game_results_json)
        self.assertTrue(is_good_json)
        # NOT GOOD ENOUGH FOR JSON CONTENT CHECKS THOUGH!

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "anyball")

    def test_result_single_baseball(self):
        """

        :return:
        """
        # schedule_set = ('Baseball_Away', 'Baseball_Home')
        schedule_set = ('Baseball_Team_AA', 'Baseball_Team_BB')
        game_schedule = schedule.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            schedule.generate_games_from_schedule(game_schedule, gametype='baseball')
        self.assertEqual(len(schedule_set) // 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='baseball')
        print(f"{game_results_json=}")

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "baseball")

    def test_result_single_basketball(self):
        """

        :return:
        """
        # schedule_set = ('Basketball_Away', 'Basketball_Home')
        schedule_set = ('Basketball_Team_AA', 'Basketball_Team_BB')
        game_schedule = schedule.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            schedule.generate_games_from_schedule(game_schedule, gametype='basketball')
        self.assertEqual(len(schedule_set) // 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='basketball')
        print(f"{game_results_json=}")

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "basketball")

    def test_result_single_football(self):
        """

        :return:
        """
        # schedule_set = ('Football_Away', 'Football_Home')
        schedule_set = ('Football_Team_AA', 'Football_Team_BB')
        game_schedule = generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            generate_games_from_schedule(game_schedule, gametype='football')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
        print(f"{game_results_json=}")

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "football")

    def test_result_single_hockey(self):
        """

        :return:
        """
        # schedule_set = ('Hockey_Away', 'Hockey_Home')
        schedule_set = ('Hockey_Team_AA', 'Hockey_Team_BB')
        game_schedule = generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            generate_games_from_schedule(game_schedule, gametype='hockey')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        # verify US96: Results reduce ties.  Temporary until ties are permitted.
        self.assertFalse(game_generation_results[0][0][1] == game_generation_results[0][1][1])

        game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
        print(f"{game_results_json=}")

        gametype = json.loads(game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "hockey")

    def test_result_multiple_anyball(self):
        """
        verify results from anyball
        :return:
        """
        schedule_set = ('AA', 'BB', 'CC', 'DD')
        game_schedule = generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            generate_games_from_schedule(game_schedule, gametype='anyball')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')
        print(f"{multi_game_results_json=}")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "anyball")

    def test_result_multiple_baseball(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_MLB_AL_EAST
        game_schedule = schedule.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            schedule.generate_games_from_schedule(game_schedule, gametype='baseball')
        self.assertEqual(len(schedule_set) // 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='baseball')
        print(f"{multi_game_results_json=}")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "baseball")

    def test_result_multiple_basketball(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NBA_EASTERN_CENTRAL
        game_schedule = schedule.generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            schedule.generate_games_from_schedule(game_schedule, gametype='basketball')
        self.assertEqual(len(schedule_set) // 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='basketball')
        print(f"{multi_game_results_json=}")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "basketball")

    def test_result_multiple_football(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NFL_AFC_EAST
        game_schedule = generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            generate_games_from_schedule(game_schedule, gametype='football')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')
        print(f"{multi_game_results_json=}")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "football")

    def test_result_multiple_hockey(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
        game_schedule = generate_schedule_single_pairs(schedule_set)
        game_generation_results = \
            generate_games_from_schedule(game_schedule, gametype='hockey')
        self.assertEqual(len(schedule_set) / 2, len(game_generation_results))
        # print(f"{game_generation_results=}")

        multi_game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')
        print(f"{multi_game_results_json=}")

        gametype = json.loads(multi_game_results_json)[0]["gametype"]
        self.assertEqual(gametype, "hockey")

    def test_schedule_all_pairs(self):
        """

        :return:
        """
        schedule_set = ('AA', 'BB', 'CC', 'DD')
        game_schedule = generate_schedule_all_pairs(schedule_set)
        schedule_expected = \
            [('AA', 'BB'), ('AA', 'CC'), ('AA', 'DD'),
             ('BB', 'CC'), ('BB', 'DD'), ('CC', 'DD')]
        self.assertEqual(game_schedule, schedule_expected)
        print(f"\ngame_schedule = {game_schedule}")

    def test_schedule_single_pairs(self):
        """

        :return:
        """
        schedule_set = ('AA', 'BB', 'CC', 'DD')
        game_schedule = generate_schedule_single_pairs(schedule_set)
        self.assertEqual(len(sorted(game_schedule)), 2)
        print(f"\nschedule = {game_schedule}")

    def test_schedule_single_pairs_default(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_DEFAULT
        game_schedule = generate_schedule_single_pairs(schedule_set)
        self.assertEqual(len(sorted(game_schedule)), 4)
        print(f"\ndefault teams schedule = {game_schedule}")

    def test_schedule_single_pairs_nfl_afc_east(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NFL_AFC_EAST
        game_schedule = generate_schedule_single_pairs(schedule_set)
        self.assertEqual(len(sorted(game_schedule)), 2)
        print(f"\nnfl afc east schedule = {game_schedule}")

    def test_schedule_single_pairs_nhl_eastern_atlantic(self):
        """

        :return:
        """
        schedule_set = data.TEAMS_NHL_EASTERN_ATLANTIC
        game_schedule = generate_schedule_single_pairs(schedule_set)
        self.assertEqual(4, len(sorted(game_schedule)))
        print(f"\nnhl eastern atlantic schedule = {game_schedule}")


if __name__ == '__main__':
    import sys

    # noinspection PyTypeChecker
    sys.exit(unittest.main())
