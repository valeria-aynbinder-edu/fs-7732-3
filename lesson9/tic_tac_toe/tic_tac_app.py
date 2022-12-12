# i will run this file

import validators
from lesson9.tic_tac_toe.board import board_logic, board_prints




if __name__ == '__main__':
    print("Welcome to Ticx Tac Toe")

    size = input("Boadr size: ")
    validators.validate_size(size)

    board_logic.is_winner()

    #
    #
    #
    board_prints.print_current_board()