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


def is_valid_json(json_string):
    try:
        result = json.loads(json_string)
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
    is_supported_anyball = None
    is_config_enabled_anyball = True  # future:   local config setting
    is_present_generate_score_anyball = hasattr(scoremipsum.game, "generate_score_anyball")
    is_present_get_score_anyball = hasattr(scoremipsum.game.GameGeneration, "get_score_anyball")

    if (is_config_enabled_anyball
            and is_present_get_score_anyball and is_present_generate_score_anyball):
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
    is_supported_baseball = None
    is_config_enabled_baseball = True  # future:   local config setting
    is_present_generate_score_baseball = hasattr(scoremipsum.game, "generate_score_baseball")
    is_present_get_score_baseball = hasattr(scoremipsum.game.GameGeneration, "get_score_baseball")

    if (is_config_enabled_baseball
            and is_present_get_score_baseball and is_present_generate_score_baseball):
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
    is_supported_basketball = None
    is_config_enabled_basketball = True  # future:   local config setting
    is_present_generate_score_basketball = hasattr(scoremipsum.game, "generate_score_basketball")
    is_present_get_score_basketball = hasattr(scoremipsum.game.GameGeneration, "get_score_basketball")

    if (is_config_enabled_basketball
            and is_present_get_score_basketball and is_present_generate_score_basketball):
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
    is_supported_football = None
    is_config_enabled_football = True  # future:   local config setting
    is_present_generate_score_football = hasattr(scoremipsum.game, "generate_score_football")
    is_present_get_score_football = hasattr(scoremipsum.game.GameGeneration, "get_score_football")

    if (is_config_enabled_football
            and is_present_get_score_football and is_present_generate_score_football):
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
    is_supported_hockey = None
    is_config_enabled_hockey = True  # future:   local config setting
    is_present_generate_score_hockey = hasattr(scoremipsum.game, "generate_score_hockey")
    is_present_get_score_hockey = hasattr(scoremipsum.game.GameGeneration, "get_score_hockey")

    if (is_config_enabled_hockey
            and is_present_get_score_hockey and is_present_generate_score_hockey):
        is_supported_hockey = True
    else:
        is_supported_hockey = False
    return is_supported_hockey


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
