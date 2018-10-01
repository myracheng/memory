import sys
import string
import random
from ast import literal_eval
sys.tracebacklimit = 0

class Memory(object):
    """Single-player Memory game using a set of cards 
    labeled with different uppercase letters.
    """

    def __init__(self, num_chars=26):
        """Constructs a new game of Memory.
           type: (int) -> None
        """
        self.matches_found = []
        self.unshuffled_letters = string.ascii_uppercase[0:num_chars] * 2
        self.characters = random.sample(self.unshuffled_letters,len(self.unshuffled_letters))
        self.turn_count = 1
        self.last_row_length = len(self.characters) % 6

        self.board_for_user = [['.']*6 for row in range(int(len(self.characters)/6))]
        self.board_answers = [self.characters[i*6:(i*6 + 6)] for i in range(0,int(len(self.characters)/6))]
        if len(self.characters) % 6 is not 0:
            self.board_for_user.append(['.'] * (self.last_row_length))
            self.board_answers.append(self.characters[len(self.characters) - self.last_row_length:])

    def play_turn(self):
        """Asks user to flip two cards to play a turn.
           type: (None) -> None
        """
        print('\n'*25 + 'Turn #' + str(self.turn_count))
        self.display_board(False)
        
        result = None
        while result is None:
            try:
                first_card = literal_eval(input('Enter the coordinates of the first card to check using the format (row,column): '))
                second_card = literal_eval(input('Enter the coordinates of the second card to check using the format (row,column): '))
                result = self.check(first_card[0],first_card[1],second_card[0],second_card[1])
            except (TypeError, ValueError, SyntaxError):
                print('Oops, try again. Your coordinates were not the right format.')
    
    def check(self, a, b, c, d):
        """Checks the cards at the two coordinates inputted by the user and continues the game.
           type: (int,int,int,int) -> None
        """
        if not all(i >= 0 for i in [a,b,c,d]) \
            or not all(i < len(self.board_for_user) for i in [a,c]) \
            or not all(i < len(self.board_for_user[0]) for i in [b,d]) \
            or (a == len(self.board_for_user) - 1 and b >= self.last_row_length) \
            or (c == len(self.board_for_user) - 1 and d >= self.last_row_length):
            print('Oops, try again. Your coordinate values are not on the board') 
        elif self.board_for_user[a][b] == ' ' or self.board_for_user[c][d] == ' ':
            print('Oops, try again. You already matched the card at these coordinates.')
        elif a == c and b == d:
            print('Oops, try again. You picked the same card twice.')
        else:
            self.display_board(True,a,b,c,d)
            print('The card at (' + str(a) + ',' + str(b) + ') is ' + self.board_answers[a][b] + '.')
            print('The card at (' + str(c) + ',' + str(d) + ') is ' + self.board_answers[c][d] + '.\n')

            self.turn_count += 1

            if self.board_answers[a][b] == self.board_answers[c][d]:
                print('You found a pair! \n')
                self.update(a,b,c,d)
                self.add_to_found(self.board_answers[a][b])
                if self.check_done():
                    print('Finished! Took ' + str(self.turn_count) + ' turns.')
                    return

        input("Press any key to continue.")
        self.play_turn()

    def display_board(self, show=False, a=0,b=0,c=0,d=0):
        """Prints current state of the cards, as visible to the user.
           type: (bool,int,int,int,int) -> None
        """
        if show:
            self.board_for_user[a][b] = self.board_answers[a][b]
            self.board_for_user[c][d] = self.board_answers[c][d]

        print('   ' + ' '.join(str(x) for x in range(0,len(self.board_for_user[0]))))
        count = 0
        for arr in self.board_for_user:
            print(str(count) + '  ' + ' '.join(str(cell) for cell in arr))
            count += 1
        
        self.board_for_user[a][b] = self.board_for_user[a][b]
        self.board_for_user[c][d] = self.board_for_user[c][d]

        if len(self.matches_found) > 0:
            print('Pairs found: ' + ' '.join(card + ',' + card for card in self.matches_found))
        
        if show:
            self.board_for_user[a][b] = '.'
            self.board_for_user[c][d] = '.'

    def update(self, a, b, c, d):
        """Clears cards at the given coordinates when a match has been found.
           type: (int,int,int,int) -> None
        """
        self.board_for_user[a][b] = ' '
        self.board_for_user[c][d] = ' '
    
    def add_to_found(self, found_char):
        """Adds a found match to the list of them.
           type: (char) -> None
        """
        self.matches_found.append(found_char)
    
    def check_done(self):
        """Checks if all the matches have been found.
           type: (None) -> bool
        """
        return (len(self.matches_found) == int((len(self.characters)/2)))

def main():
    """Plays a game of Memory.
       type: (None) -> None
    """
    try:
        num_count = int(input('How many pairs of cards would you like to play with? '))
    except ValueError:
        print("ValueError: Input must be a positive integer less than 27. ")
        sys.exit()
    if num_count <= 0 or num_count >= 27:
       print("Input must be a positive integer less than 27. ")
       sys.exit()

    memory = Memory(num_count)
    memory.play_turn()

if __name__ == "__main__":
    """Helper method to run the program
    """
    sys.exit(main())