from game import TicTacToe, play
from player import RandomComputerPlayer, HumanPlayer, AIPlayer

#main process
if __name__ == "__main__":
    #create player and game
    x_player = AIPlayer('X')
    o_player = HumanPlayer('O')
    new_game = TicTacToe()

    #play
    play(new_game, x_player, o_player)


 
