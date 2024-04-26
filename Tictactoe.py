"""
@author: Asia Harris
Discrete Structures CS 20...
Tictactoe project to show the ....
"""
 #Prints every element in the board in a grid layout
def print_board(board):
    for r in range(len(board)):
        print(board[r][0] + " " + board[r][1] + " " + board[r][2])
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
    print("To play ")
board_dash = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board_num =[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
Y_N = input("Welcome to Tic-Tac-Toe! Would you like to play? Y/N: ")
if(Y_N == "Y"):
    play_game(board_dash, board_num)
