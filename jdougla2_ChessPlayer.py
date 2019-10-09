# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:58:49 2019

@author: Jack
"""

from chess_player import ChessPlayer
import random
from copy import deepcopy

class jdougla2_ChessPlayer(ChessPlayer):
    
    def __init__(self, board, color):
        super().__init__(board, color)
        if self.color == 'Black':
            self.opponentColor = 'White'
        else:
            self.opponentColor = 'Black'
            
    def get_move(self, your_remaining_time, opp_remaining_time, prog_stuff):
        opponentColor = ''
        if self.color == 'black':
            opponentColor = 'white'
        else:
            opponentColor = 'black'
        boardy = deepcopy(self.board)
        moves = boardy.get_all_available_legal_moves(self.color)
        #print(len(moves))
        bestMove = -1
        y = 0
        for x in moves:
            boardy = deepcopy(self.board)
            #orig = boardy.all_occupied_positions(opponentColor)
            orig = self.get_opp_pieces(boardy)
            boardy.make_move(x[0], x[1])
            #print(len(self.get_pieces(boardy, opponentColor)))
            #new = boardy.all_occupied_positions(opponentColor)
            new = self.get_opp_pieces(boardy)
            if new < orig or boardy.is_king_in_check(opponentColor):
                bestMove = y
                break
                #print('here')
            y = y + 1    

        if bestMove == -1:
            return random.choice(self.board.get_all_available_legal_moves(self.color))
        
        #print()
        return self.board.get_all_available_legal_moves(self.color)[bestMove]
    
    def get_opp_pieces(self, boardy):
        opponentColor = ''
        if self.color == 'black':
            opponentColor = 'white'
        else:
            opponentColor = 'black'
            
        allPieces = []
        oppPieces = []
        
        for x in boardy.items():
            allPieces.append(x[1].get_notation())
            
        if opponentColor == 'white':
            for x in allPieces:
                if x.isupper() == True:
                    oppPieces.append(x)
        else:
            for x in allPieces:
                if x.islower() == True:
                    oppPieces.append(x)
        
        return len(oppPieces)