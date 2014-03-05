steps_taken = 0
number = input("Give me a number. ")
print number
while number != 1:
    if number % 2 == 0:
        number = number/2
    else:
        number = (number*3)+1
    print number
    steps_taken = steps_taken + 1
print "It took", steps_taken , "turns to get to the number 1."

