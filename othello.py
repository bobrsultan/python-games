import random
import sys
import copy
#working a little
# to do
# show all moves
#say who won
#say the winner at the end
#add some good cheats (let you go in the corner?) or go twice
#also add an undo

class Board():
    def __init__(self):
        self.positions=[[" "for i in xrange(8)] for j in xrange(8)]
	self.setup()
    def setup(self):
	self.positions[3][3]="W"
        self.positions[3][4]="B"
	self.positions[4][3]="B"
        self.positions[4][4]="W"
    def __repr__(self):
        s="   0   1   2   3   4   5   6   7  \n" 
	s+="  --------------------------------\n"	
        for r in xrange(8):
	    s+=str(r)+"|"
            for c in xrange(8):
                s+=(" %s |"%self.positions[r][c])
            s+=str(r)+"\n  --------------------------------\n"
        s+="   0   1   2   3   4   5   6   7  \n"
        return s


def in_bounds(row,col):
	if row>7 or row<0 or col>7 or col<0:
		return False
	return True

def legal_move(board, row,col,letter, opp_letter):
	if board.positions[row][col]!=" ":
		return False,[]
	legal=False
	to_flip=[]
	for xinc,yinc in [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,-1),(-1,1)]:
		x=row+xinc
		y=col+yinc
		count=0
		while in_bounds(x,y) and board.positions[x][y]=="%c"%opp_letter:
			x+=xinc
			y+=yinc
			count+=1
		if count==0:
			#print(count,xinc,yinc)
			continue
		if in_bounds(x,y) and board.positions[x][y]=="%c"%letter:
			xtemp=x
			ytemp=y
			legal=True
			while count>=0:
				to_flip.append((xtemp,ytemp))
				xtemp-=xinc
				ytemp-=yinc
				count-=1
	if legal:
		to_flip.append((row,col))	
	return legal,to_flip

def find_all_moves(board,letter,opp_letter):
	moves=[]
	for r in xrange(8):	
		for c in xrange(8):
			if legal_move(board,r,c,letter,opp_letter)[0]:
				moves.append((r,c))
	return moves

def make_a_move(board, row,col,letter, opp_letter):
	l=legal_move(board, row,col,letter, opp_letter)
	if l[0]:
		for x,y in l[1]:
			board.positions[x][y]="%c"%letter
		return True
	return False

def count_points(b):
	bpoints=0
	wpoints=0
	for r in xrange(8):	
		for c in xrange(8):
			if b.positions[r][c]=="B":
				bpoints+=1
			if b.positions[r][c]=="W":
				wpoints+=1
	print("B has %d points; W has %d points"%(bpoints,wpoints))
	return  

def game_over(board):
	if find_all_moves(board,"B","W")==[] and find_all_moves(board,"W","B")==[]:
		return True
	return False

def get_winner(b):
	bpoints=0
	wpoints=0
	for r in xrange(8):	
		for c in xrange(8):
			if b.positions[r][c]=="B":
				bpoints+=1
			if b.positions[r][c]=="W":
				wpoints+=1
	if bpoints>wpoints:
		print("BLACK WINS!!!!!"*1000)
	if wpoints>bpoints:
		print("WHITE WINS!!!!!"*1000)
	if bpoints==wpoints:	
		print("TIE!!")
	

def show_moves(b,letter,opp_letter):	
	m=find_all_moves(b,letter,opp_letter)
	return m

def play(cheat_corner=False,cheat_twice=False):
	b=Board()
	gameover=False
	if cheat_corner:
		b.positions[0][0]="B"
		b.positions[7][0]="B"
		b.positions[0][7]="B"
		b.positions[7][7]="B"
	if cheat_twice:	
		made_move=False
		while not made_move:
			print(b)
			count_points(b)
			try:
				print("Valid moves are: "+str(find_all_moves(b,"B","W")))
				m = raw_input("Make a move: ")
				r,c = m.split(",")
				r=int(r)
				c=int(c)
				l=legal_move(b,r,c,"B","W")
				if l[0]:
					make_a_move(b,r,c,"B","W")
					made_move=True
			except:
				pass
	while not gameover:
		can_move=find_all_moves(b,"B","W")
		made_move=False
		while can_move and not made_move:
			print(b)
			count_points(b)
			try:
				print("Valid moves are: "+str(find_all_moves(b,"B","W")))
				m = raw_input("Make a move: ")
				r,c = m.split(",")
				r=int(r)
				c=int(c)
				l=legal_move(b,r,c,"B","W")
				if l[0]:
					make_a_move(b,r,c,"B","W")
					made_move=True
			except:
				pass
		made_move=False
		can_move=find_all_moves(b,"W","B")
		while can_move and not made_move:
			r,c = random.choice(find_all_moves(b,"W","B"))
			make_a_move(b,r,c,"W","B")
			made_move=True
		gameover=game_over(b)
	print(b)	
	get_winner(b)
        count_points(b)

if __name__=="__main__":
	if len(sys.argv)>1:
		if sys.argv[1]=="corner":						
			play(cheat_corner=True)
		if sys.argv[1]=="twice":						
			play(cheat_twice=True)
	else:
		play()	
