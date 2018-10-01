To play the single-player game of Memory, go to the directory (memory-game), and call the program in terminal as follows:

$ python memory.py

I chose to represent the game as a class, and I broke down the steps of the game into separate methods within the class.

I used 2-dimensional arrays (lists of lists) to represent the cards. One array is for the player's view of the cards, with dots for covered cards and blank spaces for cards that have been already matched and thus taken away. Another array, hidden from the player, represents what the cards actually are. This is straightforward and does not use unnecessary memory (no pun intended).

I decided to have cards differentiated by uppercase letters since this facilitates an easy-to-understand game. The maximum number of cards, then, is 26 (letters in the alphabet)*2=52, which is the number of cards in a standard deck. The board has length 6 as a balance between having too many or too few rows depending on the number of cards the player wants to use. 

There are many lines of whitespace between each turn to discourage the player from looking at the cards that were "flipped over" during previous turns. Also, I kept track of the number of turns as a metric to guide skill improvement across multiple games.

I considered various edge cases, like invalid inputs, and wrote meaningful error messages that are printed to terminal for the player. Since the player would not want to restart the entire game due to one single invalid input, I chose to continue the game rather than exiting in these cases.

I used Python 3 because it is a free, widely-accessible, and well-documented object-oriented programming language that has a helpful built-in standard library.