import random
digit_1 = random.randint(0,9) 
digit_3 = random.randint(1,9) * 100
digit_2 = random.randint(0,9) * 10
guesses = 0
print "I'm thinking of a 3 digit number."
answer = digit_1 + digit_2 + digit_3
player_input = "9999"


def fermi():
    global new_number
    fermis = 0
    if int(player_input[0]) == digit_3/100:
        fermis = fermis + 1
        new_number += "a"
    else:
        new_number += player_input[0]
        
    if int(player_input[1]) == digit_2/10:
        fermis = fermis + 1
        new_number += "a"
    else:
        new_number += player_input[1]
        
    if int(player_input[2]) == digit_1:
        fermis = fermis + 1
        new_number += "a"
    else:
        new_number += player_input[2]
 
    return fermis

def pico():
    picos = 0
    if new_number[0] == str(digit_1) or new_number[0] == str(digit_2/10):
        picos +=1
    if new_number[1] == str(digit_1) or new_number[1] == str(digit_3/100):
        picos +=1
    if new_number[2] == str(digit_3/100) or new_number[2] == str(digit_2/10):
        picos +=1
    return picos

def valid_input():
    input_num = raw_input("What is the number? ")
    while len(input_num) != 3:
        input_num = raw_input("What is the number? ")
    return input_num
        
while answer != int(player_input):
    player_input = valid_input() 
    guesses = guesses + 1
    new_number = ""
    f = fermi()
    p = pico()
    print "fermi " * f, "pico " * p, "bagels " * (3 - (p + f))
print "It took", guesses,"guesses until you got the answer."
