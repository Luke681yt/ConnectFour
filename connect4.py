import random
import doctest

def draw_board(board):
    """(lst) -> ()
    Assigns indexes for each spot on the board
    """
    print(board[5][0],"|",board[5][1],"|",board[5][2],"|",board[5][3],"|",board[5][4],"|",board[5][5],"|",board[5][6])
    print("--------------------------")
    print(board[4][0],"|",board[4][1],"|",board[4][2],"|",board[4][3],"|",board[4][4],"|",board[4][5],"|",board[4][6])
    print("--------------------------")
    print(board[3][0],"|",board[3][1],"|",board[3][2],"|",board[3][3],"|",board[3][4],"|",board[3][5],"|",board[3][6])
    print("--------------------------")
    print(board[2][0],"|",board[2][1],"|",board[2][2],"|",board[2][3],"|",board[2][4],"|",board[2][5],"|",board[2][6])
    print("--------------------------")
    print(board[1][0],"|",board[1][1],"|",board[1][2],"|",board[1][3],"|",board[1][4],"|",board[1][5],"|",board[1][6])
    print("--------------------------")
    print(board[0][0],"|",board[0][1],"|",board[0][2],"|",board[0][3],"|",board[0][4],"|",board[0][5],"|",board[0][6])

def coin_flip():
    """() -> (int)
    Returns either 1 or 0 to randomize starting player
    """
    count = 0
    coin = ["X", "O"]
    flip = random.choice(coin)
    if flip == "O": #determines who starts first
        count += 1
    return count

#return players column choice
def player_choice():
    """() -> (int)
    Returns players choice of column
    """
    while True:
        if (count%2 == 0):
            choice = input("\nPlayer X, enter (1-7): ")
        else:
            choice = input("\nPlayer O, enter (1-7): ")
        try: #validates number
            choice = int(choice)
            if 1 <= (choice) <= 7: #validates number 1 to 7
                return choice
            else:
                print("Invalid input")
        except:
            print("Invalid input")

#update players choice
def player_turn(choice, board):
    """(int, lst) -> ()
    Update the board with the players choice of column
    """
    row = 0
    while True:
        row = 0
        for row in range(0,6): #cycle through rows
            if (board[row][choice-1] == " "): #check if theres a blank spot in column*
                if (count%2 == 0):
                    board[row][choice-1] = "X"
                else:
                    board[row][choice-1] = "O"
                return
        print("The column is full!") #*if not, get a new column choice
        choice = player_choice()

#check if win
def check_win(board):
    """(lst) -> (bool)
    Checks all win conditions, then returns True or False respectively
    """
    #horizontal
    for row in range(0,6):
        for column in range(0,4):
            if (board[row][column]==board[row][column+1] and board[row][column]==board[row][column+2] and board[row][column]==board[row][column+3] and board[row][column]!=" "):
                return True
      
    #vertical
    for row in range(0,3):
        for column in range(0,7):
            if (board[row][column]==board[row+1][column] and board[row][column]==board[row+2][column] and board[row][column]==board[row+3][column] and board[row][column]!=" "):
                return True

    #diagonal going up
    for row in range(0,3):
        for column in range(0,4):
            if (board[row][column]==board[row+1][column+1] and board[row][column]==board[row+2][column+2] and board[row][column]==board[row+3][column+3] and board[row][column]!=" "):
                return True

    #diagonal going down
    for row in range(3,6):
        for column in range(0,4):
            if (board[row][column]==board[row-1][column+1] and board[row][column]==board[row-2][column+2] and board[row][column]==board[row-3][column+3] and board[row][column]!=" "):
                return True

#check if tie (checks if all spots full)
def check_tie(board):
    """(lst) -> (bool)
    Checks tie condition, then returns True or False respectively
    >>> check_tie(" ")
    False
    """
    for t in range(0,7):
        for tie in range(0,6):
            if board[tie][t] == " ":
                return False
            else:
                continue
    return True

#actions in each turn
def turn():
    """
    Runs the turn by drawing board, getting input, updating board
    """
    draw_board(board) #draw board (blank spots with indexes)
    choice = player_choice() #get player choice
    player_turn(choice, board) #update player choice

#check if win, tie, and return the answer
def game_check(count, board):
    """(int, lst) -> (bool)
    Runs the check_win and check_tie; return True will end the game (False; continue game)
    """
    if check_win(board): #runs the check win function
        if count%2 == 0: #if even, player 1 wins, otherwise player 2 wins
            draw_board(board) #draw the board to see the final 4 match
            print("Player X wins!")
            return True
        else:
            draw_board(board)
            print("Player O wins!")
            return True
    if check_tie(board): #runs the check tie function
        draw_board(board) #draw the final tie board
        print("The game is a tie!")
        return True

#ask for rematch
def rematch(option):
    """(str) -> (bool)
    Returns players choice to rematch
    >>> rematch("1")
    True
    """
    if option == "1":
        return True
    else:
        return False


if  __name__ == "__main__":
    doctest.testmod()
    print("\nDetermine who is Player X and Player O\n")

    while True: #assigns spots on the board --V
        
        board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
        count = coin_flip() #determines who starts first
        while True:
            turn() #run a players turn
            print("")
            if game_check(count, board): #checks if anyone wins or if tie
                break
            count += 1 #next turn
        r_option = input("One more game? Press 1 for yes and any other key to exit: ")
        if rematch(r_option): #asks user for rematch
            print("")
            continue
        else:
            break

    print("Thanks for playing the game! ")