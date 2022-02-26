import random as rand
from typing import Tuple


def input_int(prompt: str, min_val: int = 1, max_val: int = 5) -> int:
    """Get an integer from the user"""
    while True:
        try:
            user_input = int(input(prompt))
            if min_val <= user_input <= max_val:
                return user_input
            print("Value not within range. Try again!")
        except ValueError:
            print("Invalid integer input. Try again!")


class BattleshipGame:
    """This is a battleship game to be played in the console"""
    BOARD_BLANK = "O"
    BOARD_MISS = "X"
    BOARD_HIT = "S"

    def __init__(self, max_players: int, board_width: int, board_height: int) -> None:
        """Initialize the BattleshipGame Class"""
        self.max_players = max_players
        self.board_width = board_width
        self.board_height = board_height
        self.num_players = input_int("Please enter how many players are going to play:", 1, max_players)
        self.current_player = 1
        self.board = [[self.BOARD_BLANK] * board_width for _i in range(board_height)]
        self.ship_row, self.ship_col = rand.randint(0, board_width - 1), rand.randint(0, board_height - 1)

    def get_player_guess(self) -> Tuple[int, int]:
        """Get the guess row and column from the player"""
        while True:
            guess_row = input_int(f"Player {self.current_player}, guess row: ", 1, self.board_width) - 1
            guess_col = input_int(f"Player {self.current_player}, guess col: ", 1, self.board_height) - 1

            if self.board[guess_row][guess_col] == self.BOARD_BLANK:
                return guess_row, guess_col

            print("You've already guessed on that row! Try again.")

    def play(self) -> None:
        """main game loop"""
        while True:
            [print(*col) for col in self.board]
            guess_row, guess_col = self.get_player_guess()
            if (guess_row, guess_col) == (self.ship_row, self.ship_col):
                self.board[self.ship_row][self.ship_col] = self.BOARD_HIT
                print(f"Congratulations! Player {self.current_player} sank the ship!")
                [print(*col) for col in self.board]
                return
            self.board[guess_row][guess_col] = self.BOARD_MISS
            self.current_player = (self.current_player % self.num_players) + 1


if __name__ == "__main__":
    BattleshipGame(2, 5, 5).play()
