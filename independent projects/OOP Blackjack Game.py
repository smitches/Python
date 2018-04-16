import random
class card:
    def __init__(self,letter):
        try:
            self.value=int(letter)
            self.name=letter
            self.ace=False
        except:
            self.value = 10
            self.name=letter
            self.ace=False
            if letter=='A':
                self.value=11
                self.ace=True
    def __str__(self):
        return self.name #+ ' '+str(self.value) + ' '+str(self.ace)
    
class hand:
    def __init__(self,x):
        self.total=0
        self.cards=[]
        self.bust=False
        self.dealer=x
    def add(self,card):
        self.total+=card.value
        self.cards.append(card)
        if self.total>21:
            for card in self.cards:
                if card.ace==True:
                    card.ace=False
                    self.total-=10
                    return self.total
            self.bust=True
            
        return self.total
    def deal(self,card):
        self.add(card)
    def __str__(self):
        string=''
        for card in self.cards:
            string+=str(card) +' '
        string += "Hand Value:" + str(self.total)+'\n'
        return string

class deck:
    def __init__(self):
        values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cardList=[]
        for i in range(6):
            random.shuffle(values)
            for value in values:
                self.cardList.append(card(value))
        random.shuffle(self.cardList)
        
    def deal(self):
        return self.cardList.pop()

        
def main():
    myDeck = deck()
    dealerHand=hand(True)
    myHand=hand(False)
    print()
    myHand.deal(myDeck.deal())
    dealerHand.deal(myDeck.deal())
    hit='y'
    while hit =='y' and not myHand.bust:
        print("Dealer has ",dealerHand)
        myHand.deal(myDeck.deal())
        print("You have ",myHand)
        if myHand.bust:
            break
        hit = input("Hit ? 'y' or 'n' ")
    if myHand.bust:
        print('You busted, sorry')
    print()
    while dealerHand.total<17:
        dealerHand.deal(myDeck.deal())
        
    print("Dealer ends with ", dealerHand)
    print("You end with", myHand)
    if (myHand.bust):
        print("You lose")
    elif (myHand.total==dealerHand.total):
        print('You push')
    elif(myHand.total>dealerHand.total or dealerHand.bust):
        print("You win")
    else:
        print("You lose")

hit= input ("Are you ready to play?")  
play = True
while play:
    main()
    play=input("Play again? 'y' or 'n' ")=='y'
    print()











