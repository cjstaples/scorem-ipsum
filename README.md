# scoremipsum
SCOREMIPSUM

-- Generate sports scores and statistics for use in data testing or as content filler

# features (planned for initial review / v0.5 and release / v1.0)
  * get list of supported sports (anyball, hockey, football)
    - scoremipsum.sports()
  * produce semi-realistic random scores appropriate to sport
  * adjust initial generation to reduce incidence of ties
  * produce game results object in JSON format
  * display available commands
    - scoremipsum.commands()
 
- get sample set of scores with minimal input - scoremipsum.game()
- get basic set of scores for any supported sport with a minimal call - e.g. scoremipsum.game(gametype='sport_name')
 
# features (planned for release / v1.1)
- support input parameter for sport
- support input parameter for number of games
 
# features (planned for release / v1.2)
- run module via entry point
- support command line options for gametype, number of games, schedule set
- support schedule home / away values
