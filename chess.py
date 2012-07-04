#/usr/bin/python
#coding=utf8


class Board():
    def __init__(self):
        pass


    def __repr__(self):
        board = Board().draw_board()
        lines = []
        for n in '87654321':
            fields = [board[a + n] for a in 'ABCDEFGH']
            lines.append(' '.join(fields))
        return '\n'.join(lines)


    def draw_board(self):
        board = {'A1': 'r', 'A2': 'p', 'A3': ' ', 'A4': ' ',
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
        return board


def main():
    print Board()


if __name__ == '__main__':
    main()
