"""
@author: Asia Harris
Discrete Structures CS 20...
Tictactoe project to show the ....
"""
#Prints every element in the board in a grid layout
def print_board(board):
    for r in range(len(board)):
        print(board[r][0] + " " + board[r][1] + " " + board[r][2])
#Edits the board with updated moves
def edit_board(board1, board2, move, spot):
    if(spot == 1):
        board1[0][0] = move
        board2[0][0] = move  
    elif(spot == 2):
        board1[0][1] = move
        board2[0][1] = move  
    elif(spot == 3):
        board1[0][2] = move
        board2[0][2] = move  
    elif(spot == 4):
        board1[1][0] = move
        board2[1][0] = move  
    elif(spot == 5):
        board1[1][1] = move
        board2[1][1] = move 
    elif(spot == 6):
        board1[1][2] = move
        board2[1][2] = move 
    elif(spot == 7):
        board1[2][0] = move
        board2[2][0] = move 
    elif(spot == 8):
        board1[2][1] = move
        board2[2][1] = move 
    else:
        board1[2][2] = move
        board2[2][2] = move 
#Will check for winner ... 
#def check_winner(board):
def play_game(board1, board2):
    player_1 = input("Enter your name: ")
    player_2 = input("Would you like to play against the computer or a friend?: ")
    if(player_2 == "friend" or player_2 == "Friend"):
        player_2 = input("Enter the friend's name: ")
    print(player_1 + " will be X, and " + player_2 + " will be O.")
    print()
    print("This will be your board: ")
    print_board(board1)
    print("And these are the corresponding numbers: ")
    print_board(board2)
    print("To play, enter the number of the space you want to place your X or O. Have fun!")
    spot = input(player_1 + ", you will go first. Enter your spot: ")
    edit_board(board1, board2, "X", spot)    
    print_board(board1)         
    
board_dash = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board_num =[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
Y_N = input("Welcome to Tic-Tac-Toe! Would you like to play? Y/N: ")
if(Y_N == "Y"):
    play_game(board_dash, board_num)
