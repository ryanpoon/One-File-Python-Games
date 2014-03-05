turn = "X"
turns = 0
winner = " "
print " 0 | 1 | 2 "
print "-----------"
print " 3 | 4 | 5 "
print "-----------"
print " 6 | 7 | 8 "
board = [" "," "," "," "," "," "," "," "," "]
def printboard():
    print "                                                                 "
    print  " " + board[0], "|", board[1], "|", board[2]
    print "-----------"
    print " " + board[3], "|", board[4], "|", board[5]
    print "-----------"
    print " " + board[6], "|", board[7], "|", board[8]
def checksquares(spot):
    if spot >= 9 or spot < 0 or board[spot] == "X" or board[spot] == "O":
        return False
    else:
        return True
def checkwinner():
    if (board[0] == turn and board[1] == turn and board[2] == turn) or (board[3] == turn and board[4] == turn and board[5] == turn) or (board[6] == turn and board[7] == turn and board[8] == turn) or (board[0] == turn and board[3] == turn and board[6] == turn) or (board[1] == turn and board[4] == turn and board[7] == turn) or (board[2] == turn and board[5] == turn and board[8] == turn) or (board[0] == turn and board[4] == turn and board[8] == turn) or (board[2] == turn and board[4] == turn and board[6] == turn):
       return True
    else:
        return False


#game loop
while turns != 9 and winner == " ":
    
    square_chosen = input(turn+", which spot do you chose to go to? " )
    while checksquares(square_chosen) == False:
        print "Spot taken. Enter again."
        square_chosen = input(turn + ", which spot do you chose to go to? " )
    if checksquares(square_chosen) == True:
        board[square_chosen] = turn
        printboard()
    
   
    turns = turns + 1
    
    result = checkwinner()
    if result == True:
        if turn == "X":
            print "X won."
            winner = "X"
        elif turn == "O":
            winner = "O"
            print "O won."
    
    if turn == "X":
        turn = "O"
    else:
        turn = "X"


    
