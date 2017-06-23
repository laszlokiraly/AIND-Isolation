# Summary of "Mastering the game of Go with deep neural networks and tree search"

## Introduction

The paper describes the architecture of machine learning model(s), which was developed to beat world class human players in the two player game of Go.
Go is a 19x19x board game with perfect information but because of it's huge amount of possible game states (2e^170^, see^[1]^), the game cannot be won by brute force algorithms.

Traditional Go programs used the Monte Carlo Tree Search (MCTS) for heuristic search of optimal moves, which uses rollouts to evaluate the most promising paths. The MCTS is extended by a policy for predicting the opponent's move, but still performs only on an amateur level in Go.

Another possible strategy to search for the most promising move in a large tree of possible moves is to estimate the value of and select best/worst expected values for simulated moves by using the Minimax algorithm with Alpha Beta pruning. This algorithm did not work well with Go and is not used in AlphaGo.

## Architecture

The AlphaGo architecture consists of multiple Policy Networks and a Value Network mixed with the MCTS method.

The first model, a Convolutional Neural Network (CNN), allows to interpret the board like an image in order to find promising winning patterns with it's filters.
This CNN model is trained with human expert games and is used to reduce the size of the search tree. The learning is done supervised, so that the CNN can optimise it's weights towards the known outcomes. It's accuracy is 57% with an execution time of 3 milliseconds. This model is slower because of the large deep neural network that has been trained with 30 million positions.

The second network uses rollouts to predict moves with less accuracy ~24% but with a faster response time ~ microseconds.

The third policy network is based on the first model reusing it's weights. It is then trained by playing matches against itself using reinforcement learning (RL). This way the policy is geared towards winning the game and not only predicting outcomes correctly.

Finally a value network is trained, similar to RL network, this time by regression to predict a winner at a given board state. It showed that learning the expert games only lead to overfitting and memorising of positions. To overcome this problem, 30 million positions were selected and used to play games against each other, leading to an almost identical Mean Squared Error (MSE) on validation and test sets.

## Searching

For searching AlphaGo uses the fast networks to make computationally cheap rollouts and uses the costly SL network only once on the leafs of the rollouts. By adding small penalty when revisiting branches, the search is encouraged to expand other branches, so that local maxima can be avoided.

## Results

This version has easily beaten all existing Go programs.
The performance was further improved by scaling out in a distributed version of AlphaGo.

It turned out that AlphaGo was 10 years ahead of it's time, since the AI community did not expect an AI to beat the best human players that early.
It will be interesting to see if general purpose deep learning gaming architectures will be possible.

## References
[[1] Combinatorics of Go](https://tromp.github.io/go/gostate.pdf)
