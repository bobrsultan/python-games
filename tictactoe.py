#!/usr/bin/env python
import sys
import random
player =raw_input("Give Player Symbol: ")
comp="C"
def printboard(board):
	print(str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
	print("----------")	
	print(str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
	print("-----------")
	print(str(board[6])+" | "+str(board[7])+" | "+str(board[8]))	

def playrandom(board):
	missing=[x for x in range(9) if board[x]==0]
	move=random.randint(0,len(missing)-1)
	board[missing[move]]=comp
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
				board[move]=player
		except:	
			print("invalid move")
	return None

def winner(board):
	if board[:3]==[player,player,player] or board[3:6]==[player,player,player] or board[6:]==[player,player,player]:
		print("YOU WIN!!!!!"*10000)
		return 1
	if board[:3]==[comp,comp,comp] or board[3:6]==[comp,comp,comp] or board[6:]==[comp,comp,comp]:
		print("YOU Lose, sorry")
		return 2
	if board[::3]==[player,player,player] or board[1::3]==[player,player,player] or board[2::3]==[player,player,player]:
		print("YOU WIN!!!!!"*10000)
		return 1
	if board[::3]==[comp,comp,comp] or board[1::3]==[comp,comp,comp] or board[2::3]==[comp,comp,comp]:
		print("YOU Lose, sorry")
		return 2
	if [board[0],board[4],board[8]]==[player,player,player] or [board[2],board[4],board[6]]==[player,player,player]:
		print("YOU WIN!!!!!"*10000)
		return 1
	if [board[0],board[4],board[8]]==[comp,comp,comp] or [board[2],board[4],board[6]]==[comp,comp,comp]:
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


