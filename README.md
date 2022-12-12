# 3D-Tic-Tac-Toe-game
Text based tic tac toe game written in python. The code consists of game play and testing.

The repository consists of 4 .py files:
1. game.py
2. play_mode.py
3. tester.py
4. problem_generator.py

*In the next sections I will explain the purpose of each file and how to use it.*

### 1. game.py
This file is the implementation of the 3D-Tic-Tac-Toe-game. \
You will have to have this file in the same directory as the other files in order to run them. \
You can use either IDE or the command line.


### 2. play_mode.py
The play mode file is a runnable file. Its sole purpose is to make it possible for 2 players to play together. \
Each player has its turn, and a specific move is 'x y z' so that x,y,z represent a coordinate between 0 and 3.

*Example*

<img src="https://user-images.githubusercontent.com/92261832/206935263-5a23ec54-9465-402d-a758-b05becaf535a.png" width="500" height="auto">

Requires: game.py


### 3. tester.py
Also a runnable file. Its purpose is to test different play sequences.  \
Writing one long play sequence so that at the end of reading this sequence the match will be rolled (Winner / Tie / Still on)

*Example*

<img src="https://user-images.githubusercontent.com/92261832/206936069-23f9f436-8152-4453-9767-26013c7672f8.png" width="800" height="auto">

Requires: game.py


### 4. problem_generator.py
Runnable file. We use this file to create different play sequences.  \
This file creates a random sequence of moves until the game is over. Once the game is over, it writes the sequence to the text file. \
We can choose to find more than one play sequence by changing the value of `problems_to_generate` at the start of the file.

*Example of input.txt*

<img src="https://user-images.githubusercontent.com/92261832/206936703-bcb2a47f-7f44-4f84-ac8b-d31355e637f6.png" width="800" height="auto">


We will also save the results (Winenr / Tie) and the winning sequence.

*Example of results.txt*

<img src="https://user-images.githubusercontent.com/92261832/206936713-db216423-0cdf-456a-9369-eba5a45286c3.png" width="800" height="auto">

Once we have the input file, we can use it on the tester. 

Requires: game.py, random.py Library.

There are a few more details to this code but those are the main points.
## That's it! Have fun playing (:




