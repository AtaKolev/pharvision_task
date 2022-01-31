#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:30:59 2022

@author: nasko
"""

import numpy as np
import pandas as pd
import random    

class Teacher():
    
    def play(self):
        

       possible_moves = [x for x, letter in enumerate(bd.board) if letter == ' ' and x != 0] # Create a list of possible moves
       for let in ['O','X']:
                    for i in possible_moves:
                        self.board_copy = bd.board[:]
                        self.board_copy[i] = let
                        if self.is_winner(let):
                            move = i
                            return move
       return random.choice(possible_moves)
# =============================================================================
#         move = 0
#         
#         #Check for possible winning move to take or to block opponents winning move
#         for let in ['O','X']:
#             for i in possible_moves:
#                 self.board_copy = bd.board[:]
#                 self.board_copy[i] = let
#                 if self.is_winner(let):
#                     move = i
#                     return move
#     
#     
#         #Try to take one of the corners
#         corners_open = []
#         for i in possible_moves:
#             if i in [1,3,7,9]:
#                 corners_open.append(i)
#         if len(corners_open) > 0:
#             move = corners_open[random.randrange(0, len(corners_open))]
#             return move
#         
#         #Try to take the center
#         if 5 in possible_moves:
#             move = 5
#             return move
#     
#         #Take any edge
#         edges_open = []
#         for i in possible_moves:
#             if i in [2,4,6,8]:
#                 edges_open.append(i)
#         
#         if len(edges_open) > 0:
#             move = edges_open[random.randrange(0, len(edges_open))]  
#     
#         return move
# =============================================================================
        
    
    def is_winner(self, mark):
        # Given a board and a player’s letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don’t have to type as much.
        return ((self.board_copy[7] == mark and self.board_copy[8] == mark and self.board_copy[9] == mark) or # across the top
        (self.board_copy[4] == mark and self.board_copy[5] == mark and self.board_copy[6] == mark) or # across the middmark
        (self.board_copy[1] == mark and self.board_copy[2] == mark and self.board_copy[3] == mark) or # across the self.board_copyttom
        (self.board_copy[7] == mark and self.board_copy[4] == mark and self.board_copy[1] == mark) or # down the markft side
        (self.board_copy[8] == mark and self.board_copy[5] == mark and self.board_copy[2] == mark) or # down the middmark
        (self.board_copy[9] == mark and self.board_copy[6] == mark and self.board_copy[3] == mark) or # down the right side
        (self.board_copy[7] == mark and self.board_copy[5] == mark and self.board_copy[3] == mark) or # diagonal
        (self.board_copy[9] == mark and self.board_copy[5] == mark and self.board_copy[1] == mark)) # diagonal
    
class Board():
    
    def __init__(self, board):
        self.board = board
        
    def insert_letter(self, letter, pos):
        self.board[pos] = letter
        
    def space_free(self, pos):
        return self.board[pos] == ' '
    
    def print_board(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        
    def is_winner(self, mark):
        # Given a board and a player’s letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don’t have to type as much.
        return ((self.board[7] == mark and self.board[8] == mark and self.board[9] == mark) or # across the top
        (self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) or # across the middmark
        (self.board[1] == mark and self.board[2] == mark and self.board[3] == mark) or # across the self.boardttom
        (self.board[7] == mark and self.board[4] == mark and self.board[1] == mark) or # down the markft side
        (self.board[8] == mark and self.board[5] == mark and self.board[2] == mark) or # down the middmark
        (self.board[9] == mark and self.board[6] == mark and self.board[3] == mark) or # down the right side
        (self.board[7] == mark and self.board[5] == mark and self.board[3] == mark) or # diagonal
        (self.board[9] == mark and self.board[5] == mark and self.board[1] == mark)) # diagonal
    
    def is_board_full(self):
        if self.board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
            return False
        else:
            return True
    
    def reset_board(self):
        self.board = [' ' for _ in range(10)]
    
class Player:
    
    def play(self, mark):
        
        run = True
        while run:  # Keep looping until we get a valid move
            move = input('Please select a position to place an '+str(mark)+' (1-9): ')
            try:
                move  = int(move)
                if move > 0 and move < 10:  # makes sure we type in a number between 1-9
                    if bd.space_free(move):  # check if the move we choose is valid (no other letter is there already)
                        run = False
                        return move
                    else:
                        print('This postion is already occupied!')
                else:
                    print('Please type a number within the range!')
            except:
                print('Please type a number!')

class Computer():
    
    def __init__(self):
        self.moves_outcome = pd.DataFrame(columns = ['Move '+str(x) for x in range(1,10)])
        self.moves_outcome['Outcome'] = []
        
    def play(self, num_move):
        
        
        possible_moves = [x for x, letter in enumerate(bd.board) if letter == ' ' and x != 0] # Create a list of possible moves
# =============================================================================
#         positional_probabilities = {1 : 0,
#                                     2 : 0,
#                                     3 : 0,
#                                     4 : 0,
#                                     5 : 0,
#                                     6 : 0,
#                                     7 : 0,
#                                     8 : 0,
#                                     9 : 0}
# =============================================================================
        positional_probabilities = {}
        for possible_position in possible_moves:
            positional_probabilities.update({possible_position : 0})
        
        #Check for possible winning move to take or to block opponents winning move
# =============================================================================
#         for let in ['O','X']:
#             for pos in possible_moves:
#                 board_copy = bd.board[:]
#                 board_copy[pos] = let
#                 if bd.is_winner(board_copy, let):
#                     return pos
# =============================================================================
        
        if self.moves_outcome.empty:
            return random.choice(possible_moves)

        for position in possible_moves:
            moves_outcome_curr_poss = self.moves_outcome[self.moves_outcome['Move '+str(num_move)] == position]
            if moves_outcome_curr_poss.empty:
                positional_probabilities.update({position : 0})
                continue # taking us to position + 1
            if num_move % 2 == 1:
                prob_win = moves_outcome_curr_poss['Outcome'].sum() / moves_outcome_curr_poss['Outcome'].shape[0]
# =============================================================================
#             else:
#                 prob_win = abs(moves_outcome_curr_poss['Outcome'] - 1).sum() / moves_outcome_curr_poss['Outcome'].shape[0]
# =============================================================================
            positional_probabilities.update({position : prob_win})
            
        best_prob = max(list(positional_probabilities.values()))
        best_positions = []
        for position in list(positional_probabilities.keys()):
            if positional_probabilities[position] == best_prob:
                best_positions.append(position)
        
        if len(best_positions) > 1:
            return random.choice(best_positions)
        else:
            return best_positions[0]
        
        
def main():
    #Main game loop
    print('Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.')
    global p1, p2, num_game
    bd.print_board()
    
    while True:
        play_or_learn = input("Do you want to play or let it learn? [P, L] ").upper()
        if play_or_learn[0] == 'L':
            if isinstance(p1, Player):
                p1 = Teacher()
            else:
                p2 = Teacher()
            break
        elif play_or_learn[0] == 'P':
            if isinstance(p1, Teacher):
                p1 = Player()
            else:
                p2 = Player()
            break
        else:
            print("Input should be P(lay) or L(earn)!")
    
    choice = ''
    while not choice:
        player1_mark = input("Choose a mark for player1 to play with (X or O)?").upper()
        if (player1_mark == 'O') or (player1_mark == 'X'):
            if player1_mark == 'O':
                player2_mark = 'X'
            else:
                player2_mark = 'O'
            choice = True
            print('Player1 mark is: ', player1_mark)
            print('Player2 mark is: ', player2_mark)
        else:
            print("Please insert a valid mark! (X or O)")
    
    bd.print_board()
    i = 1
    while not(bd.is_board_full()):
        
        if bd.is_winner(player1_mark):
            print("Player 1 wins this game!")
            if isinstance(p1, Computer):
                p1.moves_outcome.loc[num_game, 'Outcome'] = 1
            else:
                p2.moves_outcome.loc[num_game, 'Outcome'] = 0
            break
        elif bd.is_winner(player2_mark):
            print("Player 2 wins this game!")
            if isinstance(p2, Computer):
                p2.moves_outcome.loc[num_game, 'Outcome'] = 1
            else:
                p1.moves_outcome.loc[num_game, 'Outcome'] = 0
            break
        #elif bd.
        
        if i % 2 == 1:
            #palyer1 move
            if not (bd.is_winner(player1_mark)):
                if isinstance(p1, Computer):
                    move = p1.play(i)
                    p1.moves_outcome.loc[num_game, 'Move '+str(i)] = move
                else:
                    if isinstance(p1, Player):
                        move = p1.play(player1_mark)
                    else:
                        move = p1.play()
                    p1.moves_outcome.loc[num_game, 'Move '+str(i)] = move
                bd.insert_letter(player1_mark, move)
                bd.print_board()
            else:
                print("Player1 wins")
                if isinstance(p1, Computer):
                    p1.moves_outcome.loc[num_game, 'Outcome'] = 1
                else:
                    p2.moves_outcome.loc[num_game, 'Outcome'] = 0
                break
        else:
            #player2 move
            if not (bd.is_winner(player2_mark)):
                if isinstance(p2, Computer):
                    move = p2.play(i)
                    p2.moves_outcome.loc[num_game, 'Move '+str(i)] = move
                else:
                    if isinstance(p2, Player):
                        move = p2.play(player2_mark)
                    else:
                        move = p2.play()
                    p1.moves_outcome.loc[num_game, 'Move '+str(i)] = move
                    bd.insert_letter(player2_mark, move)
                bd.print_board()
            else:
                print("Player2 wins!")
                if isinstance(p2, Computer):
                    p2.moves_outcome.loc[num_game, 'Outcome'] = 1
                else:
                    p1.moves_outcome.loc[num_game, 'Outcome'] = 0
                break
        i += 1
    else:
        if bd.is_winner(player1_mark):
            print("Player 1 wins this game!")
            if isinstance(p1, Computer):
                p1.moves_outcome.loc[num_game, 'Outcome'] = 1
            else:
                p2.moves_outcome.loc[num_game, 'Outcome'] = 0
        elif bd.is_winner(player2_mark):
            print("Player 2 wins this game!")
            if isinstance(p2, Computer):
                p2.moves_outcome.loc[num_game, 'Outcome'] = 1
            else:
                p1.moves_outcome.loc[num_game, 'Outcome'] = 0
        else:
            if isinstance(p1, Computer):
                p1.moves_outcome.loc[num_game, 'Outcome'] = 1
            else:
                p2.moves_outcome.loc[num_game, 'Outcome'] = 1
            print("Game is Tie!")
        
board = [' ' for _ in range(10)]
bd = Board(board)
global p1, p2
num_game = 0
goes_first = ''
while True:
    goes_first = input("Do you want the computer to go first or second? [F, S] ").upper()
    if goes_first[0] == 'F':
        p1 = Computer()
        p2 = Player()
        break
    elif goes_first[0] == 'S':
        p1 = Player()
        p2 = Computer()
        break
    else:
        print("Please respond with F(irst) or S(econd))!")
        
while True:
    answer = input('Do you want to play? (Y/N)').upper()
    if answer[0] == 'Y':
        bd.reset_board()
        print('-----------------------------------')
        main()
    elif answer[0] == 'N':
        break
    else:
        print("Please enter Y(es) or N(o)!")
    num_game += 1

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        