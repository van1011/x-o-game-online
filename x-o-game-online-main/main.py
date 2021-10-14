from flask import Flask, render_template, request, redirect, url_for
from gamePlay import check_valid, valid_positions, game_over, get_move, minimax, heuristic_score, try_move

app = Flask(__name__)
global board

@app.route("/")
def main():
  return render_template("main.html")

@app.route("/choose/<mode>", methods = ['GET', 'POST'])
def choose(mode):
  global board
  if request.method == 'POST' and request.form['num']:
    num = int(request.form["num"])
    board = [0]*num
    return redirect(url_for('game', mode = mode))

  return render_template("choose.html")

@app.route("/game/<mode>", methods = ['GET', 'POST'])
def game(mode):
  message = ""
  global board
  if request.method == 'POST' and request.form['box']:
    position = int(request.form["box"])

    #check if position valid
    if check_valid(position,board) == True:
      board[position] = 1

      #check end game
      if game_over(board):
        return redirect(url_for("endgame", result = 'win'))

      #AI moves
      elif mode == 'AI':
        AIposition = get_move(board)
        board[AIposition] =2

        #check end game
        if game_over(board):
          return redirect(url_for("endgame", result = 'lose'))
    else:
      message = "not valid"
    
  return render_template("gameboard.html", board=board, message = message)

@app.route("/end/<result>")
def endgame(result):
  return render_template("endgame.html", board=board, message = result)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)


