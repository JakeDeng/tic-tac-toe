import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o

        self.letter = letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        #call init method in the base player class
        super().__init__(letter)
    
    def get_move(self, game):
        #choose a random valid spot
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        #call init method in the base player class
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8):")
            #checking
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        
        return val

#极小化极大算法 minimax
#maximize the utility function at its turn
#minimize the utility function at opponent's turn
class AIPlayer(Player):
    def __init__(self, letter):
        #call init method in the base player class
        super().__init__(letter)
    
    def get_move(self, game):
        #first step, random
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #get move based off the minimax algorithm
            square = self.minimax(game, self.letter)
            print(f"AI move to {square['position']} with score {square['score']}")
            square = square['position']
            
        return square
    
    #utility function 
    #calculate score based on the move
    def utility(self, state, is_opponent):
        sign = 1 if is_opponent else -1
        return  sign * (state.num_empty_squares() + 1) 

    def minimax(self, state, player):
        max_player = self.letter #AI player itself
        other_player = 'O' if player == 'X' else 'X'

        #base cases: check if the previous move is a winner
        #win at least amount of steps as possible
        if state.current_winner == other_player:
            #return position and score
            return {
                'position': None,
                'score':self.utility(state, max_player == other_player) #1 if your turn, -1 if opponent's turn
            }
        elif not state.has_empty_square(): # no empty square
            return {
                'position': None,
                'score':0
            }
        
        #algorithm starts
        if player == max_player:
            best_move = {'position': None, 'score':-math.inf} #each score should maximize(be larger than this)
        else:
            best_move = {'position': None, 'score':math.inf} #each score should minimize
        
        for possibile_move in state.available_moves():
            #1. make a move, try that spot
            state.make_move(possibile_move, player)

            #2. recurse using minimax to simulate a game after making that move
            simulated_move = self.minimax(state, other_player)

            #3. undo the move
            state.board[possibile_move] = ' '
            state.current_winner = None
            simulated_move['position'] = possibile_move

            #4. update dictionary if necessary
            #maximize the max_player and minimize the other player
            if player == max_player:
                if simulated_move['score'] > best_move['score']:
                    best_move = simulated_move
            else:
                if simulated_move['score'] < best_move['score']:
                    best_move = simulated_move
        return best_move

        











