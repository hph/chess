#/usr/bin/python
#coding=utf8

import sys

class Board():
    def __init__(self):
        self.board = {'A1': 'r', 'A2': 'p', 'A3': ' ', 'A4': ' ',
                      'A5': ' ', 'A6': ' ', 'A7': 'P', 'A8': 'R',
                      'B1': 'n', 'B2': 'p', 'B3': ' ', 'B4': ' ',
                      'B5': ' ', 'B6': ' ', 'B7': 'P', 'B8': 'N',
                      'C1': 'b', 'C2': 'p', 'C3': ' ', 'C4': ' ',
                      'C5': ' ', 'C6': ' ', 'C7': 'P', 'C8': 'B',
                      'D1': 'q', 'D2': 'p', 'D3': ' ', 'D4': ' ',
                      'D5': ' ', 'D6': ' ', 'D7': 'P', 'D8': 'Q',
                      'E1': 'k', 'E2': 'p', 'E3': ' ', 'E4': ' ',
                      'E5': ' ', 'E6': ' ', 'E7': 'P', 'E8': 'K',
                      'F1': 'b', 'F2': 'p', 'F3': ' ', 'F4': ' ',
                      'F5': ' ', 'F6': ' ', 'F7': 'P', 'F8': 'B',
                      'G1': 'n', 'G2': 'p', 'G3': ' ', 'G4': ' ',
                      'G5': ' ', 'G6': ' ', 'G7': 'P', 'G8': 'N',
                      'H1': 'r', 'H2': 'p', 'H3': ' ', 'H4': ' ',
                      'H5': ' ', 'H6': ' ', 'H7': 'P', 'H8': 'R'}


    def __str__(self):
        lines = []
        for n in '87654321':
            fields = [self.board[a + n] for a in 'ABCDEFGH']
            lines.append(n + ' ' + ' '.join(fields))
        board = '\n'.join(lines)
        pieces = {'p': '♙', 'P': '♟', 'r': '♖', 'R': '♜', 'n': '♘', 'N': '♞',
                  'b': '♗', 'B': '♝', 'q': '♕', 'Q': '♛', 'k': '♔', 'K': '♚'}
        for piece in pieces:
            board = board.replace(piece, pieces[piece])
        board += '\n  %s' % ' '.join('ABCDEFGH')
        return board


    def move(self, move):
        '''If the move is legal, update the board with the new positions.'''
        try:
            piece = self.board[move[0]]
            self.board[move[0]] = ' '
            self.board[move[1]] = piece
        except KeyError as error:
            print 'Invalid move: %s.' % error


    def legal(self, motion):
        '''Return True if the motion is legal, otherwise return False.'''
        pass


def main():
    board = Board()
    print board
    while True:
        try:
            move = raw_input('Enter a move: ')
            if move:
                board.move(move.upper().split('-'))
            print
            print board
            print
        except (KeyboardInterrupt, EOFError):
            print
            sys.exit()

if __name__ == '__main__':
    main()
