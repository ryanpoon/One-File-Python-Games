import random
import datetime

total_heads = 0
total_tails = 0
total_ties = 0
streaks_of_ten_heads = 0
streaks_of_ten_tails = 0
biggest_streak = 0
#create a function that half the time returns "heads" and half the time returns
time1 = datetime.datetime.now()
def flip_coin():
    if random.randint(1,2) == 1:
        return "heads"
    else:
        return " "
#flip 100 times
for n in range(0,10000000):
    flip = flip_coin()
    if flip == "heads":
        total_heads = total_heads + 1
        streaks_of_ten_heads = streaks_of_ten_heads + 1
        streaks_of_ten_tails = 0
    else:
        total_tails = total_tails + 1
        streaks_of_ten_tails = streaks_of_ten_tails + 1
        streaks_of_ten_heads = 0
    if total_heads == total_tails:
        total_ties = total_ties + 1
    if streaks_of_ten_heads > biggest_streak:
        biggest_streak = streaks_of_ten_heads
    else:
        if streaks_of_ten_tails > biggest_streak:
            biggest_streak = streaks_of_ten_tails
print "Heads flipped: ", total_heads
print "Tails flipped: ", total_tails
time2 = datetime.datetime.now() - time1
print "That took", time2.seconds , "seconds" 
print "There were ", total_ties, "ties"
print "The longest winning streak was", biggest_streak 
