import random
from connect4 import *

coin=coin_flip()
print(coin)

board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
draw_board(board)
assert (check_tie(board))==False
assert (check_win(board))==None

board = [["O","X","O","X","O","X","O"],["O","X","O","X","O","X","X"],["O","X","O","X","O","X","O"],["X","O","X","O","X","O","X"],["O","O","X","O","X","O","X"],["X","X","O","X","O","X","O"]]
draw_board(board)
assert (check_tie(board))==True
assert (check_win(board))==None

board = [["X","X","X","X"," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
draw_board(board)
assert (check_tie(board))==False
assert (check_win(board))==True

board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
assert rematch("1")==True