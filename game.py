class TicTacToe:
    def __init__(self):
        self.board = [ ' ' for _ in range(9)]
        self.current_winner = None # keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)] :
            #print(row)
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        
    def available_moves(self):
        moves = []
        for (index , val) in enumerate(self.board):
            if val == ' ':
                moves.append(index) 
        return moves
        #list comprehension
        #return [i for i, val in enumerate(self.board) if spot == ' ']
    
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

        #check diag
        

        return False

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] == letter
            #check winner
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

#play function outside of the class
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    #iterate while the board still has empty square
    while game.has_empty_square():
        #get the move from player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'made a move to square {square}')
                game.print_board()
                print('')
            
            #check winner
            if game.current_winner != None:
                if print_game:
                    print(f'player {letter} won !')
                return letter
            
            #switch player
            letter = 'O' if letter == 'X' else 'X'
    
    if print_game:
        print('It is a tie!')


            