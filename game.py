class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None # keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
        
    def available_moves(self):
        avail_moves =  [i for i, x in enumerate(self.board) if x == " "]
        #print('available move:')
        #print(avail_moves)
        return avail_moves
    
    def has_empty_square(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def check_winner(self, square, letter):
        #win if 3 in a row
        #check row
        row_index = square//3
        row = self.board[row_index*3 : (row_index+1)*3]
        #if everything in the list is true then return true, otherwise false
        if all([spot == letter for spot in row]):
            return True

        #check col
        col_index = square%3
        col = [self.board[col_index + i*3] for i in range(3)]
        #col = [spot for index, spot in enumerate(self.board) if index%3 == col_index]
        if all([spot == letter for spot in col]):
            return True

        #check diagonals
        #first check for even number (0,2,4,6,8)
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diag2]):
                return True
        return False

    def make_move(self, square, letter):
        if self.board[square] == " ":
            #print(f'{letter} make move to {square}')
            self.board[square] = letter
            #check winner
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

#play function outside of the class
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
        print('')
    
    letter = x_player.letter
    #iterate while the board still has empty square
    while game.has_empty_square():
        #get the move from player
        if letter == o_player.letter:
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #player makes a move
        if game.make_move(square, letter):
            if print_game:
                #print(letter + f' made a move to square {square}')
                game.print_board()
                print('')
            
            #check winner
            if game.current_winner != None:
                if print_game:
                    print(f'player {letter} won !')
                return letter
            
            #switch player
            letter = o_player.letter if letter == x_player.letter else x_player.letter
        
        #delay
        import time
        time.sleep(0.8)
    
    if print_game:
        print('It is a tie!')


            