#
#   SCOREM
#
"""
conversion
----------

conversion utils for the `scoremipsum` module.
"""
import json


def convert_game_result_to_json(result_score, gametype=None):
    result_score_dict = []
    result_score = result_score
    gametype = gametype

    keys = ["gametype", "team_away", "score_away", "team_home", "score_home"]

    for res in result_score:
        gametype = gametype
        team_away, score_away = res[0][0], res[0][1]
        team_home, score_home = res[1][0], res[1][1]
        values = gametype, team_away, score_away, team_home, score_home
        game_dict = dict(zip(keys, values))
        result_score_dict.append(game_dict)

    # json_data = result_score_dict
    result_score_json = json.dumps(result_score_dict, indent=4)
    result_score_list = json.loads(result_score_json)
    print(f":::: conversion :: {result_score_list = }")

    return result_score_json
