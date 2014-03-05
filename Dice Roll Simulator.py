# Listing_23-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------
# Changes by Brian Skinner - Sept, 2013

# Rolling two six-sided dice 1000 times.

import random

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#function that rolls 2 dice and returns the sum of their rolls
def roll_dice():
    die1 = random.randint(1,6) 
    die2 = random.randint(1,6) 
    return die1 + die2
   
    
for i in range(1000):
    dice_total = roll_dice()
    totals[dice_total] = totals[dice_total] + 1

#why did we skip spots 0 and 1?
print " 2 was rolled", totals[2], "times",totals[2]/5 *"="
print " 3 was rolled", totals[3], "times",totals[3]/5*"="
print " 4 was rolled", totals[4], "times",totals[4]/5*"="
print "5 was rolled", totals[5], "times",totals[5]/5*"="
print "6 was rolled", totals[6], "times",totals[6]/5*"="
print "7 was rolled", totals[7], "times",totals[7]/5*"="
print "8 was rolled", totals[8], "times",totals[8]/5*"="
print "9 was rolled", totals[9], "times",totals[9]/5*"="
print "10 was rolled", totals[10], "times",totals[10]/5*"="
print "11 was rolled", totals[11], "times",totals[11]/5*"="
print "12 was rolled", totals[12], "times",totals[12]/5*"="

