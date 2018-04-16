#  File: Blackjack.py
#  Description: This simulates a blackjack game with a user interface
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 2/17/17
#  Date Last Modified: 2/24/17

import random

#create a card class
class Card:

    #initialize rank and suit instance variables for cards
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit

        #determine initial value for the cards
        try:
            #integer if 2-10
            self.value=int(rank)
        except:
            #11 if ace
            if rank=='A':
                self.value=11
            #10 if J,Q,K
            else:
                self.value=10

    #define string method to show card object
    def __str__(self):
        return str(self.rank)+str(self.suit)+' '

#define a deck class
class Deck:

    #initialize a deck to be represented with a list of cards
    def __init__(self):
        self.cardList=[]
        #make a nested loop for all cards
        for j in ['C','D','H','S']:
            for i in [2,3,4,5,6,7,8,9,10,'J','Q','K','A']:
                self.cardList.append((Card(j,i)))

    #shuffle the deck method
    def shuffle(self):
        random.shuffle(self.cardList)

    #create a string method to show the deck with proper formatting
    def __str__(self):
        deckstring=' '
        num=0
        #go through all cards in the cardList and add them to the string
        for i in self.cardList:
            deckstring+=' '*(4-len(str(i)))+str(i)
            num+=1
            #new line after 13 cards
            if num%13==0:
                deckstring+='\n '
        #return string
        return deckstring

    #define a deal one method
    def dealOne(self, other):
        a=(self.cardList.pop(0))
        other.hand.append(a)
        other.handTotal+=a.value
        #modify instance variable of ace to add one
        if a.value==11:
            other.ace+=1

#define a player class
class Player:

    #initialize hand, handTotal, ace, and bust variables
    def __init__(self):
        self.hand=[]
        self.handTotal=0
        self.ace=0
        self.bust=False

    #define a string method
    def __str__(self):
        handstring=''
        for i in self.hand:
            handstring+=str(i)+' '
        return handstring

#define a showhands function to show objects of opponent and dealer
def showHands(opponent, dealer):
    print()
    print('Dealer shows',dealer.hand[-1],'faceup')
    print('You show', opponent.hand[-1],'faceup')

#define opponentTurn function
def opponentTurn(deck,dealer,opponent):
    
    print('\nYou go first\n')

    #see if opponent has an ace    
    if opponent.ace>0:
        print('Assuming 11 points for an ace you were dealt for now.')
        if opponent.ace==2:
            opponent.handTotal-=10
            opponent.ace-=1
        
    #print hand total        
    print('You hold',opponent,'for a total of',opponent.handTotal)

    #ask user what he wants to do
    choice=int(input('1 (hit) or 2 (stay)? '))
    while choice==1 and not opponent.bust:
        print()
        deck.dealOne(opponent)
        print('Card dealt:', opponent.hand[-1])

        #see if card puts player over 21
        if opponent.handTotal>21:
            print('Over 21',end='')

            #switch ace if he has one
            if opponent.ace>0:
                print('  switching an ace from 11 points to 1')
                opponent.handTotal-=10
                #deduct ace option by 1
                opponent.ace-=1

            #else, he has busted and leave the loop
            else:
                opponent.bust=True
                print()
                break

        #stop if player gets 21
        elif opponent.handTotal==21:
            print('21!  My turn . . .')
            return

        #print totals
        print('New total: ',opponent.handTotal)
        print('\nYou hold',opponent,'for a total of',opponent.handTotal)

        #prompt user for another choice
        choice=int(input('1 (hit) or 2 (stay)? '))

    #print player's final hand
    if opponent.handTotal==21:
        print('21!  My turn . . .')
    elif opponent.bust==True:
        print('You bust, you lose.')
    else:
        print('Staying with', opponent.handTotal)

#define function dealerTurn
def dealerTurn(deck,dealer,opponent):
    
    #header for dealer's turn
    print("\nDealer's turn")
    print('Your hand:',opponent,'for a total of',opponent.handTotal)

    #see if dealer was dealt two aces
    if dealer.ace==2:
        dealer.handTotal-=10
        dealer.ace-=1
        
    print("Dealer's hand:",dealer,'for a total of',dealer.handTotal,'\n')

    #see if dealer was dealt at least one ace
    if dealer.ace>0:
        print('Assuming 11 points for an ace you were dealt for now.')

    #tell dealer to play as long as dealer and opponent have not bust and
    #the dealer has fewer points
    while not opponent.bust and dealer.handTotal<opponent.handTotal and not dealer.bust:

        #give dealer a card
        deck.dealOne(dealer)
        print('Dealer hits:',dealer.hand[-1])
        print('New total: ',dealer.handTotal,'\n')

        #see if he has more than 21 points
        if dealer.handTotal>21:
            #reduce by ten if he has an ace
            if dealer.ace>0:
                print('Over 21.  switching an ace from 11 points to 1')
                dealer.handTotal-=10
                dealer.ace-=1
                print('New total:', dealer.handTotal,'\n')
            else:
                dealer.bust=True
                break
                print('\n')

    #see who won
    if dealer.bust==True:
        print('Dealer has',dealer.handTotal,'. Dealer busts! You win.\n')
    elif dealer.handTotal>=opponent.handTotal:
        print('Dealer has the same or more points without busting. Dealer wins')
        
#run the main program
def main():
    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print('Initial Deck:')          # print heading of initial deck
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    #random.seed(50)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print('Shuffled Deck')          # print header of shuffled deck
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    dealer = Player()               # create the player:  you play for this Player
    opponent = Player()             # create the dealer:  the computer plays for this Player
    
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face down (the "hole" card)
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face up
    
    print('Deck after dealing two cards each:') #print the statement of 2 card dealt
    print(cardDeck)                             #print the new card deck
    
    showHands(opponent,dealer)      # remember not to show face down cards
    
    opponentTurn(cardDeck,dealer,opponent)     # this is where half of the hard stuff is done
    dealerTurn(cardDeck,dealer,opponent)       # this is where the other half of the hard stuff is done
    
    print ("Game over.")
    print ("Final hands:")
    print ("   Dealer:   ", dealer)
    print ("   Opponent: ", opponent)
    
main()
