#!/usr/bin/python

import sys
import random

if len(sys.argv)!=3:
	print("USAGE: python guess.py num_tries MAX")
	sys.exit(0)

num_tries = int(sys.argv[1])
MAX = int(sys.argv[2])
#compute picks a number
number=random.randint(1,MAX)
done=False
tries=0
under=1
over=MAX
while(not done and tries<num_tries):
	guessed=False
	guess=0
	while not guessed:
		try: 
			guess=int(input("Please guess a number between %d and %d: "%(under,over)))
			guessed=True
		except:
			print("Please type a number!")
			pass
	if guess==number:
		done=1
	if guess<number:
		print("WRONG: "+ str(guess)+" is too SMALL, try a higher number")
		under=max(under,guess)
	if guess>number:
		print("WRONG: "+ str(guess)+" is too BIG, try a smaller number")
		over=min(over,guess)
	tries+=1
if done==1:
	s="YOU WIN "
	print(s*100000)

else:
	print("YOU LOSE "*100000)

