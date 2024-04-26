"""
@author: Asia Harris
Discrete Structures, CS 203, Spring 2024
Tictactoe project to show the demonstrate principles in discrete structures. Specifically, it will use the
rules of inferences for the limited winning outcomes of the game. 
"""
#Prints every element in the board in a grid layout
def print_board(board):
    for r in range(len(board)):
        print(board[r][0] + " " + board[r][1] + " " + board[r][2])
#Will check for winner, both lateral and diagonal wins
def check_winner(board, move):
    for i in range(3):
        #Checking for row and column wins
        if ((board[i][0] == board[i][1] == board[i][2] == move) or (board[0][i] == board[1][i] == board[2][i] == move)):
            return True
        #Checking for diagonal wins
        if ((board[0][0] == board[1][1] == board[2][2] == move) or (board[0][2] == board[1][1] == board[2][0] == move)):
            return True
    return False
#The actual gameplay
def play_game(board, player1, player2):
    moves = ["X", "O"]
    players = [player1, player2]
    for i in range(9):
        player = players[i%2]
        move = moves[i%2]
        print(player + "'s turn!")
        while True:
            try:
                spot = int(input("Enter your move (1-9): ")) - 1
                r = spot // 3
                c = spot % 3
                if(0 <= spot <= 8 and board[r][c] == "_"):
                    board[r][c] = move
                    print_board(board)
                    break
                print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        if (check_winner(board, move)):
            print()
            print_board(board)
            print(player + "  wins! Winner winner, chicken dinner!")
            return
    print("It's a tie!")
                        
    
board_dash = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board_num =[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
moves = ["X", "O"]
Y_N = input("Welcome to Tic-Tac-Toe! Would you like to play? Y/N: ")
if(Y_N.lower() == "y"):
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

    #Allows game to continue after 1 round
    while True:
        play_game(board_dash, player_1, player_2)
        Y_N = input("Would you like to play again? Y/N: ")
        if(Y_N.lower() != "y"):
            print("Thanks for playing!")
            break
        board_dash = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
