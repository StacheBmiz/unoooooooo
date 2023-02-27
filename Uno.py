#************************************************************************************
# Ben Heffron
# Program CardGraphicsPython
# 
# 1/11/2023
# Update:
# Program creates cards and draws them. Special cards (wild, +4, +2, skip, reverse) 
# have symbols and corner placements. Need to add plus 2 symbol and number cards to 
# corner placement. Comments indicate what each method does.
#
# 1/13/2023
# Program now is complete in displaying your cards. Numbers shown in the corners
# and +2 is finished.
#
# 1/26/2023
# Added large cards and in the process of adding numbers within them
#
# 1/28/2023
# Working on the remove and add methods and dealing with local and global variable
# issues.
#
# 1/29/2023
# Game successfully removes a card from any hand or pile, while having the option
# to add to a hand or pile. Need to work on grid for input detection and have 
# solution to the drawing problem (creates overlap on previous drawings). Issue
# with the reading of the cardC on the added card, while cardNum is reading 
# properly.
#
# 1/31/2023
# Game properly adds and removes cards from one hand to another. Updated drawing
# on canvas to accomodate deletion and redrawing. Working on player input to allow
# user to enter moves.
# 
# Update: created array for playable cards for player1. Working on redrawing cards
#
# 2/2/2023
# Game can properly redraw the hand and used pile after one move. Still working on
# user input and adjusting hand location while checking if the card is playable.
#
# 2/3/2023
# Successfully added user input to play the card that is wanted to play. Need to
# add conditional for whether the card selected is legal, and need to add event
# for draw a card.
#
# 2/6/2023
# User can successfully play a card that is the same number, color, or wild. Issue
# with inputed characters other than numbers and need to add the events of the 
# modifier cards.

# 2/10/2023
# UNO can correctly play the first move, preventing cards that are illegal from
# being played. Also if an event card is played, it will execute.

# 2/15/2023
# Game successfully plays an eligable card from an enemy hand. Needs work on event
# cards.
#
# 2/24/2023
# Can successfuully complete a full game of UNO. Need to add quality of life
# improvements, but the base game is complete.
#
# 2/29/2023
# Added indicator for whos turn it is. Pile also resets when it is at 1 card.
#
# THINGS TO CONSIDER: changing the positioning of the cards when numbers are high,
# adding a second number to be inputed if cards reach double digit, adding a method
# to choose which wild color you want, making space draw from the pile, making a
# method to draw 4 and draw 2, grouping the card colors if cards reach a certain
# number, 
#**********************************************************************************

from tkinter import *
from tkinter.ttk import *
import random
from collections import namedtuple, OrderedDict
import pdb
import tkinter.font as font
import time
import threading

main = Tk() #Creates blank window to be edited
main.title("UNO")
main.maxsize(width = 1366, height = 768)
main.minsize(width = 1366, height = 768)

# colors used for the cards
colors = {
   'rcard' : '#D72600',
   'bcard' : '#0956BF',
   'ycard' : '#ECD407',
   'gcard' : '#379711',
   'wcard' : "black",
   'bg'    : '#FF5F1F',
   'gold'  : '#FFD700',
   'lr'    : '#F70D1A'
   }

bg = Canvas(main, width = 1366, height = 768, background = colors['bg'])
#creates a list for the entire deck
cards = []
for x in range(0, 54):
   if x == 0 or x == 13 or x == 26 or x == 39:
      cards.append(x)
   elif x < 52:
      cards.append(x)
      cards.append(x)
   elif x >= 52:
      cards.append(x)
      cards.append(x)
      cards.append(x)
      cards.append(x)
      
# shuffles the cards to be relatively similar to real shuffles
random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)

# location for each player and piles
player1 = []
player2 = []
player3 = []
player4 = []
pile = []
used = []


# deals all of the cards and sets aside the rest for the pile
place = 1
for x in range(28):
   holder = cards[x]
   if place == 1:
      player1.append(holder),
   elif place == 2:
      player2.append(holder)
   elif place == 3:
      player3.append(holder)
   else:
      player4.append(holder)
      place = 0 
   place = place + 1
x = 28
for x in range(28, 108):
   pile.append(cards[x])
   
# where the cards will be created
class Card:

   def __init__(self, card, playerNum):
      self.card = card
      self.cardC = []
      self.cardNum = []
      self.graphics = []
      self.playerNum = playerNum
      x = 0
      #creates all of the cards and seperates them into card number and card color
      while x < len(self.card):
         
         # sets value for number cards (color, number)
         if self.card[x] <= 12:
            self.cardC.append('red')
            self.cardNum.append(self.card[x])
         
         elif self.card[x] <= 25:
            self.cardC.append('blue')
            if self.card[x] == 13:
               self.cardNum.append(0)
            elif self.card[x] == 14:
               self.cardNum.append(1)
            elif self.card[x] == 15:
               self.cardNum.append(2)
            elif self.card[x] == 16:
               self.cardNum.append(3)
            elif self.card[x] == 17:
               self.cardNum.append(4)
            elif self.card[x] == 18:
               self.cardNum.append(5)
            elif self.card[x] == 19:
               self.cardNum.append(6)
            elif self.card[x] == 20:
               self.cardNum.append(7)
            elif self.card[x] == 21:
               self.cardNum.append(8)
            elif self.card[x] == 22:
               self.cardNum.append(9)
            elif self.card[x] == 23:
               self.cardNum.append(10)
            elif self.card[x] == 24:
               self.cardNum.append(11)
            elif self.card[x] == 25:
               self.cardNum.append(12)
         
         elif self.card[x] <= 38:
            self.cardC.append('green')
            if self.card[x] == 26:
               self.cardNum.append(0)
            elif self.card[x] == 27:
               self.cardNum.append(1)
            elif self.card[x] == 28:
               self.cardNum.append(2)
            elif self.card[x] == 29:
               self.cardNum.append(3)
            elif self.card[x] == 30:
               self.cardNum.append(4)
            elif self.card[x] == 31:
               self.cardNum.append(5)
            elif self.card[x] == 32:
               self.cardNum.append(6)
            elif self.card[x] == 33:
               self.cardNum.append(7)
            elif self.card[x] == 34:
               self.cardNum.append(8)
            elif self.card[x] == 35:
               self.cardNum.append(9)
            elif self.card[x] == 36:
               self.cardNum.append(10)
            elif self.card[x] == 37:
               self.cardNum.append(11)
            elif self.card[x] == 38:
               self.cardNum.append(12)
               
         elif self.card[x] <= 51:
            self.cardC.append('yellow')
            if self.card[x] == 39:
               self.cardNum.append(0)
            elif self.card[x] == 40:
               self.cardNum.append(1)
            elif self.card[x] == 41:
               self.cardNum.append(2)
            elif self.card[x] == 42:
               self.cardNum.append(3)
            elif self.card[x] == 43:
               self.cardNum.append(4)
            elif self.card[x] == 44:
               self.cardNum.append(5)
            elif self.card[x] == 45:
               self.cardNum.append(6)
            elif self.card[x] == 46:
               self.cardNum.append(7)
            elif self.card[x] == 47:
               self.cardNum.append(8)
            elif self.card[x] == 48:
               self.cardNum.append(9)
            elif self.card[x] == 49:
               self.cardNum.append(10)
            elif self.card[x]== 50:
               self.cardNum.append(11)
            elif self.card[x] == 51:
               self.cardNum.append(12)
         
         # sets value for wild cards
         elif self.card[x] <= 53:
            self.cardC.append('wild')
            if self.card[x] == 52:
               self.cardNum.append(13)
            elif self.card[x] == 53:
               self.cardNum.append(14)
         x += 1
     
      #if self.playerNum == 5:
          #  self.cardC[0] = 'red'
           # self.cardNum[0] = 12
      
   # makes it possible to access the card number outside of the class
   def getCardNum(self):
      return self.cardNum
      
   def getCardNumAt(self, i):
      return self.cardNum[i]
   
   # makes it possible to access the color outside of the class
   def getCardC(self):
      return self.cardC
      
   def getCardCAt(self, i):
      return self.cardC[i]
   
   # draws the card at the location necessary
   def drawCard(self):
      if self.playerNum == 5:
         x = 700
         y = 275
      #elif self.playerNum == 6:
      else:
         h = 200
         w = 125
         x = 250
         y = 550
      i = 0
      
      xPlus = 125
         
      for p in range(7, len(self.card)):
         xPlus = xPlus - 10
      
      # iterates through the cards needed to be made and draws the card without the symbol
      while i in range(0, len(self.card)):
         plus2 = font.Font(slant = 'italic', size = '60', family = 'CabinBold')
         
         if self.playerNum == 5:
            i = len(self.card)-1
         self.graphics.append(bg.create_rectangle(x-5,y-5,x + 105, y + 155, fill = 'white'))
         if self.cardC[i] == 'red':
            self.graphics.append(bg.create_rectangle(x, y, x + 100, y + 150, outline = "black", fill = colors['rcard']))
            self.graphics.append(bg.create_oval(x+2,y+6,x+98,y+144,fill = 'white'))
            if self.cardC[i] != 'wild':
               self.graphics.append(bg.create_oval(x+5, y+10, x+95, y+140, fill = colors['rcard']))
         
         elif self.cardC[i] == 'blue':
            self.graphics.append(bg.create_rectangle(x, y, x + 100, y + 150, outline = "black", fill = colors['bcard']))
            self.graphics.append(bg.create_oval(x+2,y+6,x+98,y+144,fill = 'white'))
            if self.cardC[i] != 'wild':
               self.graphics.append(bg.create_oval(x+5, y+10, x+95, y+140, fill = colors['bcard']))
         
         elif self.cardC[i] == 'green':
            self.graphics.append(bg.create_rectangle(x, y, x + 100, y + 150, outline = "black", fill = colors['gcard']))
            self.graphics.append(bg.create_oval(x+2,y+6,x+98,y+144,fill = 'white'))
            if self.cardC[i] != 'wild':
               self.graphics.append(bg.create_oval(x+5, y+10, x+95, y+140, fill = colors['gcard']))
         
         elif self.cardC[i] == 'yellow':
            self.graphics.append(bg.create_rectangle(x, y, x + 100, y + 150, outline = "black", fill = colors['ycard']))
            self.graphics.append(bg.create_oval(x+2,y+6,x+98,y+144,fill = 'white'))
            if self.cardC[i] != 'wild':
               self.graphics.append(bg.create_oval(x+5, y+10, x+95, y+140, fill = colors['ycard']))
         else:
            
            self.graphics.append(bg.create_rectangle(x, y, x + 100, y + 150, outline = "black", fill = colors['wcard']))
            self.graphics.append(bg.create_oval(x+5, y+10, x+95, y+140, fill = 'white'))
         if self.playerNum == 1:
            yourCard.drawCardNum(i, x) 
            #if i == len(self.card)-1:
             #  yourCard.drawSelect(xPlus)
         elif self.playerNum == 5:
            usedC.drawCardNum(i,x)
         if self.playerNum != 5:
            x = x + xPlus
         i = i + 1
    
   # puts the symbols on the cards
   def drawCardNum(self, i, xA):
      if self.playerNum == 5:
         x = 750
         y = 353
         xA = 700
         yA = 275
         xI = x + 20
         yI = yA + 40
         xC = xA
         yC = yA
      elif self.playerNum == 6:
         x = 633
         y = 309
      else:
         h = 200
         w = 125
         x = xA+50
         y = 628
         yA = 550
         xI = xA+70
         yI = 590
         xC = xA
         yC = 550
         
      
      # all faunts used for numbers and symbols
      cardF = font.Font(slant = 'italic', size = '80', family = 'CabinBold')
      reverse = font.Font(slant = 'italic', size = '18', family = 'CabinBold')
      skip = font.Font(slant = 'italic', size = '100', family = 'CabinBold')
      plus2 = font.Font(slant = 'italic', size = '60', family = 'CabinBold')
      plus2M = font.Font(slant = 'italic', size = '13', family = 'CabinBold')
      wildM = font.Font(slant = 'italic', size = '12', family = 'CabinBold')
      wild = font.Font(slant = 'italic', size = '40', family = 'CabinBold')
      skipMB = font.Font(slant = 'italic', size = '26', family = 'CabinBold')
      skipMBS1 = font.Font(slant = 'italic', size = '29', family = 'CabinBold')
      skipMBS2 = font.Font(slant = 'italic', size = '23', family = 'CabinBold')
      numM = font.Font(slant = 'italic', size = '19', family = 'CabinBold')
   
      
   
      # draws the skip logos
      if self.playerNum == 5:
         i = len(self.card)-1
      
      xPlus = 125
      
      for p in range(7, len(self.card)):
         xPlus = xPlus - 10
         
      if self.cardNum[i] == 10:
         for i in range(0, 5):
            xX = xC +50
            yY = yC + 60
            if i == 0:
               xX -= 3
               yY -= 3
            elif i == 1:
               xX += 2
               yY -= 3
            elif i == 2:
               xX -= 3
               yY += 2
            elif i == 3:
               xX += 2
               yY += 2
            skipC = [ 
               xX - 23,
               yY + 10,
               xX + 26,
               yY,
               xX + 26,
               yY + 10,
               xX - 24,
               yY + 20, 
               ]
            self.graphics.append(bg.create_polygon(skipC, fill = 'black'))
         xX = xC+50
         yY = yC+60
         self.graphics.append(bg.create_text(xX-3, yY-3, font = skip, text = "o", fill = 'black'))
         self.graphics.append(bg.create_text(xX+1, yY-3, font = skip, text = "o", fill = 'black'))
         self.graphics.append(bg.create_text(xX-3, yY+1, font = skip, text = "o", fill = 'black'))
         self.graphics.append(bg.create_text(xX+1, yY+1, font = skip, text = "o", fill = 'black'))
         self.graphics.append(bg.create_polygon(skipC, fill = 'white'))
         self.graphics.append(bg.create_text(xX, yY, text = "o",font = skip, fill = 'white'))
         i = 0
         xCsave = xC
         yCsave = yC
         xC += 12
         yC += 10
         # draws the small skips
         while i in range(0,2):
            if i == 1:
               xC += 77
               yC += 123
            skipC = [ 
               xC - 23/3.2,
               yC + 10/3.2,
               xC + 26/3.2,
               yC,
               xC + 26/3.2,
               yC + 10/3.2,
               xC - 24/3.2,
               yC + 20/3.2, 
               ]
            self.graphics.append(bg.create_text(xC, yC, font = skipMBS1, text = 'o', fill = 'black'))
            self.graphics.append(bg.create_text(xC, yC, font = skipMBS2, text = 'o', fill = 'black'))
            self.graphics.append(bg.create_polygon(skipC, fill = 'white', outline = 'black'))
            self.graphics.append(bg.create_text(xC, yC, font = skipMB, text = 'o', fill = 'white'))
            i += 1
         xC = xCsave
         yC = yCsave
         
      # draws +2
      elif self.cardNum[i] == 11:
         xSave = xC
         ySave = yC
         xC += 44
         yC += 42
         self.graphics.append(bg.create_rectangle(xC+1, yC+3, xC+110/3.7+1, yC+160/3.7+6, fill = 'black'))
         self.graphics.append(bg.create_rectangle(xC+1, yC-1, xC+110/3.7+1, yC+160/3.7-1, fill = 'black'))
         self.graphics.append(bg.create_rectangle(xC-3, yC-1, xC+110/3.7-3, yC+160/3.7-1, fill = 'black'))
         self.graphics.append(bg.create_rectangle(xC-3, yC+3, xC+110/3.7-3, yC+160/3.7+6, fill = 'black'))
         
         self.graphics.append(bg.create_rectangle(xC-18, yC+28, xC+110/3.7-16, yC+160/3.7+31,fill = 'black'))
         self.graphics.append(bg.create_rectangle(xC-18, yC+24, xC+110/3.7-16, yC+160/3.7+24,fill = 'black'))
         self.graphics.append(bg.create_rectangle(xC-20, yC+24, xC+110/3.7-20, yC+160/3.7+24,fill = 'black'))
         self.graphics.append(bg.create_rectangle(xC-20, yC+28, xC+110/3.7-20, yC+160/3.7+31,fill = 'black'))
         self.graphics.append(bg.create_rectangle(xC, yC, xC+110/3.7, yC+160/3.5, outline = 'black',fill = 'white'))
         xC -=17
         yC +=25
         self.graphics.append(bg.create_rectangle(xC, yC, xC+110/3.7, yC+160/3.5, outline = 'black',fill = 'white'))
         
         # draws the corner symbols for +2
         self.graphics.append(bg.create_text(xA + 13, yA + 12, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 13, yA + 10, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 11, yA + 10, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 11, yA + 12, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 12, yA + 11, text = '+2', font = plus2M, fill = 'white'))
         
         self.graphics.append(bg.create_text(xA + 86, yA + 138, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 84, yA + 138, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 84, yA + 136, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 86, yA + 136, text = '+2', font = plus2M, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 85, yA + 137, text = '+2', font = plus2M, fill = 'white'))
         xC = xSave
         yC = ySave
      # draws reverse
      elif self.cardNum[i] == 12:
         tri1 = [
            xI,
            yI,
            xI + 20,
            yI + 20,
            xI,
            yI + 40,
            xI,
            yI + 30,
            xI-30,
            yI +30,
            xI-30,
            yI+10,
            xI,
            yI+10
            ]           
         tri2 = [
               xI-10,
               yI+50,
               xI-40,
               yI+50,
               xI-40,
               yI+60,
               xI-60,
               yI+40,
               xI-40,
               yI+20,
               xI-40,
               yI+30,
               xI-10,
               yI+30
            ]    
               # shadow to each arrow
         tri1S = [
            xI-1,
            yI-5,
            xI + 25,
            yI + 20,
            xI,
            yI + 31,
            xI-33,
            yI +31,
            xI-33,
            yI+7,
            xI-1,
            yI+7
            ]  
         tri2S = [
            xI-10,
            yI+50,
            xI-40,
            yI+50,
            xI-40,
            yI+60,
            xI-65,
            yI+40,
            xI-40,
            yI+15,
            xI-40,
            yI+28,
            xI-10,
            yI+28
            ]
         xIS = xI
         yIS = yI
         xI = xA + 20
         yI = yA + 2
         i = 0
               # draws little reverses
         while i in range(0,2):
            if i == 1:
               xI = xA + 93
               yI = yA + 128
            tri1M = [
               xI,
               yI,
               xI + 6,
               yI + 6,
               xI,
               yI + 12,
               xI,
               yI + 9,
               xI-9,
               yI +9,
               xI-9,
               yI+3,
               xI,
               yI+3
               ]           
            tri2M = [
               xI-3,
               yI+15,
               xI-12,
               yI+15,
               xI-12,
               yI+18,
               xI-18,
               yI+12,
               xI-12,
               yI+6,
               xI-12,
               yI+9,
               xI-3,
               yI+9
               ]              
            self.graphics.append(bg.create_polygon(tri1M, outline = 'black',fill = 'white'))
            self.graphics.append(bg.create_polygon(tri2M, outline = 'black',fill = 'white'))
            i = i + 1
         self.graphics.append(bg.create_polygon(tri1S, outline = 'black',fill = 'black'))
         self.graphics.append(bg.create_polygon(tri2S, outline = 'black',fill = 'black'))
         self.graphics.append(bg.create_polygon(tri1, outline = 'black',fill = 'white'))
         self.graphics.append(bg.create_polygon(tri2, outline = 'black',fill = 'white'))
         xI = xIS
         yI = yIS
      # draws the wild symbol on the card
      elif self.cardNum[i] == 13:
         self.graphics.append(bg.create_arc(xA+10, yA+15, xA+90, yA+135, fill = colors['bcard']))
         self.graphics.append(bg.create_arc(xA+10, yA+15, xA+90, yA+135, start = 90, fill = colors['rcard']))
         self.graphics.append(bg.create_arc(xA+10, yA+15, xA+90, yA+135, start = 180, fill = colors['ycard']))
         self.graphics.append(bg.create_arc(xA+10, yA+15, xA+90, yA+135, start = 270, fill = colors['gcard']))
         self.graphics.append(bg.create_text(x-3, y-3, font = wild, text = 'wild', fill = 'black'))
         self.graphics.append(bg.create_text(x+1, y-3, font = wild, text = 'wild', fill = 'black'))
         self.graphics.append(bg.create_text(x-3, y+1, font = wild, text = 'wild', fill = 'black'))
         self.graphics.append(bg.create_text(x+1, y+1, font = wild, text = 'wild', fill = 'black'))
         self.graphics.append(bg.create_text(x, y, font = wild, text = 'wild', fill = 'white'))
         self.graphics.append(bg.create_text(xA + 15, yA + 12, text = 'wild', font = wildM, fill = 'white'))
         self.graphics.append(bg.create_text(xA + 85, yA + 135, text = 'wild', font = wildM, fill = 'white'))
       
         # draws the wild +4
      elif self.cardNum[i] == 14:
         self.graphics.append(bg.create_rectangle(xA+10, yA+70, xA+35, yA+112, fill = 'black'))
         self.graphics.append(bg.create_rectangle(xA+30, yA+45, xA+55, yA+87, fill = 'black'))
         self.graphics.append(bg.create_rectangle(xA+45, yA+60, xA+70, yA+102, fill = 'black'))
         self.graphics.append(bg.create_rectangle(xA+60, yA+35, xA+85, yA+77, fill = 'black'))
         
         self.graphics.append(bg.create_rectangle(xA+12, yA+72, xA+37, yA+112, fill = colors['gcard']))
         self.graphics.append(bg.create_rectangle(xA+32, yA+47, xA+57, yA+87, fill = colors['bcard']))
         self.graphics.append(bg.create_rectangle(xA+47, yA+62, xA+72, yA+102, fill = colors['rcard']))
         self.graphics.append(bg.create_rectangle(xA+62, yA+37, xA+87, yA+77, fill = colors['ycard']))
         
         self.graphics.append(bg.create_text(xA + 12, yA + 12, text = '+4', font = plus2M, fill = 'white'))
         self.graphics.append(bg.create_text(xA + 85, yA + 135, text = '+4', font = plus2M, fill = 'white'))
      else:
         self.graphics.append(bg.create_text(x-3, y-3, font = cardF, text = self.cardNum[i], fill = 'black'))
         self.graphics.append(bg.create_text(x+1, y-3, font = cardF, text = self.cardNum[i], fill = 'black'))
         self.graphics.append(bg.create_text(x-3, y+1, font = cardF, text = self.cardNum[i], fill = 'black'))
         self.graphics.append(bg.create_text(x+1, y+1, font = cardF, text = self.cardNum[i], fill = 'black'))
         self.graphics.append(bg.create_text(x, y, font = cardF, text = self.cardNum[i], fill = 'white'))
          
         self.graphics.append(bg.create_text(xA + 12, yA + 14, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 12, yA + 12, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 10, yA + 12, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 10, yA + 14, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 11, yA + 13, text = self.cardNum[i], font = numM, fill = 'white'))
          
         self.graphics.append(bg.create_text(xA + 90, yA + 138, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 88, yA + 138, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 88, yA + 136, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 90, yA + 136, text = self.cardNum[i], font = numM, fill = 'black'))
         self.graphics.append(bg.create_text(xA + 89, yA + 137, text = self.cardNum[i], font = numM, fill = 'white'))
      
         
         if self.playerNum != 5:
            x = x + xPlus
            xA += xPlus
            xI+=xPlus
            xC += xPlus
   
   
   # draws the rest of the deck
   def drawPile(self, cards):
      bg.create_rectangle(633, 309, 733, 459, fill = 'black')
   
   # removes one card and switches it to another player or used deck
   def removeC(self, num, player):
      if len(pileC.getCardNum()) == 1 and self.playerNum == 6:
         for i in range(0, len(usedC.getCardNum())-2):
            usedC.removeC(0, 6)
      if player == 1:
         yourCard.addC(self.cardC[num], self.cardNum[num], self.card[num])
      elif player == 2:
         e2.addC(self.cardC[num], self.cardNum[num], self.card[num])
      elif player == 3:
         e3.addC(self.cardC[num], self.cardNum[num], self.card[num])
      elif player == 4:
         e4.addC(self.cardC[num], self.cardNum[num], self.card[num])
      elif player == 5:
         usedC.addC(self.cardC[num], self.cardNum[num], self.card[num])
      elif player == 6:
         pileC.addC(self.cardC[num], self.cardNum[num], self.card[num])       
      del(self.card[num])
      del(self.cardC[num])
      del(self.cardNum[num])
   # adds one card
   def addC(self, cardColor, cardNumber, baseNum):
      self.card.append(baseNum)
      if self.playerNum == 1 or self.playerNum == 6:
         self.card = sorted(self.card)
      placeHolder = Card(self.card, self.playerNum)
      self.cardC = placeHolder.getCardC()
      self.cardNum = placeHolder.getCardNum()
   
   # redraws the graphics
   def redrawGraphics(self):
      if self.playerNum == 1:
         yourCard.drawCard()
      usedC.drawCard()
   
   def deleteGraphics(self):
      for i in range(0, len(self.graphics)):
         bg.delete(self.graphics[i])
   
   # plays the card that is needed to be played
   def playC(self, whichC):
      global direction
      global turnNum
      if self.playerNum == 1:
         yourCard.removeC(whichC, 5)
      elif self.playerNum == 2:
         e2.removeC(whichC, 5)
      elif self.playerNum == 3:
         e3.removeC(whichC, 5)
      elif self.playerNum == 4:
         e4.removeC(whichC, 5)
      
      # deletes every card so it can be redrawn
      for i in range(0, len(self.graphics)):
         bg.delete(self.graphics[i])
      
      # redraws number of cards eligable for selection
      resetSelect()
      usedC.drawCard()
      
      # checks to see if the card played is an event
      if usedC.getCardCAt(len(usedC.getCardNum())-1) == 'wild':
         resetENum()
         eventModifier(usedC.getCardNumAt(len(usedC.getCardNum())-1))
         
         # redraws your hand
         yourCard.drawCard()
         resetENum()
         
      else:
         if usedC.getCardNumAt(len(usedC.getCardNum())-1) > 9:
            resetENum()
            eventModifier(usedC.getCardNumAt(len(usedC.getCardNum())-1))
         
         if direction:
            turnNum += 1
         else:
            turnNum -= 1
      
         # redraws your hand
         yourCard.drawCard()
         resetENum()
      
         checkTurnNum()
      
   def setWild(self, color): 
      self.cardC[len(self.cardC)-1] = color
    
   def callEvent(self):
      resetENum()
      eventModifier(usedC.getCardNumAt(len(usedC.getCardNum())-1))
   
   drawnC = []  
   def drawFromPile(self):
      pass
      global drawnC
      #if self.playerNum == 1:
         #RdrawnC.append(bg.create_text()
      
# plays the enemy card and if there are no legal cards, then it will draw
def playECard():
   global turnNum
   g = 0
   check1 = len(usedC.getCardC())-1
   check = True
   if turnNum == 2:
      for i in range(0, len(e2.getCardNum())):
         if usedC.getCardCAt(check1) == 'wild' or usedC.getCardCAt(check1) == e2.getCardCAt(i) or usedC.getCardNumAt(check1) == e2.getCardNumAt(i) or e2.getCardCAt(i) == 'wild':
            e2.playC(i)
            check = False
            break
         g = i+1
      if check:
         pileC.removeC(0, 2)
         resetENum()
         if direction:
            turnNum += 1
         else:
            turnNum -= 1
         checkTurnNum()
         
   elif turnNum == 3:
      for i in range(0, len(e3.getCardNum())):
         if usedC.getCardCAt(check1) == 'wild' or usedC.getCardCAt(check1) == e3.getCardCAt(i) or usedC.getCardNumAt(check1) == e3.getCardNumAt(i) or e3.getCardCAt(i) == 'wild':
            e3.playC(i)
            check = False
            break
         g = i+1
      if check:
         pileC.removeC(0, 3)
         resetENum()
         if direction:
            turnNum += 1
         else:
            turnNum -= 1
         checkTurnNum()
   
   elif turnNum == 4:
      for i in range(0, len(e4.getCardNum())):
         if usedC.getCardCAt(check1) == 'wild' or usedC.getCardCAt(check1) == e4.getCardCAt(i) or usedC.getCardNumAt(check1) == e4.getCardNumAt(i) or e4.getCardCAt(i) == 'wild':
            e4.playC(i)
            check = False
            break
         g = i+1
      if check:
         pileC.removeC(0, 4)
         resetENum()
         if direction:
            turnNum += 1
         else:
            turnNum -= 1
         checkTurnNum()
         
select = []

# draws the numbers to type for your hand to play a card
def drawSelect(xPlus):
   global select
   x = 300
   y = 500
   plus2 = font.Font(slant = 'italic', size = '60', family = 'CabinBold')
   for i in range(0, len(yourCard.getCardNum())):
      select.append(bg.create_text(x, y, text = i+1, font = plus2, fill = 'black'))
      x = x + xPlus
   select.append(bg.create_text(500, 359, text = "0", font = plus2, fill = 'black'))

# resets the numbers you can type for a card to play
def resetSelect():
   global select
   for i in range(0, len(select)):
      bg.delete(select[i])

# calls the drawSelect method so it can redraw the graphics
def callDrawSelect():
   global select
   # xplus signifies spacing for the numbers
   xPlus = 125
   for p in range(7, len(yourCard.getCardNum())):
      xPlus = xPlus - 10
   drawSelect(xPlus)

circle = []
# draws the color wheel and then accepts an input from the user
def drawWheel():
   wheelFont = font.Font(slant = 'italic', size = '75', family = 'CabinBold')
   global circle
   circle.append(bg.create_arc(525, 245, 825, 545, fill = 'blue'))
   circle.append(bg.create_arc(525, 245, 825, 545, start = 90, fill = 'red'))
   circle.append(bg.create_arc(525, 245, 825, 545, start = 180, fill = 'yellow'))
   circle.append(bg.create_arc(525, 245, 825, 545, start = 270, fill = 'green'))   
   circle.append(bg.create_text(845, 310, text = "b", font=wheelFont, fill = colors['bcard']))
   circle.append(bg.create_text(505, 310, text = "r", font=wheelFont, fill = colors['rcard']))
   circle.append(bg.create_text(505, 480, text = "y", font=wheelFont, fill = colors['ycard']))
   circle.append(bg.create_text(845, 480, text = "g", font=wheelFont, fill = colors['gcard']))
   bg.after(0, userInputW)

# checks if the user inputed character is 
def checkColor(event):
   global circle
   global direction
   global turnNum
   event = event.char
   if event == 'b' or event == 'r' or event == 'y' or event == 'g' or event == 'B' or event == 'R' or event == 'Y' or event == 'G':
      if event == 'b':
         usedC.setWild('blue')
      elif event == 'r':
         usedC.setWild('red')
      elif event == 'y':
         usedC.setWild('yellow')
      elif event == 'g':
         usedC.setWild('green')
   
      for i in range(0, len(circle)):
         bg.delete(circle[i])
      bg.after(0, usedC.drawCard)
      main.unbind('<Key>')
      
      if direction:
         turnNum += 1
      else:
         turnNum -= 1
      
      if usedC.getCardNumAt(len(usedC.getCardNum())-1) == 14:
         if direction:
            turnNum += 1
         else:
            turnNum -= 1
      
      checkTurnNum()
    
   
# deletes the color wheel so the game can continue

# allows thhe enemy to choose a color from r g b y
def chooseEColor():
   global turnNum
   global turnNum
   r = 0
   b = 0
   g = 0
   y = 0
   maxC = 'red'
   maxN = r
   if turnNum == 2:
      for i in range(0, len(e2.getCardC())):
         if e2.getCardCAt(i) == 'red':
            r += 1
         elif e2.getCardCAt(i) == 'blue':
            b += 1
         elif e2.getCardCAt(i) == 'green':
            g += 1
         elif e2.getCardCAt(i) == 'yellow':
            y += 1
   elif turnNum == 3:
      for i in range(0, len(e3.getCardC())):
         if e3.getCardCAt(i) == 'red':
            r += 1
         elif e3.getCardCAt(i) == 'blue':
            b += 1
         elif e3.getCardCAt(i) == 'green':
            g += 1
         elif e3.getCardCAt(i) == 'yellow':
            y += 1       
   elif turnNum == 4:
      for i in range(0, len(e4.getCardC())):
         if e4.getCardCAt(i) == 'red':
            r += 1
         elif e4.getCardCAt(i) == 'blue':
            b += 1
         elif e4.getCardCAt(i) == 'green':
            g += 1
         elif e4.getCardCAt(i) == 'yellow':
            y += 1
   if b > maxN:
      maxC = 'blue'
   elif g > maxN:
      maxC = 'green'
   elif y > maxN:
      maxC = 'yellow'
   usedC.setWild(maxC)
   usedC.drawCard()
   
   if direction:
      turnNum += 1
   else:
      turnNum -= 1
   
   if usedC.getCardNumAt(len(usedC.getCardNum())-1) == 14:
      if direction:
         turnNum += 1
      else:
         turnNum -= 1
   
   checkTurnNum()
       

# executes the events of the cards
def eventModifier(type):
   global turnNum
   global direction
   # does event for skip
   if type == 10:
      if direction:
         turnNum += 1
      else:
         turnNum -= 1
   
   # does event for +2
   elif type == 11:
      if direction:
         if turnNum == 4 or turnNum == 0:
            pileC.removeC(0, 1)
            pileC.removeC(0, 1)
         else: 
            pileC.removeC(0, turnNum+1)
            pileC.removeC(0, turnNum+1)
      else:
         if turnNum == 1:
            pileC.removeC(0, 4)
            pileC.removeC(0, 4)
         else: 
            pileC.removeC(0, turnNum-1)
            pileC.removeC(0, turnNum-1)
      
      if direction:
         turnNum += 1
      else: 
         turnNum -= 1
      
      if turnNum == 1 or turnNum == 5:
         yourCard.deleteGraphics()
         yourCard.drawCard()
      
      
   
   # does event for reverse
   elif type == 12:
      if direction:
         direction = False
      else: 
         direction = True
   
   # does event for wild
   elif type == 13:
      if turnNum == 1:
         drawWheel()
      else:
         chooseEColor()
   
   # does event for wild +4
   else:
      if direction:
         if turnNum == 4 or turnNum == 0:
            pileC.removeC(0, 1)
            pileC.removeC(0, 1)
            pileC.removeC(0, 1)
            pileC.removeC(0, 1)
         else: 
            pileC.removeC(0, turnNum+1)
            pileC.removeC(0, turnNum+1)
            pileC.removeC(0, turnNum+1)
            pileC.removeC(0, turnNum+1)
      else:
         if turnNum == 1:
            pileC.removeC(0, 4)
            pileC.removeC(0, 4)
            pileC.removeC(0, 4)
            pileC.removeC(0, 4)
         else: 
            pileC.removeC(0, turnNum-1)
            pileC.removeC(0, turnNum-1)
            pileC.removeC(0, turnNum-1)
            pileC.removeC(0, turnNum-1)
      if turnNum == 1:
         drawWheel()
      elif turnNum != 0:
         chooseEColor()
      
            
      
# checks if inputted number is a valid
def checkNum(event):
   global turnNum
   global direction
   event = int(event.char)
   if turnNum == 1 and event <= len(yourCard.getCardNum()): 
      if event == 0:
         pileC.removeC(0, 1)
         yourCard.deleteGraphics()
         yourCard.drawCard()
         if direction:
            turnNum += 1
         else:
            turnNum -= 1
         checkTurnNum()
         resetSelect()
         main.unbind('<Key>')
      elif usedC.getCardNumAt(len(usedC.getCardNum())-1) == yourCard.getCardNumAt(event-1) or usedC.getCardCAt(len(usedC.getCardC())-1) == yourCard.getCardCAt(event-1) or yourCard.getCardCAt(event-1) == 'wild' or usedC.getCardCAt(len(usedC.getCardNum())-1) == 'wild':
         yourCard.drawCard()
         yourCard.redrawGraphics()
         yourCard.playC(event-1) 
         main.unbind('<Key>')
         
             
   
   #elif turnNum

# allows user to input number
def userInput():
   bg.after(0, callDrawSelect)
   main.bind('<Key>', checkNum)

# allows user to input char for colorwheel   
def userInputW(): 

   main.bind('<Key>', checkColor)
   
   
   #main.unbind('<Key>')
   
# calls the methods and signifies the the starting spot to the cards
player1 = sorted(player1)
pileC = Card(pile, 6)
yourCard = Card(player1, 1)
player2 = sorted(player2)
player3 = sorted(player3)
player4 = sorted(player4)
usedC = Card(used, 5)
pileC.removeC(0, 5)

e2 = Card(player2, 2)
e3 = Card(player3, 3)
e4 = Card(player4, 4)

player1 = yourCard.getCardNum()

yourCard.drawCard()


usedC.drawCard()

# draws enemy cards and how many cards they have
eCards = []
def drawECards():
   global eCards
   unoFaunt = font.Font(slant = 'italic', size = '40', family = 'CabinBold')
   unoNum = font.Font(slant = 'italic', size = '40', family = 'CabinBold')
   
   eCards.append(bg.create_rectangle(50-7.5, 200-7.5, 200+7.5, 425+7.5, outline='black', fill = 'white'))
   eCards.append(bg.create_rectangle(50, 200, 200, 425, outline = 'white', fill = 'black'))
   eCards.append(bg.create_oval(52, 206, 197, 416, outline = 'black', fill = 'white'))
   eCards.append(bg.create_oval(58, 212, 191, 410, outline = 'black', fill = 'red'))
   eCards.append(bg.create_text(125+1, 310-3, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125+1, 310+1, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125-3, 310-3, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125-3, 310+1, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125, 310, text = 'UNO', font = unoFaunt, fill = 'white'))
   eCards.append(bg.create_text(125+1, 360+1, text = len(e4.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125+1, 360-3, text = len(e4.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125-3, 360+1, text = len(e4.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125-3, 360-3, text = len(e4.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125, 360, text = len(e4.getCardNum()), font = unoNum, fill = 'white'))
   
   
   eCards.append(bg.create_rectangle(50-7.5+550, 200-7.5-190, 200+550+7.5, 425-190+7.5, outline='black', fill = 'white'))
   eCards.append(bg.create_rectangle(50+550, 200-190, 200+550, 425-190, outline = 'white', fill = 'black'))
   eCards.append(bg.create_oval(52+550, 206-190, 197+550, 416-190, outline = 'black', fill = 'white'))
   eCards.append(bg.create_oval(58+550, 212-190, 191+550, 410-190, outline = 'black', fill = 'red'))
   eCards.append(bg.create_text(125+1+550, 310-3-190, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125+1+550, 310+1-190, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125-3+550, 310-3-190, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125-3+550, 310+1-190, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125+550, 310-190, text = 'UNO', font = unoFaunt, fill = 'white'))
   eCards.append(bg.create_text(125+1+550, 360+1-190, text = len(e3.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125+1+550, 360-3-190, text = len(e3.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125-3+550, 360+1-190, text = len(e3.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125-3+550, 360-3-190, text = len(e3.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125+550, 360-190, text = len(e3.getCardNum()), font = unoNum, fill = 'white'))
   
   
   eCards.append(bg.create_rectangle(50-7.5+1100, 200-7.5, 200+1100+7.5, 425+7.5, outline='black', fill = 'white'))
   eCards.append(bg.create_rectangle(50+1100, 200, 200+1100, 425, outline = 'white', fill = 'black'))
   eCards.append(bg.create_oval(52+1100, 206, 197+1100, 416, outline = 'black', fill = 'white'))
   eCards.append(bg.create_oval(58+1100, 212, 191+1100, 410, outline = 'black', fill = 'red'))
   eCards.append(bg.create_text(125+1+1100, 310-3, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125+1+1100, 310+1, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125-3+1100, 310-3, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125-3+1100, 310+1, text = 'UNO', font = unoFaunt, fill = 'black'))
   eCards.append(bg.create_text(125+1100, 310, text = 'UNO', font = unoFaunt, fill = 'white'))
   eCards.append(bg.create_text(125+1+1100, 360+1, text = len(e2.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125+1+1100, 360-3, text = len(e2.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125-3+1100, 360+1, text = len(e2.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125-3+1100, 360-3, text = len(e2.getCardNum()), font = unoNum, fill = 'black'))
   eCards.append(bg.create_text(125+1100, 360, text = len(e2.getCardNum()), font = unoNum, fill = 'white'))

# updates enemy card numbers
def resetENum():
   global eCards
   for i in range(0, len(eCards)):
      bg.delete(eCards[i])
   drawECards()
  
# draws the pile top card 
unoFaunt = font.Font(slant = 'italic', size = '20', family = 'CabinBold')
bg.create_rectangle(550-5,275-5,650+5,425+5, fill = 'white')
bg.create_rectangle(550,275,650,425, fill = 'black')
bg.create_oval(550+2,275+6,550+98,275+144,fill = 'white')
bg.create_oval(550+5, 275+10, 550+95, 275+140, fill = 'red')
bg.create_text(600+1, 350-2, text = 'UNO', font = unoFaunt, fill = 'black')
bg.create_text(600+1, 350+1, text = 'UNO', font = unoFaunt, fill = 'black')
bg.create_text(600-2, 350-2, text = 'UNO', font = unoFaunt, fill = 'black')
bg.create_text(600-2, 350+1, text = 'UNO', font = unoFaunt, fill = 'black')
bg.create_text(600, 350, text = 'UNO', font = unoFaunt, fill = 'white')
   
x = 700
y = 300
xT = x + 50 
yT = x +75

turnNum = 0
direction = True

# checks the first card for an event, otherwise continue normally
def checkFirst():
   global turnNum
   if usedC.getCardNumAt(0) == 14:
      usedC.playC(53)
      turnNum = turnNum + 1
   elif usedC.getCardNumAt(0) == 10:
      usedC.playC(10)
   elif usedC.getCardNumAt(0) == 11:
      usedC.playC(11)
      
   elif usedC.getCardNumAt(0) == 12:
      usedC.playC(25)
      turnNum = 1
      bg.after(0, checkTurnNum)
   else:
      turnNum = 1
      bg.after(0, checkTurnNum)



winner = []
winnerF = font.Font(weight = 'bold', size = '150', family = 'CabinBold')
winnerFe = font.Font(weight = 'bold', size = '110', family = 'CabinBold')

# ends the game if you win and recurs infinitly
def gameOver():
   winner.append(bg.create_text(700-13, 350+3, text = "YOU WIN!", font = winnerF, fill = 'black'))
   winner.append(bg.create_text(700-13, 350-5, text = "YOU WIN!", font = winnerF, fill = 'black'))
   winner.append(bg.create_text(700+3, 350+3, text = "YOU WIN!", font = winnerF, fill = 'black'))
   winner.append(bg.create_text(700+3, 350-5, text = "YOU WIN!", font = winnerF, fill = 'black'))
   winner.append(bg.create_text(700, 350, text = "YOU WIN!", font = winnerF, fill = colors['gold']))
   
   bg.after(1500, redraw)
def redraw():
   for i in range(0, len(winner)):
      bg.delete(winner[i])
   bg.after(750, gameOver)

# ends the game if you win and recurs infinitly
def gameOver2():
   winner.append(bg.create_text(700-13, 350+3, text = "PLAYER 2 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700-13, 350-5, text = "PLAYER 2 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700+3, 350+3, text = "PLAYER 2 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700+3, 350-5, text = "PLAYER 2 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700, 350, text = "PLAYER 2 WINS!", font = winnerFe, fill = colors['lr']))
   bg.after(1500, redraw2)
def redraw2():
   for i in range(0, len(winner)):
      bg.delete(winner[i])
   bg.after(750, gameOver2)    

# ends the game if you win and recurs infinitly
def gameOver3():
   winner.append(bg.create_text(700-13, 350+3, text = "PLAYER 3 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700-13, 350-5, text = "PLAYER 3 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700+3, 350+3, text = "PLAYER 3 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700+3, 350-5, text = "PLAYER 3 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700, 350, text = "PLAYER 3 WINS!", font = winnerFe, fill = colors['lr']))
   bg.after(1500, redraw3)
def redraw3():
   for i in range(0, len(winner)):
      bg.delete(winner[i])
   bg.after(750, gameOver3)        

# ends the game if you win and recurs infinitly
def gameOver4():
   winner.append(bg.create_text(700-13, 350+3, text = "PLAYER 4 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700-13, 350-5, text = "PLAYER 4 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700+3, 350+3, text = "PLAYER 4 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700+3, 350-5, text = "PLAYER 4 WINS!", font = winnerFe, fill = 'black'))
   winner.append(bg.create_text(700, 350, text = "PLAYER 4 WINS!", font = winnerFe, fill = colors['lr']))
   bg.after(1500, redraw4)
def redraw4():
   for i in range(0, len(winner)):
      bg.delete(winner[i])
   bg.after(750, gameOver4)    

# checks to see who won and calls the end game screen accordingly  
def checkWinner():
   
   if len(yourCard.getCardNum()) == 0:
      gameOver()
   elif len(e2.getCardNum()) == 0:
      gameOver2()
   elif len(e3.getCardNum()) == 0:
      gameOver3()
   elif len(e4.getCardNum()) == 0:
      gameOver4()
 
# checks to see if the game is over
def checkGame():
   if len(yourCard.getCardNum()) == 0:
      return(True)
   elif len(e2.getCardNum()) == 0:
      return(True)
   elif len(e3.getCardNum()) == 0:
      return(True)
   elif len(e4.getCardNum()) == 0:
      return(True)
   else:
      return(False)

locate = []

# draws the red dot to indicate the turn number
def drawTurnNum(turnNum):
   global locate
   if turnNum == 2:
      locate.append(bg.create_oval(1025, 250, 1125, 350, fill = 'red', outline = 'black'))
   elif turnNum == 3:
      locate.append(bg.create_oval(800, 50, 900, 150, fill = 'red', outline = 'black'))
   elif turnNum == 4:
      locate.append(bg.create_oval(250, 250, 350, 350, fill = 'red', outline = 'black'))

# resets the graphics for the turn number
def resetTurnNum():
   global locate
   for i in range(0, len(locate)):
      bg.delete(locate[i])

# checks whos turn it is and if the game is over. Allows that player to play a card
def checkTurnNum():
   global turnNum
   if checkGame() == False:
      if turnNum == 5:
         turnNum = 1
      elif turnNum == 6:
         turnNum = 2
      elif turnNum == 0:
         turnNum = 4
      elif turnNum == -1:
         turnNum = 3
      
      resetTurnNum()
      drawTurnNum(turnNum)
      
      if turnNum > 1:
         bg.after(2000, playECard)
      else:
         bg.after(0, userInput)
   else:
      checkWinner()

# draws the enemy cards
bg.after(0, drawECards)
# calls the checkFirst method after the original canvas was made
bg.after(0, checkFirst)

bg.pack()
main.mainloop()