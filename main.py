class Tictactoe:
    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-', ]
    player_turn = 0
    game = ''

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def get_player1(self):
        return self.player1

    def get_player2(self):
        return self.player2

    @classmethod
    def print_board(cls):
        print(cls.board[0] + ' | ' + cls.board[1] + ' | ' + cls.board[2])
        print(cls.board[3] + ' | ' + cls.board[4] + ' | ' + cls.board[5])
        print(cls.board[6] + ' | ' + cls.board[7] + ' | ' + cls.board[8])

    def start_game(self):
        winner = ''
        Tictactoe.player_turn = 1
        Tictactoe.print_board()
        while Tictactoe.game != 'over':
            self.handle_turn()
            self.print_board()
            winner = Tictactoe.check_board()

        winner = Tictactoe.check_board()
        print('Player1 wins') if winner == self.player1 else print('Player2 wins')

    def handle_turn(self):
        if self.player_turn % 2 == 0:
            position = input('Player 2, choose a position from 1-9:')
            position = int(position) - 1
            Tictactoe.board[position] = self.get_player2()

        else:
            position = input('Player 1, choose a position from 1-9:')
            position = int(position) - 1
            Tictactoe.board[position] = self.get_player1()

        Tictactoe.player_turn += 1

    @classmethod
    def check_board(cls):
        row1 = cls.board[0] == cls.board[1] == cls.board[2] != '-'
        row2 = cls.board[3] == cls.board[4] == cls.board[5] != '-'
        row3 = cls.board[6] == cls.board[7] == cls.board[8] != '-'

        col1 = cls.board[0] == cls.board[3] == cls.board[6] != '-'
        col2 = cls.board[1] == cls.board[4] == cls.board[7] != '-'
        col3 = cls.board[2] == cls.board[5] == cls.board[8] != '-'

        diag1 = cls.board[0] == cls.board[4] == cls.board[8] != '-'
        diag2 = cls.board[2] == cls.board[4] == cls.board[6] != '-'

        if row1 or row2 or row3:
            cls.game = 'over'
            if row1:
                return cls.board[0]
            elif row2:
                return cls.board[3]
            elif row3:
                return cls.board[6]
        elif col1 or col2 or col3:
            cls.game = 'over'
            if col1:
                return cls.board[0]
            elif col2:
                return cls.board[3]
            elif col3:
                return cls.board[6]
        elif diag1 or diag2:
            cls.game = 'over'
            if diag1:
                return cls.board[0]
            else:
                return cls.board[2]


def main():
    game = Tictactoe('x', 'o')
    game.start_game()


if __name__ == '__main__':
    main()
