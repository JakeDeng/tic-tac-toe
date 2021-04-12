from flask import Flask, render_template, url_for
from game import TicTacToe, play
from player import RandomComputerPlayer, HumanPlayer, AIPlayer

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    #use session storage to save the board
    return render_template('home.html')

@app.route("/move", methods=["POST"])
def move():
    from flask import request
    square = request.form['square']

    return render_template('home.html')

# main process
if __name__ == '__main__':
   
    #create player and game
    x_player = HumanPlayer('X')
    o_player = AIPlayer('O')
    new_game = TicTacToe()
    #play
    play(new_game, x_player, o_player, True)







 
