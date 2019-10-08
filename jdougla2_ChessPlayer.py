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
        boardy = deepcopy(self.board)
        myPieces = self.get_pieces(boardy, self.color)
        theirPieces = self.get_pieces(boardy, self.opponnentColor)
        
        print(myPieces)
        return random.choice(self.board.get_all_available_legal_moves(self.color))
    
    def get_pieces(self, boardy, color):
        boardyMoves = boardy.get_all_available_legal_moves(color)
        pieces = []
        for x in boardyMoves:
            pieces.append(x[0])
        
        res = []
        for i in myPieces:
            if i not in res:
                res.append(i)