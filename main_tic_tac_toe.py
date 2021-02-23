#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tick tack to fot the comandline
"""

import random as rm

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print_board = lambda: print(f'\n  1 2 3\n1 {board[0][0]}|{board[0][1]}|{board[0][2]}\n  -----\n2 {board[1][0]}|{board[1][1]}|{board[1][2]}\n  -----\n3 {board[2][0]}|{board[2][1]}|{board[2][2]}\n')

def user_make_move() -> None:
        try:
                x, y = tuple(map(int, input('X and Y: ').split()))
                if 1 <= x <= 3 and 1<= y <= 3:
                        if board[y-1][x-1] != ' ': raise Exception('already taken')
                        board[y-1][x-1] = 'X'

                else:
                        raise Exception('out of range...')

        except Exception as err:
                print(f'Error: {err}')
                user_make_move()

def not_user_make_move() -> str:
        # if the bot can winn in one move
        def winn_with_the_next_move():
                # check row's
                for row_index in range(len(board)):
                        if board[row_index].count('O') == 2 and board[row_index].count(' ') == 1:
                                index_of_empty_field = board[row_index].index(' ')
                                print(f'R Computer wonn with {index_of_empty_field, row_index}')
                                board[index_of_empty_field][row_index] = 'O'
                                return 1
                # check cols
                for index_col in range(len(board)):
                        col = [board[0][index_col], board[1][index_col], board[2][index_col]]
                        if col.count('O') == 2 and col.count(' ') == 1:
                                index_of_empty_field = col.index(' ')
                                print(f'C Computer wonn with {index_col, index_of_empty_field}')
                                board[index_of_empty_field][index_col] = 'O'
                                return 1

                # check diagonale
                d_1 = [board[0][0], board[1][1], board[2][2]]
                if d_1.count('O') == 2 and d_1.count(' ') == 1:
                        free_field = d_1.index(' ')
                        print('D Computer wonn')
                        if free_field == 0:
                                board[0][0] = 'O'
                        elif free_field == 1:
                                board[1][1] = 'O'
                        else:
                                board[2][2] = 'O'
                        return 1

                d_2 = [board[2][0], board[1][1], board[0][2]]
                if d_2.count('O') == 2 and d_2.count(' ') == 1:
                        free_field = d_2.index(' ')
                        print('D Computer wonn')
                        if free_field == 0:
                                board[2][0] = 'O'
                        elif free_field == 1:
                                board[1][1] = 'O'
                        else:
                                board[0][2] = 'O'
                        return 1


        if  True not in [' ' in board[index] for index in range(len(board))]:
                print('GAME OVER')
                return 'exit'
        else:
                if winn_with_the_next_move() == 1:
                        return

                x = rm.randint(1, 3)
                y = rm.randint(1, 3)

                if board[y-1][x-1] == 'X' or board[y-1][x-1] == 'O':
                        not_user_make_move()
                else:
                        print(f"Computer's move: {x, y}")
                        board[y-1][x-1] = 'O'
                        return 'ok'

def check_for_winner() -> bool:
        l_of_x = ['X', 'X', 'X']
        l_of_o = ['O', 'O', 'O']

        for row in board:
                if row == l_of_o or row == l_of_x:
                        return True

        for index_col in range(len(board)):
                board_col = [board[0][index_col], board[1][index_col], board[2][index_col]]
                if board_col == l_of_o or board_col == l_of_x:
                        return True

        d_1 = [board[0][0], board[1][1], board[2][2]]
        if d_1 == l_of_o or d_1 == l_of_x: return True

        d_2 = [board[2][0], board[1][1], board[0][2]]
        if d_2 == l_of_o or d_2 == l_of_x: return True

        return False

def main() -> None:
        game_over = False
        while not game_over:
                print_board()

                user_make_move()

                if check_for_winner():
                        game_over = True
                        print('You won!')
                        break

                print_board()

                if not_user_make_move() == 'exit':
                        game_over = True
                        print('The Computer won!')
                        break

                if check_for_winner():
                        game_over = True
                        break
        print_board()


if __name__ == '__main__':
        main()

