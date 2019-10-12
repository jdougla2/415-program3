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
        bestMove = -1
        y = 0
        for x in moves:
            boardy = deepcopy(self.board)
            orig = self.get_opp_pieces(boardy, self.color)
            boardy.make_move(x[0], x[1])
            new = self.get_opp_pieces(boardy, self.color)
            if new < orig or boardy.is_king_in_check(opponentColor):
                bestMove = y
                break
            y = y + 1    

        if bestMove == -1:
            return random.choice(self.board.get_all_available_legal_moves(self.color))
        
        return self.board.get_all_available_legal_moves(self.color)[bestMove]
    
    def get_opp_pieces(self, boardy, color):
        opponentColor = ''
        if color == 'black':
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
    
    def get_opp_piece_value(self, boardy, color): #Wasn't able to get working in time
        opponentColor = ''
        if color == 'black':
            opponentColor = 'white'
        else:
            opponentColor = 'black'
            
        allPieces = list(boardy.items())
        oppPieces = []
        for x in range(len(allPieces)):
            allPieces[x] = [allPieces[x][0], allPieces[x][1].get_notation()]
        
        if opponentColor == 'white':
            for x in allPieces:
                if x[1].isupper() == True:
                    oppPieces.append(x)
        else:
            for x in allPieces:
                if x[1].islower() == True:
                    oppPieces.append(x)
                    
        for x in range(len(oppPieces)):
            if oppPieces[x][1].lower() == 'p':
                oppPieces[x] = [oppPieces[x][0], 1]
            elif oppPieces[x][1].lower() == 'p':
                oppPieces[x] = [oppPieces[x][0], 3]
            else:
                oppPieces[x] = [oppPieces[x][0], 2]
        
        return oppPieces