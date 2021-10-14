import math

def check_valid(position, board):
    num = len(board)
    if position<  0 or position >(num-1):
      return False 
    elif board[position] != 0:
      return False
    elif position == 0: 
      return board[position+1] == 0
    elif position == num-1:
      return board[position-1] == 0
    elif board[position+1] != 0 or board[position-1] != 0:
      return False
    else:
      return True

def valid_positions(board):
      #return valid moves left as list
      valid_moves = []
      for i in range(len(board)):
        if check_valid(i, board):
          valid_moves.append(i)
      return valid_moves

def game_over(board):
    #check if someone has won, return winner
    valid = valid_positions(board)
    if len(valid) == 0:
      return True
    return False

def try_move(player,position,board):
    #fill a square on board, return board (list)
    board = board.copy()
    board[position] = player
    return board



def heuristic_score(board,winner):

    if game_over(board):
      if winner == 'AI':
        return 100
      else:
        return -100
        
    else: 
      return 0


def get_move(board):
    options = {}
    validMoves = valid_positions(board)
    bestScore = -math.inf

    for move in validMoves:
      new_board = try_move('AI',move,board)
      score = minimax(new_board,1,False)
      options[move] = score

      if(score > bestScore):
        bestScore = score
        bestMove = move

    print(options)
    return bestMove



def minimax(board, depth, isMaximizing):
    maxDepth = 6
    gameOver = game_over(board) 
    validMoves = valid_positions(board)
    
    #print('depth', depth, 'board', board)

    if (depth == maxDepth) or gameOver:

      if isMaximizing: winner = 'Human'
      else: winner = 'AI'
      #print('entering heuristic. depth', depth, 'winner',winner)

      return heuristic_score(board,winner)

    else:

      if isMaximizing:
        value = -math.inf
        
        for move in validMoves:
          next_step = try_move('AI',move,board)
          value = max(value,minimax(next_step, depth+1,False))

      else:
        value = math.inf
        for move in validMoves:
          next_step = try_move('Human',move,board)
          value = min(value,minimax(next_step, depth+1,True))
              
      return value
