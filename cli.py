from os import sys

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
print "[[1][2][3]]\n[[4][5][6]]\n[[7][8][9]]\n"
print '-'* 20
print "The game is on!"
print '-'* 20

def update_game_board(move, current_player):
    if current_player == 1:
        piece_type = 'X'
    else: 
        piece_type = 'O'
    game_array[move - 1][0] += piece_type
    game_board = (str(game_array[0:3]).replace(',', '') + 
            "\n" + str(game_array[3:6]).replace(',', '') +  
            "\n" + str(game_array[6:9]).replace(',', '')
        )
    print game_board

def check_game_status():
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

def get_move():
    worked = False
    move = raw_input("> ")
    try:
        move = int(move)
        if move in range(1,10):
            if game_array[move - 1][0] == '':
                worked = True
    except:
        move = ''
    return [worked, move]

# handle game interaction
total_moves = 0
current_player = 1

while True: 
    if current_player == 1:
        print "Player 1, what is your move?"
        worked, move = get_move()
        while worked == False:
            print "Invalid move. Try again:"
            worked, move = get_move()
        update_game_board(move, current_player)
        total_moves += 1
        game_won = check_game_status()
        if game_won:
            print "Player 1 wins!"
            sys.exit()
        if total_moves >= 9 and not game_won:
            print "It's a draw!"
            sys.exit()
        else:
            current_player = 2
    if current_player == 2:
        print "Player 2, what is your move?"
        worked, move = get_move()
        while worked == False:
            print "Invalid move. Try again:"
            worked, move = get_move()
        update_game_board(move, current_player)
        total_moves += 1
        game_won = check_game_status()
        if game_won:
            print "Player 2 wins!"
            sys.exit()
        if total_moves >= 9 and not game_won:
            print "It's a draw!"
            sys.exit()
        else:
            current_player = 1

