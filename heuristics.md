Starting with all scorers as AB_Improved:

```
                        *************************                         
                             Playing Matches                              
                        *************************                         

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      10  |   0    10  |   0    10  |   0    10  |   0  
    2       MM_Open      7  |   3     7  |   3     7  |   3     9  |   1  
    3      MM_Center     7  |   3     9  |   1    10  |   0     8  |   2  
    4     MM_Improved    7  |   3     7  |   3     8  |   2     6  |   4  
    5       AB_Open      5  |   5     5  |   5     6  |   4     4  |   6  
    6      AB_Center     6  |   4     5  |   5     6  |   4     6  |   4  
    7     AB_Improved    6  |   4     4  |   6     5  |   5     4  |   6  
--------------------------------------------------------------------------
Win Rate:      68.6%        67.1%        74.3%        67.1%    

optional: insert game_agent_playground.py here

- ab_custom: opponents_toes based on improved_score
- ab_custom2: 2 forecasts in the endgame, else improved_score
- ab_custom3: mix begin/middle/end game

best ab_custom:
Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                       Won | Lost   Won | Lost   Won | Lost   Won | Lost
   1       Random      95  |   5    93  |   7    95  |   5    94  |   6
   2       MM_Open     78  |  22    69  |  31    71  |  29    76  |  24
   3      MM_Center    83  |  17    92  |   8    81  |  19    85  |  15
   4     MM_Improved   76  |  24    73  |  27    68  |  32    69  |  31
   5       AB_Open     53  |  47    54  |  46    50  |  50    52  |  48
   6      AB_Center    48  |  52    59  |  41    51  |  49    51  |  49
   7     AB_Improved   43  |  57    49  |  51    41  |  59    43  |  57
--------------------------------------------------------------------------
          Win Rate:      68.0%        69.9%        65.3%        67.1%

but usually on similar level as ab improved:
Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                       Won | Lost   Won | Lost   Won | Lost   Won | Lost
   1       Random      92  |   8    96  |   4    94  |   6    91  |   9
   2       MM_Open     80  |  20    77  |  23    71  |  29    69  |  31
   3      MM_Center    91  |   9    84  |  16    92  |   8    88  |  12
   4     MM_Improved   74  |  26    71  |  29    68  |  32    63  |  37
   5       AB_Open     54  |  46    54  |  46    49  |  51    45  |  55
   6      AB_Center    59  |  41    57  |  43    51  |  49    46  |  54
   7     AB_Improved   49  |  51    53  |  47    44  |  56    42  |  58
--------------------------------------------------------------------------
          Win Rate:      71.3%        70.3%        67.0%        63.4%

     1       Random      91  |   9    88  |  12    96  |   4    92  |   8
     2       MM_Open     75  |  25    73  |  27    81  |  19    66  |  34
     3      MM_Center    83  |  17    86  |  14    87  |  13    89  |  11
     4     MM_Improved   83  |  17    72  |  28    62  |  38    66  |  34
     5       AB_Open     59  |  41    53  |  47    44  |  56    44  |  56
     6      AB_Center    60  |  40    58  |  42    55  |  45    53  |  47
     7     AB_Improved   46  |  54    45  |  55    48  |  52    43  |  57
 --------------------------------------------------------------------------
            Win Rate:      71.0%        67.9%        67.6%        64.7%

```
