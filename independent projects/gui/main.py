import tkinter
import tkinter.messagebox
import random

class deck:
    def __init__(self):
        suit=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        one_deck=suit*4
        shoe=one_deck*6
        self.deck=shoe
    def deal_one(self):
        index=random.randint(0,len(self.deck)-1)
        return self.deck[index]

class dealer:
    def __init__(self):
        pass

class player:
    def __init__(self,bank):
        self.bank=int(bank)
    def win(self):
        self.bank+=1
    def lose(self):
        self.bank-=1
    def broke(self):
        return self.bank<=0

class start:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.top_frame=tkinter.Frame(self.main_window)
        self.middle_frame=tkinter.Frame(self.main_window)
        self.end_frame=tkinter.Frame(self.main_window)

        self.top_label=tkinter.Label(self.top_frame,text='Welcome to Blackjack!')
        self.space=tkinter.Label(self.top_frame,text='')
        self.bank_label=tkinter.Label(self.middle_frame,text='How many dollars do you have to gamble?')
        self.bank_entry=tkinter.Entry(self.middle_frame,width=4)
        self.top_label.pack()
        self.space.pack()
        self.bank_label.pack(side='left')
        self.bank_entry.pack(side='left')
        self.space2=tkinter.Label(self.end_frame,text='')
        self.space2.pack()
        self.play_button=tkinter.Button(self.end_frame,text="Let's Play!",command=self.start_game)
        self.quit_button=tkinter.Button(self.end_frame,text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='right')
        self.play_button.pack(side='right')
        self.top_frame.pack()
        self.middle_frame.pack()
        self.end_frame.pack()
        tkinter.mainloop()
        
    def start_game(self):
        self.player=player(self.bank_entry.get())
        self.dealer=dealer()
        self.deck=deck()
        self.play_game()

    def hand_value(self,myList):
        value=0
        for item in myList:
            if type(item)==str:
                if item=='A':
                    value+=11
                else:
                    value+=10
            else:
                value+=item
        if value>21:
            for i in range(myList.count('A')):
                value-=10
        return value
    
    def label_string(self, myList):
        string=''
        for item in myList:
            string+=str(item)+' '
        string+='\n'+'Total of: '+str(self.hand_value(myList))
        string+='\n'
        return string
    
    def start_round(self,dealer,player):

        self.bet_window=tkinter.Tk()
        
        self.bet_frame=tkinter.Frame(self.bet_window)
        self.bet_frame2=tkinter.Frame(self.bet_window)
        self.bet_label=tkinter.Label(self.bet_frame,text='How much are you betting?')
        self.bet_entry=tkinter.Entry(self.bet_frame, width=4)
        self.start_round_button=tkinter.Button(self.bet_frame2,text='Start Round', command=self.new_round)
        self.cashout_button=tkinter.Button(self.bet_frame2,text='Cashout',command=self.cashout)
        self.bet_label.pack(side='left')
        self.bet_entry.pack(side='left')
        self.blank=tkinter.Label(self.bet_frame2,text='')
        self.blank.pack()
        self.start_round_button.pack(side='left')
        self.cashout_button.pack(side='left')
        self.bet_frame.pack()
        self.bet_frame2.pack()
        tkinter.mainloop()

    def cashout(self):
        tkinter.messagebox.showinfo('Cashout','You leave with $'+str(self.player.bank))
        self.main_window.destroy()
        self.bet_window.destroy()

    def new_round(self):
        dealer.hand=[]
        player.hand=[]
        dealer.hand.append(self.deck.deal_one())
        dealer.hand.append(self.deck.deal_one())
        player.hand.append(self.deck.deal_one())
        player.hand.append(self.deck.deal_one())

        self.show_window()
        
    def hit(self):
        
        self.player.hand.append(self.deck.deal_one())
        self.game_window.destroy()
        self.show_window()

    def dealer_turn(self):
        while self.hand_value(self.dealer.hand)<17 and self.hand_value(self.player.hand)<22:
            self.dealer.hand.append(self.deck.deal_one())
        self.game_window.destroy()
        self.get_winner()
    def get_winner(self):
        if self.hand_value(self.player.hand)>21 or (self.hand_value(self.dealer.hand)>self.hand_value(self.player.hand) and self.hand_value(self.dealer.hand)<=21):
            tkinter.messagebox.showinfo('Round Loss', 'You lost. Dealer has'+str(self.hand_value(self.dealer.hand))+ 'and you have'+str(self.hand_value(self.player.hand)))
        else:
            tkinter.messagebox.showinfo('Round Win', 'You win! Dealer has'+str(self.hand_value(self.dealer.hand))+ 'and you have'+str(self.hand_value(self.player.hand)))
    def show_window(self):
        self.game_window=tkinter.Tk()
        self.dealer_frame=tkinter.Frame(self.game_window)
        self.player_frame=tkinter.Frame(self.game_window)
        dealer_has='Dealer has: '+self.label_string(self.dealer.hand)
        self.dealer_label=tkinter.Label(self.dealer_frame, text=dealer_has)
        player_has='Player has: '+self.label_string(self.player.hand)
        self.player_label=tkinter.Label(self.player_frame, text=player_has)
        self.hit_button=tkinter.Button(self.player_frame, text='Hit', command=self.hit)
        self.stay_button=tkinter.Button(self.player_frame,text='Stay',command=self.dealer_turn)
        self.quit_button=tkinter.Button(self.player_frame, text='Quit', command=self.game_window.destroy)
        self.dealer_label.pack()
        self.player_label.pack()
        self.hit_button.pack(side='left')
        self.stay_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.dealer_frame.pack()
        self.player_frame.pack()
        tkinter.mainloop()

        
    def play_game(self):
        self.start_round(self.dealer,self.player)
        if self.player.broke():
            self.end_game()


    def end_game(self):
        self.game_window.destroy()
        self.main_window.destroy()
        tkinter.messagebox.showinfo('Game Over', 'You have lost')

        
game=start()
