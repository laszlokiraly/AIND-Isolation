# Heuristics

## Statistics on win/play rates
My first impression is that the range of the win rate for a small number of games is surprisingly large. It ranges from 67.1% to 74.3%, that's a 7.2% difference.
For quick experimenting and to get a feeling for the heuristics it's ok.
But a lot more games need to be played to get more consistent numbers on win/lose rates.

## Forecasting Scorers
When i started playing with scorers, i thought that, to find potential partitions on the board for solving the horizon effect, i would like to know more than just legal moves of the players and opponent of the current pry. So i started to forecast one and two rounds and started counting and summing the legal moves and used it for scoring. In small tests, with little games, usually they did not score much better, but worse than the improved scorer.
I had the feeling that forecasting moves in the scorer was a bad idea, because the score should have a static overhead to be able to make a better assumption about the cost of the overall forecasting of Alpha Beta.

## Scorer's Knowledge of the Game
So what does the scorer know about the game and it's state? It knows the dimensions of the board, the position of the players, it knows how many rounds have been played and it knows how many blank spaces there are left.
The legal moves of the players can be evaluated and counted. The scorer can also find out if it reached a terminal state by asking the board if there is a winner in the current pry.

## Progress of the Game
Given these informations, i defined a progress from the number of spaces and the blank spaces left on the board. This would help the scorer to differentiate between start, middle and end game.
I did some statistics on the average of the left blanks at every end of a game and found it out to be around 18.5 for a 7x7 board, so a game usually ends at a progress of roughly 0.6.
I defined the phases of the game:

- start phase for a progress less than 0.25
- middle phase for a progress less than 0.5
- end phase: rest

## Best Custom Scorer

For the best custom scorer i implemented method of choosing each phase of the game according to the progress that has been made so far. This way the scorer can implement different strategies.
In the beginning, since there is no dictionary, the improved score is used.
In the middle, the scorer rewards moves, which close in on the opponent. This might be seen as trying to put pressure on the opponent by blocking moves which are near him.
In the end game the scorer rewards moves, which take away moves from the opponent. By treading on the toes the opponent has less options for moving, which should generally be favourable.

```
Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                       Won | Lost   Won | Lost   Won | Lost   Won | Lost
   1       Random      466 |  34    467 | 33     471 |  29    459 | 41
   2       MM_Open     380 |  120   378 | 122    376 |  124   382 | 118
   3      MM_Center    428 |  72    449 | 51     430 |  70    413 | 87
   4     MM_Improved   373 |  127   350 | 150    351 |  149   368 | 132
   5       AB_Open     257 |  243   261 | 239    263 |  237   255 | 245
   6      AB_Center    282 |  218   283 | 217    269 |  231   290 | 210
   7     AB_Improved   259 |  241   233 | 267    260 |  240   237 | 263

--------------------------------------------------------------------------
          Win Rate:      69.9%        69.2%        69.1%        68.7%

Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                       Won | Lost   Won | Lost   Won | Lost   Won | Lost
   1       Random      463 |  37    466 |  34    460 |  40    468 |  32  
   2       MM_Open     366 |  134   372 |  128   358 |  142   380 |  120
   3      MM_Center    430 |  70    448 |  52    439 |  61    439 |  61  
   4     MM_Improved   376 |  124   361 |  139   349 |  151   350 |  150
   5       AB_Open     255 |  245   257 |  243   275 |  225   254 |  246
   6      AB_Center    293 |  207   277 |  223   278 |  222   282 |  218
   7     AB_Improved   239 |  261   238 |  262   245 |  255   241 |  259
--------------------------------------------------------------------------
          Win Rate:      69.2%        69.1%        68.7%        69.0%    

stalker:
Match #   Opponent    AB_Custom_2
                       Won | Lost
   1       Random      470 |  30  
   2       MM_Open     365 |  135
   3      MM_Center    435 |  65  
   4     MM_Improved   360 |  140
   5       AB_Open     258 |  242
   6      AB_Center    275 |  225
   7     AB_Improved   243 |  257
--------------------------------------------------------------------------
          Win Rate:      68.7%    

Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                       Won | Lost   Won | Lost   Won | Lost   Won | Lost
   1       Random      89  |  11    95  |   5    94  |   6    90  |  10  
   2       MM_Open     79  |  21    79  |  21    74  |  26    74  |  26  
   3      MM_Center    88  |  12    83  |  17    85  |  15    87  |  13  
   4     MM_Improved   75  |  25    68  |  32    73  |  27    73  |  27  
   5       AB_Open     51  |  49    51  |  49    52  |  48    61  |  39  
   6      AB_Center    54  |  46    62  |  38    57  |  43    57  |  43  
   7     AB_Improved   54  |  46    49  |  51    47  |  53    43  |  57  
--------------------------------------------------------------------------
          Win Rate:      70.0%        69.6%        68.9%        69.3%   

```
