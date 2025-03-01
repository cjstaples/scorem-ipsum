#
#   SCOREM
#
"""
team
----------

team utils for the `scoremipsum` module.
"""
from scoremipsum import data


def get_default_teamlist_from_gametype(gametype=None):

    if not gametype:
        teamlist = data.TEAMS_DEFAULT
    elif gametype == "baseball":
        teamlist = data.TEAMS_MLB_DEFAULT
    elif gametype == "basketball":
        teamlist = data.TEAMS_NBA_DEFAULT
    elif gametype == "football":
        teamlist = data.TEAMS_NFL_DEFAULT
    elif gametype == "hockey":
        teamlist = data.TEAMS_NHL_DEFAULT
    else:
        # anyball, or any unhandled gametype
        teamlist = data.TEAMS_DEFAULT

    return teamlist

