"""
   scoremipsum sanity test / main
"""
import sys
from scoremipsum import game, data, scoremipsum
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
    scoremipsum.sportsball()

    commands = scoremipsum.commands()
    print(f"== {commands = }")
    print("-"*80)

    sports = scoremipsum.sports()
    print(f"== {sports = }")
    print("-"*80)

    # get_supported_sports() direct
    # supported_sports = util.get_supported_sports()
    # print(f"== {supported_sports = }")
    # print("-"*80)

    #   display some scores!
    #
    sample = scoremipsum.game()
    print(f"== {sample = }")
    print("-"*80)


    #   display some football scores!
    #
    sample = scoremipsum.game(gametype="football")
    print(f"== {sample = }")
    print("-"*80)


    #   display some hockey scores!
    #
    sample = scoremipsum.game(gametype="hockey")
    print(f"== {sample = }")
    print("-"*80)


    #   display some more interesting scores!
    #
    teamlist = data.TEAMS_DEFAULT
    schedule = game.generate_schedule_single_pairs(teamlist)
    game_generation_results = game.generate_games_from_schedule(schedule, gametype='anyball')
    game_results_json = convert_game_result_to_json(game_generation_results, gametype='anyball')

    print(f"== {game_results_json}")
    print("-"*80)

    teamlist = data.TEAMS_NFL_AFC_EAST
    schedule = game.generate_schedule_single_pairs(teamlist)
    game_generation_results = game.generate_games_from_schedule(schedule, gametype='football')
    game_results_json = convert_game_result_to_json(game_generation_results, gametype='football')

    print(f"== {game_results_json}")
    print("-"*80)

    teamlist = data.TEAMS_NHL_EASTERN_ATLANTIC
    schedule = game.generate_schedule_single_pairs(teamlist)
    game_generation_results = game.generate_games_from_schedule(schedule, gametype='hockey')
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
