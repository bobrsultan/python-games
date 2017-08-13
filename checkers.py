#!/bin/env python
import random
from itertools import product
#todo  1.  kings
#      2.  double jumps 
#      3.  triple or more jumps
#      4. how to be smart

class Board:
	def __init__(self):
		self.board = self.makeBoard()
	def makeBoard(self):
		board={}
		#make an empty board
		for row,col in product(xrange(8),repeat=2):
			board[(row,col)]=" "
		#fill it in
		whitepositions=[(0,0),(2,0),(1,1),(0,2),(2,2),(1,3),(0,4),(2,4),(1,5),(0,6),(2,6),(1,7)]
		for position in whitepositions:
			board[position]="W"
		blackpositions=[(6,0),(5,1),(7,1),(6,2),(7,3),(5,3),(6,4),(5,5),(7,5),(6,6),(7,7),(5,7)]
		for position in blackpositions:
			board[position]="B"           
		return board
	def onboard(self,rc):
		if 0<=rc[0]<=7 and 0<=rc[1]<=7:
			return True
		return False
	def blackjumps(self):
		jumps=[]
		for row,col in product(xrange(8),repeat=2):
			if self.board[(row,col)]=="B":
				if self.onboard((row-1,col+1)) and self.onboard((row-2,col+2)):	
					if self.board[(row-1,col+1)]=="W" and self.board[(row-2,col+2)]==" ":
						jumps.append(((row,col),(row-1,col+1),(row-2,col+2)))
				if self.onboard((row-1,col-1)) and self.onboard((row-2,col-2)):		
					if self.board[(row-1,col-1)]=="W" and self.board[(row-2,col-2)]==" ":
						jumps.append(((row,col),(row-1,col-1),(row-2,col-2)))
		return jumps	
	def whitejumps(self):
		jumps=[]
		for row,col in product(xrange(8),repeat=2):
			if self.board[(row,col)]=="W":	
				if self.onboard((row+1,col+1)) and self.onboard((row+2,col+2)):	
					if self.board[(row+1,col+1)]=="B" and self.board[(row+2,col+2)]==" ":
						jumps.append(((row,col),(row+1,col+1),(row+2,col+2)))
				if self.onboard((row+1,col-1)) and self.onboard((row+2,col-2)):	
					if self.board[(row+1,col-1)]=="B" and self.board[(row+2,col-2)]==" ":
						jumps.append(((row,col),(row+1,col-1),(row+2,col-2)))
		return jumps	
	def whitemove(self):
		moves=[]
		for row,col in product(xrange(8),repeat=2):
			if self.board[(row,col)]=="W":
				possible_moves=[(row+1,col-1),(row+1,col+1)]
				possible_moves=[x for x in possible_moves if self.onboard(x)]
				for move in possible_moves:
					if self.board[move]==" ":
						moves.append(((row,col),move))
		return moves	
	def blackmove(self):
		moves=[]
		for row,col in product(xrange(8),repeat=2):
			if self.board[(row,col)]=="B":
				possible_moves=[(row-1,col-1),(row-1,col+1)]
				possible_moves=[x for x in possible_moves if self.onboard(x)]
				for move in possible_moves:
					if self.board[move]==" ":
						moves.append(((row,col),move))
		return moves	
	def dojump(self,color,jump):
		self.board[jump[0]]=" "
		self.board[jump[1]]=" "
		self.board[jump[2]]=color
	def domove(self,color,move):
		self.board[move[0]]=" "
		self.board[move[1]]=color

	def random_black_move(self):
		moves=self.blackmove()
		move=random.choice(moves)
		self.domove("B",move)
	def random_white_move(self):
		moves=self.whitemove()
		move=random.choice(moves)
		self.domove("W",move)
	def white_turn(self):
		jumps=self.whitejumps()
		if jumps:
			self.dojump("W",random.choice(jumps))	
			return True
		moves=self.whitemove()
		if moves:
			self.domove("W",random.choice(moves))	
			return	True							
		return False
	def black_turn(self):
		jumps=self.blackjumps()
		if jumps:
			self.dojump("B",random.choice(jumps))	
			return True
		moves=self.blackmove()
		if moves:
			self.domove("B",random.choice(moves))	
			return	True							
		return False

	def __repr__(self):	
		line="---------------------------------"		
		s=""
		s+=line
		s+="\n"
		for row in xrange(8):				
			s+="|"
			for col in xrange(8):
				s+=" %s |"%self.board[(row,col)]
			s+="\n"
			s+=line
			s+="\n"
		return s	
