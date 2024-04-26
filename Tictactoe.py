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
def check_winner(board, move):
    for i in range(3):
        #Checking for lateral wins
        if ((board[i][0] == board[i][1] == board[i][2] == move) or (board[0][i] == board[1][i] == board[2][i] == move)):
            return True
        #Checking for diagonal wins
        if ((board[0][0] == board[1][1] == board[2][2] == move) or (board[0][2] == board[1][1] == board[2][0] == move)):
            return True
    return False

def play_game(board1, board2, player):
    moves = ["X", "O"]
    spot = int(input("Enter your move (1-9): ")) - 1
    r = spot // 3
    c = spot % 3
    if(0 <= spot <= 8 and board1[r][c] == "_"):
        board1[r][c] = moves[player-1]
    print_board(board1)         
    
board_dash = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board_num =[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
Y_N = input("Welcome to Tic-Tac-Toe! Would you like to play? Y/N: ")
if(Y_N == "Y"):
    player_1 = input("Enter your name: ")
    player_2 = input("Would you like to play against the computer or a friend?: ")
    if(player_2 == "friend" or player_2 == "Friend"):
        player_2 = input("Enter the friend's name: ")
    print(player_1 + " will be X, and " + player_2 + " will be O.")
    print()
    print("This will be your board: ")
    print_board(board_dash)
    print("And these are the corresponding numbers: ")
    print_board(board_num)
    print("To play, enter the number of the space you want to place your X or O. Have fun!")
    play_game(board_dash, board_num, 1)
    check_winner(board_dash, "X")
