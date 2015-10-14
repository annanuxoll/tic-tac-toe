# need to ask each player to make a move
# players will move by typing the number of the square for their next move
# I'll track the moves by adding to an array. At each step, the program 
# will check that that spot is not empty, and display an error message if the
# spot is already full. 
# At each step, the program will also check that neither player has 
# won the game- if a player has won, a winning message will be displayed. 
# optionally, I'd also like to display helptext on startup or with a 
# -h flag


# going to want to use argv
from os import sys
import time





# store the information here
game_array = [[''], [''], [''], [''], [''], [''], [''], [''], ['']]

# make the game board something that displays nicely
game_board = (str(game_array[0:3]).replace(',', '') + 
    "\n" + str(game_array[3:6]).replace(',', '') +  
    "\n" + str(game_array[6:9]).replace(',', '')
    )

# helptext 
print "TIC-TAC-TOE"
print "Player 1 is X, player 2 is O"
print "The board game looks like this:"
print game_board
print "To play, type the number of the square you'd like to claim."
print "The squares are numbered 1-9, like so:"
square_numbers = "[[1][2][3]]\n[[4][5][6]]\n[[7][8][9]]\n"
print square_numbers

# track the current player
current_player = 1

def update_game_board(move, current_player):
    """ move should be an integer from 1-9 and piece_type will be 
    either X or O (as a string)"""
    if current_player == 1:
        piece_type = 'X'
    else: 
        piece_type = 'O'
    if game_array[move - 1][0] == '':
        game_array[move - 1][0] += piece_type
        game_board = (str(game_array[0:3]).replace(',', '') + 
            "\n" + str(game_array[3:6]).replace(',', '') +  
            "\n" + str(game_array[6:9]).replace(',', '')
        )
        print game_board
    else:
        print "Invalid move, try again."
    


# while game_won == False: 

# while game_won == False: 
#     if player_one_went = False:
#         print "Player 1, what is your move?"
#         move = sys.argv[1] 
#         if array[move - 1] != '':
#             array[move - 1] = 'X'
#         # get player 1's move, check that it's ok, then edit the array
#         player_one_went = True
#         # print the game board
#     else: 
#         print "Player 2, what is your move?"
#         move = sys.argv[1] 
#         if array[move - 1] != '':
#             array[move - 1] = 'O'
#         # get player 2's move, check validity, edit array 
#         # print the game board


# # some logic here to check if the game has been won, and by whom. 
# # there are 8 ways to win tic-tac-toe
# # gotta make sure empty strings don't count, here, because with this logic, 
# # the game is already won

# # first 3 ways
# for array in game_board:
#     if array[0] != '':
#         if array[0] == array[1] and array[1] == array[2]:
#             game_won = True

# # next 3 ways
# # gotta check that these aren't empty
# for i in range(2):
#     if game_board[0][i] != '':
#         if (game_board[0][i] == game_board[1][i] 
#             and game_board[1][i] == game_board[2][i]): 
#             game_won = True

# make this into a method
# check if the game has been won, using game_array
# one set of winning moves is 1-2-3, 4-5-6, and 7-8-9
update_game_board(1, 'X')
update_game_board(5, 'X')
update_game_board(8, 'X')

def check_game_status():
    # use turn as input to determine who won?
    """update game_won"""
    # across wins
    game_won = False
    for i in [0, 3, 6]: 
        if game_array[i][0] != '':
            if (game_array[i] == game_array[i+1] and 
                game_array[i+1] == game_array[i+2]):
                game_won = True
    # down wins
    for i in [0, 1, 2]:
        if game_array[i][0] != '':
            if (game_array[i] == game_array[i+3] and 
                game_array[i+3] == game_array[i+6]):
                game_won = True
    # diagonal wins
    for i in [0]:
        if game_array[i][0] != '':
            if (game_array[i] == game_array[i+4] and
                game_array[i+4] == game_array[i+8]):
                game_won = True
    for i in [2]:
        if game_array[i][0] != '':
            if (game_array[i] == game_array[i+2] and
                game_array[i+2] == game_array[i+4]):
                game_won = True
    return game_won

def game_play():
    game_won = check_game_status()
    if game_won == False:
        print "GAME ON!"
    if game_won == True:
        print "GAME OVER!"

game_play()
