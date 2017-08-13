#!/bin/env python
import random
from Tkinter import *
import sys,os,time
import string

#todo
#2. handle end of game say who won
#3. cant keep hitting after a bust

MAXCARDS=10
MINCARDSLEFT=10
COMPUTERSTICK=19

def buildDeck():
	Deck=[]
	for number in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
		for suit in ["_H","_D","_S","_C"]:
			Deck.append(number+suit)
	return Deck

def buildPdict():
	pdic={}
	for number in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
		for suit in ["_H","_D","_S","_C"]:
			pdic[number+suit]="WarCardGame/%s%s.gif"%(suit[-1].lower(),number)
	return pdic

class Game:
	def __init__(self,name):
		self.name=name
		self.cheat=False
		self.root=Tk(className="BlackJack")
		self.hitbutton=Button(self.root,text="Hit",command=self.hitPlayer)
		self.hitbutton.grid(column=1,row=0)
		self.stickbutton=Button(self.root,text="Stick",command=self.stickPlayer)
		self.stickbutton.grid(column=1,row=1)
                self.problabel=Label(self.root,text="Bust Probability")
		self.problabel.grid(row=2,column=1)
		self.svBP=StringVar()
		self.svBP.set("0%")
		self.bpentry=Entry(self.root,textvariable=self.svBP)
		self.bpentry.grid(row=3,column=1)
		self.blank=PhotoImage(file="b.gif")
		self.question=PhotoImage(file="ec.gif")
		self.deck=buildDeck()
		self.playerHand=[]
		self.playerPoints=0
		self.computerPoints=0
                self.computerHand=[]
		self.playerWonCards=[]
		self.computerWonCards=[]
		self.svCCW=StringVar()
		self.svCCW.set("0")
		self.clabel=Label(self.root,text="Computer Cards Won")
		self.clabel.grid(row=0,column=0)
		self.centry=Entry(self.root,textvariable=self.svCCW)
		self.centry.grid(row=1,column=0)
		self.svPCW=StringVar()
		self.svPCW.set("0")
		self.plabel=Label(self.root,text="%s Cards Won"%self.name)
		self.plabel.grid(row=0,column=2)
		self.pentry=Entry(self.root,textvariable=self.svPCW)
		self.pentry.grid(row=1,column=2)
		self.svCCV=StringVar()
		self.svCCV.set("?")
		self.clabelv=Label(self.root,text="Computer Cards Value")
		self.clabelv.grid(row=2,column=0)
		self.centryv=Entry(self.root,textvariable=self.svCCV)
		self.centryv.grid(row=3,column=0)
		self.svPCV=StringVar()
		self.svPCV.set("?")
		self.plabelv=Label(self.root,text="%s Cards Value"%self.name)
		self.plabelv.grid(row=2,column=2)
		self.pentryv=Entry(self.root,textvariable=self.svPCV)
		self.pentryv.grid(row=3,column=2)	
		self.pdic=buildPdict()
		self.images={}
		for card in self.pdic:		
			self.images[card]=PhotoImage(file=self.pdic[card])
		self.playerCardImages=[]
		self.computerCardImages=[]
		self.playerCardItems=[]
		self.computerCardItems=[]
		for i in range(MAXCARDS):
			self.playerCardImages.append(Canvas(self.root,width=70, height=90))
			self.playerCardImages[i].grid(row=i+4,column=2)
			self.computerCardImages.append(Canvas(self.root,width=70, height=90))
			self.computerCardImages[i].grid(row=i+4,column=0)
			self.computerCardItems.append(self.computerCardImages[i].create_image(0,0,image=self.blank,anchor=NW))
			self.playerCardItems.append(self.playerCardImages[i].create_image(0,0,image=self.blank,anchor=NW))
	
	def updatebp(self):
		bc=0
		nbc=0
		for card in self.deck:
			tmp=self.playerHand + [card]
			points=self.getPoint(tmp)
			if points>=22:
				bc+=1
			else:
				nbc+=1
		bp=float(100.*bc)/(len(self.deck))
		self.svBP.set("%02.f"%bp)
	
	def hitPlayer(self):
		hits=1	
		if self.getPoint(self.playerHand) > 21:
			print("you cannot hit.  You have too many points already!")
			self.stickPlayer()			
			return
		if len(self.playerHand)==0:
			self.computerTurn()			
			hits=2
		for i in range(hits):
			self.playerHand.append(self.drawCard())
			index=len(self.playerHand)-1
			card=self.playerHand[-1]
			self.playerCardImages[index].itemconfig(self.playerCardItems[index],image=self.images[card])
		self.svPCV.set(str(self.getPoint(self.playerHand)))
		self.updatebp()

	def roundover(self):
		cpoints=str(self.getPoint(self.computerHand))
		print("Computer points: %s"%cpoints)
		self.svCCV.set(cpoints)		
		g=self.svCCV.get()
		time.sleep(1)
		self.checkWinner()
		for i in range(MAXCARDS):
			self.playerCardImages[i].itemconfig(self.playerCardItems[i],image=self.blank)
			self.computerCardImages[i].itemconfig(self.computerCardItems[i],image=self.blank)
		self.svPCV.set("?")
		self.svCCV.set("?")
		self.svBP.set("%02.f"%0)
	
	def stickPlayer(self):
		if len(self.playerHand)==0:
			print("you can't stick you have no cards!")
			self.hitPlayer()			
			return
		self.playerPoints=self.getPoint(self.playerHand)
		self.roundover()
		if len(self.deck)<MINCARDSLEFT:
			print("Game Over")
			if len(self.playerWonCards)>len(self.computerWonCards):
				print((("%s WON!!! ")%self.name)*1000)
			elif len(self.playerWonCards)<len(self.computerWonCards):
				print((("%s LOST!!! ")%self.name)*1000)
			else:
				print("TIE GAME  "*1000)
			sys.exit(0)				
		self.playerHand=[]

	def checkWinner(self):
		if self.playerPoints>21 and self.computerPoints>21:	
			print("TIE")
			self.playerWonCards.extend(self.playerHand)
			self.computerWonCards.extend(self.computerHand)
			self.svCCW.set("%d"%len(self.computerWonCards))	
			self.svPCW.set("%d"%len(self.playerWonCards))	
			return
		elif self.playerPoints>21:
			print("Computer Wins")
			self.computerWonCards.extend(self.playerHand)
			self.computerWonCards.extend(self.computerHand)
			self.svCCW.set("%d"%len(self.computerWonCards))	
			self.svPCW.set("%d"%len(self.playerWonCards))	
			return
		elif self.computerPoints>21:
			print("%s Wins"%self.name)
			self.playerWonCards.extend(self.playerHand)
			self.playerWonCards.extend(self.computerHand)
			self.svCCW.set("%d"%len(self.computerWonCards))	
			self.svPCW.set("%d"%len(self.playerWonCards))	
			return
		elif self.playerPoints>self.computerPoints:	
			print("%s Wins"%self.name)
			self.playerWonCards.extend(self.playerHand)
			self.playerWonCards.extend(self.computerHand)
			self.svCCW.set("%d"%len(self.computerWonCards))	
			self.svPCW.set("%d"%len(self.playerWonCards))	
			return
		elif self.playerPoints<self.computerPoints:	
			print("Computer Wins")
			self.computerWonCards.extend(self.playerHand)
			self.computerWonCards.extend(self.computerHand)
			self.svCCW.set("%d"%len(self.computerWonCards))	
			self.svPCW.set("%d"%len(self.playerWonCards))	
			return
		else:
			print("TIE")
			self.playerWonCards.extend(self.playerHand)
			self.computerWonCards.extend(self.computerHand)
			self.svCCW.set("%d"%len(self.computerWonCards))	
			self.svPCW.set("%d"%len(self.playerWonCards))	

	def drawCard(self):
		if len(self.deck)==0:
			print("deck empty")
		card=random.choice(self.deck)
		self.deck.remove(card)
		return card
	
	def value(self,card):
		if card[:-2] in ["2","3","4","5","6","7","8","9","10"]:
			return int(card[:-2])
		if card[:-2] in ["J","Q","K"]:
			return 10

	def better(self,p1,p2):
		if p1>21 and p2>21:
			return min(p1,p2)
		if p1>21:
			return p2
		if p2>21:
			return p1
		return max(p1,p2)

	def getPoint(self,hand):
		points=0
		numAces=0
		for card in hand:
			if card[:-2]=="A":
				numAces=numAces+1
			else:
				points=points+self.value(card)
		if numAces==0:
			return points
		else:
			 return self.better(points+numAces,points+10+numAces)

	def computerTurn(self):		
	    self.computerHand=[]
	    for i in xrange(2):
		card=self.drawCard()
		self.computerHand.append(card)
		if i==1 or self.cheat:
			self.computerCardImages[i].itemconfig(self.computerCardItems[i],image=self.images[card])
		else:
			self.computerCardImages[i].itemconfig(self.computerCardItems[i],image=self.question)	
	    points=self.getPoint(self.computerHand)
	    while points<COMPUTERSTICK:
		i=len(self.computerHand)	
		card=self.drawCard()
		self.computerHand.append(card)
		self.computerCardImages[i].itemconfig(self.computerCardItems[i],image=self.images[card])
	    	points=self.getPoint(self.computerHand)
    	    self.computerPoints=self.getPoint(self.computerHand)

	def play(self):
		self.root.mainloop()

if __name__ == "__main__":
	name=raw_input("Enter Player Name: ")
	name=name.strip()	
	g=Game(name)
	g.play()	


