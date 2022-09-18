#tic tac toe

"""
tic tac toe board
[
    [-, -, -],
    [-, -, -]'
    [-, -, -]

]

user_input -> something 1-9
if the user enter anything else: tell them to go again
check if the user_input is already taken
add it to the board
check if user won: checking rows, columns, diagonals
toggle between users upon sucessful moves

"""

board = [

    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]

]

""" create a print board function """

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end = "")
        print() 

print_board(board)

def quit(user_input)
    if user_input == "q": return False 
    else: return True   

while True:
    user_input = input("Enter a position 1 through 9 or enter \"q\"")