#
#   SCOREM
#
"""
support
----------

game support utils for the `scoremipsum` module.
"""
import json

import scoremipsum
import scoremipsum.generation


def is_valid_json(json_string):
    try:
        result = json.loads(json_string)
        assert result is not None
        return True
    except json.JSONDecodeError:
        return False


def check_support_anyball():
    """
    check for functions necessary for anyball data
    or turn off via override flag

    definition:  supported if we have config enabled, get_score function, generate_score function
    :return:
    """
    is_config_enabled_anyball = True  # future:   local config setting
    is_present_score_generate_anyball = hasattr(scoremipsum.score, "generate_score_anyball")
    is_present_score_compute_anyball = hasattr(scoremipsum.score, "compute_score_anyball")

    if (is_config_enabled_anyball
            and is_present_score_compute_anyball and is_present_score_generate_anyball):
        is_supported_anyball = True
    else:
        is_supported_anyball = False
    return is_supported_anyball


def check_support_baseball():
    """
    check for functions necessary for baseball data
    or turn off via override flag

    definition:  supported if we have config enabled, get_score function, generate_score function
    :return:
    """
    is_config_enabled_baseball = True  # future:   local config setting
    is_present_score_generate_baseball = hasattr(scoremipsum.score, "generate_score_baseball")
    is_present_score_compute_baseball = hasattr(scoremipsum.score, "compute_score_baseball")

    if (is_config_enabled_baseball
            and is_present_score_compute_baseball and is_present_score_generate_baseball):
        is_supported_baseball = True
    else:
        is_supported_baseball = False
    return is_supported_baseball


def check_support_basketball():
    """
    check for functions necessary for basketball data
    or turn off via override flag

    definition:  supported if we have config enabled, get_score function, generate_score function
    :return:
    """
    is_config_enabled_basketball = True  # future:   local config setting
    is_present_score_generate_basketball = hasattr(scoremipsum.score, "generate_score_basketball")
    is_present_score_compute_basketball = hasattr(scoremipsum.score, "compute_score_basketball")

    if (is_config_enabled_basketball
            and is_present_score_compute_basketball and is_present_score_generate_basketball):
        is_supported_basketball = True
    else:
        is_supported_basketball = False
    return is_supported_basketball


def check_support_football():
    """
    check for functions necessary for football data
    or turn off via override flag

    definition:  supported if we have config enabled, get_score function, generate_score function
    :return:
    """
    is_config_enabled_football = True  # future:   local config setting
    is_present_score_generate_football = hasattr(scoremipsum.score, "generate_score_football")
    is_present_score_compute_football = hasattr(scoremipsum.score, "compute_score_football")

    if (is_config_enabled_football
            and is_present_score_compute_football and is_present_score_generate_football):
        is_supported_football = True
    else:
        is_supported_football = False
    return is_supported_football


def check_support_hockey():
    """
    check for functions necessary for hockey data
    or turn off via override flag

    definition:  supported if we have config enabled, get_score function, generate_score function
    :return:
    """
    is_config_enabled_hockey = True  # future:   local config setting
    is_present_score_generate_hockey = hasattr(scoremipsum.score, "generate_score_hockey")
    is_present_score_compute_hockey = hasattr(scoremipsum.score, "compute_score_hockey")

    if (is_config_enabled_hockey
            and is_present_score_compute_hockey and is_present_score_generate_hockey):
        is_supported_hockey = True
    else:
        is_supported_hockey = False
    return is_supported_hockey


def get_command_list():
    # DYNAMIC determination, now returns convert_game_result_to_json() method - mess with this later
    # method_list = [func for func in dir(scoremipsum.scoremipsum) if
    #                callable(getattr(scoremipsum.scoremipsum, func)) and not func.startswith(
    #                    "_") and not func.startswith("get_")]
    # for now, maintain the command list manually
    override_command_list_getter = True
    # command_list = ['foo']
    # command_list = [func for func in dir(scoremipsum.ops) if
    #                callable(getattr(scoremipsum.ops, func)) and not func.startswith(
    #                    "_") and not func.startswith("get_")]
    command_list = [func for func in dir(scoremipsum.ops)
                    if callable(getattr(scoremipsum.ops, func)) and not func.startswith("_")]


    if command_list == [] or override_command_list_getter is True:
        command_list = ['commands', 'game', 'help', 'sports', 'sportsball']

    return command_list


def get_help_content() -> str:
    """
    help text content
    :return:
    """
    help_content = "" \
        + "== help() \n" \
        + "-" * 9 + "\n" \
        + "== Use the following commands to get started quickly: \n" \
        + "== \n" \
        + "==       ops.sportsball()\n" \
        + "==           Displays 'Sportsball' as a sanity check\n" \
        + "== \n" \
        + "==       ops.help()\n" \
        + "==           Displays this content\n" \
        + "== \n" \
        + "==       ops.commands()\n" \
        + "==           Displays available commands\n" \
        + "==           e.g. commands=['commands', 'game', 'help', 'sports', 'sportsball']\n" \
        + "== \n" \
        + "==       ops.sports()\n" \
        + "==           Displays supported sports\n" \
        + "==           e.g. sports=['anyball', 'baseball', 'basketball', 'football', 'hockey']\n" \
        + "== \n" \
        + "==       ops.game()\n" \
        + "==           Generates game scores for default sport, using default generic team list\n" \
        + "==           Returns JSON object\n" \
        + "==           Syntax:\n" \
        + "==               results = ops.game()\n" \
        + "== \n" \
        + "==       ops.game(gametype='<gametype>')\n" \
        + "==           Generates game scores for selected sport, using default team list from that sport\n" \
        + "==           Returns JSON object\n" \
        + "==           Syntax:\n" \
        + "==               results = ops.game(gametype='hockey')\n" \
        + "== \n" \
        + "-" * 80

    return help_content


def get_supported_sports():
    """
    list all sports for which the associated support check passes
    :return:
    """
    supported_sports = []

    if check_support_anyball():
        supported_sports.append('anyball')

    if check_support_baseball():
        supported_sports.append('baseball')

    if check_support_basketball():
        supported_sports.append('basketball')

    if check_support_football():
        supported_sports.append('football')

    if check_support_hockey():
        supported_sports.append('hockey')

    return supported_sports
