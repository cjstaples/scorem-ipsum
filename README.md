[![Pytests](
https://github.com/cjstaples/scorem-ipsum/actions/workflows/python-app.yml/badge.svg?branch=master
)](https://github.com/cjstaples/scorem-ipsum/actions/workflows/python-app.yml)
# scoremipsum
    SCOREMIPSUM

    Generate sports-like scores and statistics 
    for use in data testing or as content filler. 

# -------------------------------------------------------------------
# DISCLAIMER
    Versions of package [ scoremipsum ] below v1.0.0 are considered pre-release.
    Features are subject to revision and may change or be removed entirely.

    This code is not intended for any production use.
    May contain bugs or unexpected behavior - use at your own risk. 

    Please send feedback or code issues to Chuck Staples [ cjstaples@gmail.com ]
# -------------------------------------------------------------------

# features (planned for initial review / v0.0.x and release / v1.0)
    * display help
        - ops.help()
    * display available commands
        - ops.commands()
    * get list of supported sports (anyball, baseball, basketball, hockey, football)
        - ops.sports()
    * generate pseudo-random scores that are generally realistic for sport
        - adjust generated scores to reduce incidence of ties
    * produce game results object in JSON format 
    * get sample set of scores with minimal input
        - ops.game()
    * get basic set of scores for any supported sport with a minimal call
        - ops.game(gametype='football')
        - ops.game(gametype='hockey')

# features (planned for release / v1.1)
    . support input parameter for sport
    . support input parameter for number of games
 
# features (planned for release / v1.2)
    . run module via entry point
    . support command line options for gametype, number of games, schedule set
    . support schedule home / away values
