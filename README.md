# guiild js
## Level 1: Bowling
## Bowling rules
1) The goal is to knock down all 10 **pins**
2) Each **frame** consists of throwing the ball twice to knock down all the pins
3) There are 10 **frames** in a game
4) If you knock down all the pins with the first ball, it is called a **strike**
5) If you knock down all the pins with the second ball, it is called a **spare**
6) Scoring is based on **how many pins you knock down**. However, if you bowl a **spare**, you get to add the pins in your next ball to that frame. For **strikes**, it is the same with the next two balls.
7) If you do a **strike** or a **spare** in the last frame, you can throw 1 more ball for a spare and 2 for a strike to calculate your bonus. The balls thrown after the 10th frame **only count for the bonus**.

The maximum score is 300 if you do 12 strike in a row (the 2 last ones only count for the strike bonus).
## Your task
In *bowling.py*, implement the methods:
1) `roll`: that takes the number of pins down as an int and returns nothing.
2) `score`: that takes no input and returns an int representing the player score.

Fork the project on Github and submit a merge request when you are ready.

Python 3.6 will be used for testing.

## Test
Unit test can be found in *bowling.test.py*. If you think some are missing, you can add yours.
`python bowling.test.py`