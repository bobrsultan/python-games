#!/usr/bin/python

import sys
import random

number=random.randint(1,10)
done=0
tries=0
while(done==0 and tries<5):
	guess=int(raw_input("Guess a number between 1 and 10: "))
	if guess==number:
		done=1
	if guess<number:
		print(str(guess)+" is too small, try a higher number")
	if guess>number:
		print(str(guess)+" is too large, try a smaller number")
	tries+=1
if done==1:
	print("YOU WIN")
else:
	print("YOU LOSE")

