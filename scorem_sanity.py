"""
   scorem sanity test / main
"""
import sys
from scorem import game, data, util, scorem
from util.conversion import convert_game_result_to_json


def main():
    """
    scorem sanity main
    """
    print("="*80)
    print('(scorem sanity) :: main ::')
    print("-"*80)

    #   display the supported sports list
    #
    scorem.sportsball()

    commands = scorem.commands()
    print(f"== {commands = }")
    print("-"*80)

    sports = scorem.sports()
    print(f"== {sports = }")
    print("-"*80)

    # get_supported_sports() direct
    # supported_sports = util.get_supported_sports()
    # print(f"== {supported_sports = }")
    # print("-"*80)

    #   display some scores!
    #
    sample = scorem.game()
    print(f"== {sample = }")
    print("-"*80)


    #   display some football scores!
    #
    sample = scorem.game(gametype="football")
    print(f"== {sample = }")
    print("-"*80)


    #   display some hockey scores!
    #
    sample = scorem.game(gametype="hockey")
    print(f"== {sample = }")
    print("-"*80)


    #   display some more interesting scores!
    #
    teamlist = data.TEAMS_DEFAULT
    schedule = game.generate_schedule_single_pairs(teamlist)
    game_generation_results = game.generate_games_from_schedule(schedule, gametype='football')
    game_results_json = convert_game_result_to_json(game_generation_results)

    print(f"== {game_results_json}")
    print("-"*80)

    teamlist = data.TEAMS_DEFAULT
    schedule = game.generate_schedule_single_pairs(teamlist)
    game_generation_results = game.generate_games_from_schedule(schedule, gametype='hockey')
    game_results_json = convert_game_result_to_json(game_generation_results)

    print(f"== {game_results_json}")
    print("-"*80)

    #   display a result_score like a chyron!
    #

    #   display some scores like newspaper results!
    #

    print('(scorem sanity) :: end ::')
    print("="*80)
    return 0


# ----------------------------------------
if __name__ == '__main__':
    main()
    sys.exit(0)
