import random
board = [None, None, None, None, None, None, None, None, None]

def print_board():
    """Print the board, a row at a time""" 
    row1 = board[0:3]
    print_board_picture(row1)
    print '----------'
    row2 = board[3:6]
    print_board_picture(row2)
    print '----------'
    row3 = board[6:9]
    print_board_picture(row3)
        
def print_board_picture(row):
    for idx, r1 in enumerate(row):
        if r1 == None:
            r1 = ' '
        print r1,
        if idx < 2:
            print "|",
    print ''


def win_by_diagonal(mark):
    """Does the player with a given mark win on the diagonals?"""
    return (board[0] == mark and board[4] == mark and board[8] == mark) or (board[6] == mark and board[4] == mark and board[2] == mark)


def win_by_vertical(mark):
    """Does the player with a given mark win on the columns?"""
    return (board[0] == mark and board[3] == mark and board[6] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8]== mark)


def win_by_horizontal(mark):
    """Does the player with a given mark win on the rows?"""
    return (board[0] == mark and board[1] == mark and board[2] == mark) or (board[3] == mark and board[4] == mark and board[5] == mark) or (board[6] == mark and board[7] == mark and board[8] == mark)


def validate_move(space):
    """Is a player allowed to mark a given space?"""
    if space < 0 or space > 8:
        print "I don't understand how to make a mark at space %s" % space
        return False
    if board[space] is not None:
        print "%s has already gone there!" % board[space]
        return False
    return True


def prompt_for_space():
    """Ask a player for a space until they give one that's legal"""
    space = None

    try:
        space = int(raw_input("Give me a space number from 0 to 8 (and then hit enter): "))
    except ValueError:
        print "That's not a number."
        return prompt_for_space()

    if not validate_move(space):
        return prompt_for_space()

    return space


def human_player(mark):
    """Prompt a player to take their turn"""
    print "It's %s's turn - where would you like to play, %s?" % (mark, mark)
    return prompt_for_space()


def play(mark='X', take_turn=human_player):
    """
    A turn in the game. By default, plays with two human players, starting with
    'X'. Pass an alternative take_turn function to play with a different set of
    players.
    """
    print "\nThe board looks like this:"
    print_board()
    print


    space = take_turn(mark)
    board[space] = mark

    if win_by_diagonal(mark) or win_by_horizontal(mark) or win_by_vertical(mark):
        print "%s wins! Good job!" % mark
        print
        print_board()
    elif not [space for space in board if space is None]:
        print "It's a draw!"
    else:
        play('O' if mark == 'X' else 'X', take_turn)    


def with_a_computer_player(mark):
    """
    Use a computer player (controlled by the computer_player function) for
    the 'O' player and a human player for 'X'.
    """
    if mark == 'X':
        return human_player(mark)
    else:
        xs = [ idx for idx, space in enumerate(board) if space == 'X' ]
        os = [ idx for idx, space in enumerate(board) if space == 'O' ]
        empty = [ idx for idx, space in enumerate(board) if space is None ]

        space = computer_player({'xs': xs, 'os': os, 'empty': empty})
        print "The computer picks space %s" % space
        return space


def computer_player(world):

    #check if computer can win
    for spot in world['empty']:
        board[spot] = 'O'
        if win_by_diagonal('O') or win_by_horizontal('O') or win_by_vertical('O'):
            board[spot] = None
            return spot
        else:
            board[spot] = None

    #check for block human win
    for spot in world['empty']:
        board[spot] = 'X'
        if win_by_diagonal('X') or win_by_horizontal('X') or win_by_vertical('X'):
           
            board[spot] = None
            return spot
        else:
            board[spot] = None

    #2nd turn, middle X
    if len(world['xs']) == 1 and world['xs'][0] == 4:
        return 0
    

    #random move        
    space = random.choice(world['empty'])
        
    return space

        
    

# When we run the module, play with a computer
play(take_turn=with_a_computer_player)
