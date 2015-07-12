#!/usr/bin/env python

import random

def printboard(board):
	print(str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
	print("----------")	
	print(str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
	print("-----------")
	print(str(board[6])+" | "+str(board[7])+" | "+str(board[8]))	

def playrandom(board):
	missing=[x for x in range(9) if board[x]==0]
	move=random.randint(0,len(missing)-1)
	board[missing[move]]=2
	return None

def getmove(board):
	printboard([x for x in range(9)])
	print('')
	done=0
	while(done==0):
		x=raw_input("enter a move: ")
		try: 
			move=int(x)
			if board[move]==0:
				done=1
				board[move]=1	
		except:	
			print("invalid move")
	return None

def winner(board):
	if board[:3]==[1,1,1] or board[3:6]==[1,1,1] or board[6:]==[1,1,1]:
		print("YOU WIN!!!!!")
		return 1
	if board[:3]==[2,2,2] or board[3:6]==[2,2,2] or board[6:]==[2,2,2]:
		print("YOU Lose, sorry")
		return 2
	if board[::3]==[1,1,1] or board[1::3]==[1,1,1] or board[2::3]==[1,1,1]:
		print("YOU WIN!!!!!")
		return 1
	if board[::3]==[2,2,2] or board[1::3]==[2,2,2] or board[2::3]==[2,2,2]:
		print("YOU Lose, sorry")
		return 2
	if [board[0],board[4],board[8]]==[1,1,1] or [board[2],board[4],board[6]]==[1,1,1]:
		print("YOU WIN!!!!!")
		return 1
	if [board[0],board[4],board[8]]==[2,2,2] or [board[2],board[4],board[6]]==[2,2,2]:
		print("YOU Lose, sorry")
		return 2
	missing=[x for x in range(9) if board[x]==0]
	if len(missing)==0:
		print("TIE GAME")
		return 1.5
	return 0

board=[0 for x in range(9)]
printboard(board)
print(' ')
while(winner(board)==0):
	getmove(board)
	printboard(board)
	print(' ')
	print(' ')
	if winner(board)==0:
		playrandom(board)
		printboard(board)
                print(' ')
	        print(' ')	


