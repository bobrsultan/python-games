#!/usr/bin/python

import sys
import random

if len(sys.argv)!=3:
	print("USAGE: python guess.py num_tries MAX")
	sys.exit(0)

num_tries = int(sys.argv[1])
MAX = int(sys.argv[2])
#compute picks a number
number=random.randint(1,MAX-1)
done=0
tries=0
while(done==0 and tries<num_tries):
	guess=int(raw_input("Guess a number between 1 and %d: "%MAX))
	if guess==number:
		done=1
	if guess<number:
		print("WRONG: "+ str(guess)+" is too SMALL, try a higher number")
	if guess>number:
		print("WRONG: "+ str(guess)+" is too BIG, try a smaller number")
	tries+=1
if done==1:
	s="YOU WIN "
	print(s*100000)

else:
	print("YOU LOSE "*100000)

