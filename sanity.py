"""
   scoremipsum sanity test / main
"""
import sys
import pprint
from scoremipsum import data, ops
from scoremipsum.schedule import generate_schedule_single_pairs, generate_games_from_schedule
from scoremipsum.util.conversion import convert_game_result_to_json


def main():
    """
    scoremipsum sanity main
    """
    print("="*80)
    print('(scoremipsum sanity) :: main ::')
    print("-"*80)

    #   display the supported sports list
    #
    ops.sportsball()

    ops.help()

    commands = ops.commands()
    print(f"== {commands=}")
    print("-"*80)

    sports = ops.sports()
    print(f"== {sports=}")
    print("-"*80)

    #   display some scores!
    #
    sample = ops.game()
    pprint.pprint(sample)
    print("-"*80)

    #   display some baseball scores!
    #
    sample = ops.game(gametype="baseball")
    pprint.pprint(sample)
    print("-"*80)

    #   display some baseball scores!
    #
    sample = ops.game(gametype="basketball")
    pprint.pprint(sample)
    print("-"*80)

    #   display some football scores!
    #
    sample = ops.game(gametype="football")
    pprint.pprint(sample)
    print("-"*80)

    #   display some hockey scores!
    #
    sample = ops.game(gametype="hockey")
    pprint.pprint(sample)
    print("-"*80)

    #   -----------------------------------------------------------------------
    #   display some more interesting scores!
    #
    teamlist = data.TEAMS_DEFAULT
    schedule = generate_schedule_single_pairs(teamlist)
    game_generation_results = generate_games_from_schedule(schedule, gametype='anyball')
    game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')

    print(f"== {game_results_json}")
    print("-"*80)

    teamlist = data.TEAMS_MLB_AL_EAST
    schedule = generate_schedule_single_pairs(teamlist)
    game_generation_results = generate_games_from_schedule(schedule, gametype='baseball')
    game_results_json = convert_game_result_to_json(game_generation_results, gametype='baseball')

    print(f"== {game_results_json}")
    print("-"*80)

    teamlist = data.TEAMS_NBA_EASTERN_CENTRAL
    schedule = generate_schedule_single_pairs(teamlist)
    game_generation_results = generate_games_from_schedule(schedule, gametype='basketball')
    game_results_json = convert_game_result_to_json(game_generation_results, gametype='basketball')

    print(f"== {game_results_json}")
    print("-"*80)

    teamlist = data.TEAMS_NFL_AFC_EAST
    schedule = generate_schedule_single_pairs(teamlist)
    game_generation_results = generate_games_from_schedule(schedule, gametype='football')
    game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')

    print(f"== {game_results_json}")
    print("-"*80)

    teamlist = data.TEAMS_NHL_EASTERN_ATLANTIC
    schedule = generate_schedule_single_pairs(teamlist)
    game_generation_results = generate_games_from_schedule(schedule, gametype='hockey')
    game_results_json = convert_game_result_to_json(game_generation_results, gametype='hockey')

    print(f"== {game_results_json}")
    print("-"*80)

    #   display a result_score like a chyron!
    #

    #   display some scores like newspaper results!
    #

    print('(scoremipsum sanity) :: end ::')
    print("="*80)
    return 0


# ----------------------------------------
if __name__ == '__main__':
    main()
    sys.exit(0)
