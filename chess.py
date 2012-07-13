#/usr/bin/python
#coding=utf8

import sys
import os


PIECES = {'white': 'prnbkq', 'black': 'PRNBQK'}

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
        pieces = {'p': '♙', 'P': '♟', 'r': '♖', 'R': '♜', 'n': '♘', 'N': '♞',
                  'b': '♗', 'B': '♝', 'q': '♕', 'Q': '♛', 'k': '♔', 'K': '♚'}
        for n in '87654321':
            fields = [self.board[a + n] for a in 'ABCDEFGH']
            lines.append(n + ' ' + ' '.join(fields))
        board = '\n'.join(lines)
        for piece in pieces:
            board = board.replace(piece, pieces[piece])
        board += '\n  %s' % ' '.join('ABCDEFGH')
        return board


    def __getitem__(self, piece):
        return self.board.get(piece)


    def move(self, move):
        '''If the move is legal, update the board with the new positions.'''
        # TODO Call legal within this method.
        try:
            piece = self.board[move[:2]]
            self.board[move[:2]] = ' '
            self.board[move[2:]] = piece
        except KeyError as error:
            print 'Invalid move: %s. Use the form "E2E4".' % error


def motion(move, turn):
    '''Return the number of fields moved in the grid.'''
    chars = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    start = move[:2]
    end = move[2:]
    x_axis = int(chars[start[0]]) - int(chars[end[0]])
    y_axis = int(end[1]) - int(start[1])
    if turn == 'white':
        return x_axis, y_axis
    else:
        return x_axis, -y_axis


def clear_path(board, move, piece, turn):
    '''Return True if there are no pieces between the start and endpoints,
    otherwise return False.'''
    if piece in 'pP':
        if turn == 'white':
            plus = 1
        elif turn == 'black':
            plus = -1
        jump = move[0] + str(int(move[1]) + plus)
        if board[jump] == ' ':
            return True
    if piece in 'rR':
        return True
    if piece in 'nN':
        return True
    if piece in 'bB':
        return True
    if piece in 'qQ':
        return True
    if piece in 'kK':
        return True


def legal(move, piece, turn, board):
    '''Return True if the move is legal, otherwise return False.'''
    # Use the king function before and after a move.
    # Return False if trying to move a piece of the opposite team.
    target = board[move[2:]]
    pieces = PIECES[turn]
    opposite = PIECES['black'] if turn == 'white' else PIECES['white']
    # Return False if trying to move no piece or an enemies piece and if the
    # target field contains an allied piece.
    if any([piece not in pieces, target in pieces]):
        print 'Illegal move, %s\'s turn.' % turn
        return False
    movement = motion(move, turn)
    print movement
    if piece in 'pP':
        if target in opposite:
            # Pawns can only kill with a diagonal move by one square.
            if movement not in [(-1, 1), (1, 1)]:
                return False
        if movement == (0, 1):
            return True
        if movement == (0, 2):
            if clear_path(board, move, piece, turn):
                if any([turn == 'white' and move[1] == '2',
                        turn == 'black' and move[1] == '7']):
                    return True
        return False
    if piece in 'rR':
        # Rooks can only move in a horizontal or vertical line.
        if any([movement[0] == 0 and movement[1] != 0,
                movement[0] != 0 and movement[1] == 0]):
            if clear_path(board, move, piece, turn):
                return True
        # Invalid rook move.
        else:
            return False
    if piece in 'nN':
        pass
    if piece in 'bB':
        # Bishops move diagonally so the absolute values of the axes should be
        # equal.
        if abs(movement[0]) == abs(movement[1]):
            if clear_path(board, move, piece, turn):
                return True
        else:
            return False
    if piece in 'qQ':
        pass
    if piece in 'kK':
        pass
    return True


def king():
    # Check whether the king is being threatened before the next move, whether
    # he can be protected if he is (if he can't be protected the game is over)
    # and check whether the next move leaves him in check.
    # Return False if the king is threatened or if the move leaves him
    # threatened, return None if the game is over (the king is being threatened
    # and cannot be defended) and True if none of this applies.
    pass


def main():
    board = Board()
    print board
    turn = 'white'
    while True:
        move = raw_input('Enter a move: ').upper()
        try:
            os.system('clear')
            if move:
                piece = board[move[:2]]
                if legal(move, piece, turn, board):
                    board.move(move)
                    turn = 'black' if turn == 'white' else 'white'
                    print turn
            print
            print board
            print
        except (KeyboardInterrupt, EOFError):
            print
            sys.exit()

if __name__ == '__main__':
    main()
