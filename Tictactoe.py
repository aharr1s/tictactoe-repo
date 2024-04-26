"""
@author: Asia Harris
Discrete Structures CS 20...
Tictactoe project to show the ....
"""

def print_board(board):
    for r in range(len(board)):
        print(board[r][0] + " " + board[r][1] + " " + board[r][2])


board =[["P11", "P12", "P13"], ["P21", "P22", "P23"], ["P31", "P32", "P33"]]
print_board(board)