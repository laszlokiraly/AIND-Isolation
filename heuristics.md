# Heuristics Analysis

## Statistics on win/play rates
My first impression is that the range of the win rate for a small number of games is surprisingly large. It ranges from 67.1% to 74.3%, that's a 7.2% difference.
For quick experimenting and to get a feeling for the heuristics it's ok.
But a lot more games need to be played to get more consistent numbers on win/lose rates.

## Forecasting Scorers
When i started playing with scorers, i thought that, to find potential partitions on the board for solving the horizon effect, i would like to know more than just legal moves of the players and opponent of the current pry. So i started to forecast one and two rounds and started counting and summing the legal moves and used it for scoring. In small tests, with little games, usually they did not score much better, but worse than the improved scorer.
I had the feeling that forecasting moves in the scorer was a bad idea, because the score should have a static overhead to be able to make a better assumption about the total cost of the players overhead including AB. Another reason i stopped using expensive forecasts in the scorer was that the forecasting is already part of AB, so the scorer would just circumvent AB pruning, rendering it being effectively slower.

## Scorer's Knowledge of the Game
But what does the scorer know about the game and it's state? It knows the dimensions of the board, the position of the players, it knows how many rounds have been played and it knows how many blank spaces there are left.
The legal moves of the players can be evaluated and counted. The scorer can also find out if it reached a terminal state by asking the board if there is a winner in the current pry.

## Progress of the Game
Given these informations, i defined a progress from the number of spaces and the blank spaces of the board. This would help the scorer to differentiate between start, middle and end game.
I did some statistics on the average of the left blanks at every end of a game and found it out to be around 18.5 for a 7x7 board, so a game usually ends at a progress of roughly 0.6.
I defined the phases of the game:
- start phase for a progress less than 0.25
- middle phase for a progress less than 0.5
- end phase: rest

## Tread on opponent's toe
I made a helper function to find out if the player is on a space from which the opponent is reachable within one move. I use it to multiply the improved score.
This special move, "tread on the opponent's toe" removes one of the legal moves of the opponent, which i think can be of an advantage (of course there are special cases when it's not, which are hard to find because of the horizon effect).

The scorers:

1 calculates current progress
    - start: uses improved score as long as progress is less than 0.25
    - middle: tries to close in on the opponent
    - end: tries to step on the toe of the opponent
2 always tries to step on the toe of the opponent
3 calculates current progress
    - start: tries to stay at the center of the board
    - middle: tries to close in on the opponent
    - end: tries to step on the toe of the opponent

## Results:
```

```

## Analysis of Custom Score 1

- Random
- Minimax Open
- Minimax Center
- Minimax Improved
- Alpha Beta Open
- Alpha Beta Center
- Alpha Beta Improved

## Improvements, ideas
Some thoughts on improvements, thinking outside of the scorer.
- Partitioning:
    - for all free spaces check if the space are unreachable (i.e. no legal moves from that space), this number can be an indicator for when the end game is about to start
- More Variations and combinations of improved score, moving around (staying in the center or moving in circles?), stepping on toes, visit quadrants with potentially more blank spaces,...
