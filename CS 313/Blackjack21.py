import random
import time
def value(a):
    if a=='A':
        return 11
    elif a=='10' or a=='J' or a=='Q' or a=='K':
        return 10
    else:
        return int(a)
def blackjack():
    bank=eval (input('How much money do you have? $'))
    decks=eval(input('How many decks are we playing with? '))
    maxbank=bank
    initbank=bank
    win=0
    push=0
    lose=0
    loserow=0
    minhand=0
    winrow=0
    doubledown=False
##    plays=eval(input("Enter number of games you are willing to play: "))
    make=eval(input("Enter number of dollars you want to win: "))+bank
    starttime=time.time()
    singlesuit=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    singledeck=singlesuit*4
    vcardsfull=singledeck*decks
    vcards=vcardsfull
    i=0
    j=0
    k=1
    maxwager=1
    minbank=100
    besthand=0
    bet=eval(input('Enter your first bet: $'))
    print()
    firstbet=bet
    tie=False
    infavor=True
    danger=False
    beglosingstreakbank=1
    while bank>0:
        if len(vcards)<100:
            vcards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4*decks
            print('SHUFFLE HAS BEEN MADE')
            print()
        print('Hand',k)
        doubledown=False
        if tie:
            pass
        elif loserow>0:
            if bet>2*firstbet:
                danger=True
                print('I am worried the bets are too high')
                if bank>beglosingstreakbank:
                    bet=firstbet
                    print("\n You broke the losing streak; reset to first bet \n")
            bet+=1
            print('we lost the last one. increase bet')
        elif winrow>0 and bet>=2:
            print('we won the last one. decrease bet')
            bet-=1
            if bet>2*firstbet:
                danger=True
                print('I am worried the bets are too high')
                if bank>beglosingstreakbank:
                    danger=False
                    bet=firstbet
                    print("\n You broke the losing streak; reset to first bet \n")
        else:
            pass
        print('Bet',bet)
        index=random.randint(0,len(vcards)-1)
        dhandu=vcards[index]
        del vcards[index]
        '''
        print('WAGER', bet, 'OF BANK', bank)
        print ('Dealers upcard is a',dhandu)'''
        index2=random.randint(0,len(vcards)-1)
        phand1=vcards[index2]
        del vcards[index2]
        index3=random.randint(0,len(vcards)-1)
        dhandd=vcards[index3]
        del vcards[index3]
        index4=random.randint(0,len(vcards)-1)
        phand2=vcards[index4]
        del vcards[index4]
        print('You have a', phand1,'and a', phand2)
        vphand1=value(phand1)
        vphand2=value(phand2)
        vdhandd=value(dhandd)
        vdhandu=value(dhandu)
        dealerhas=vdhandd+vdhandu
        playerhas=vphand1+vphand2
        totaldealer=[dhandu, dhandd]
        totalplayer=[phand1, phand2]
        if playerhas==21:
            bet=bet*1.5
        while playerhas<21:
            if dealerhas==21:
                break
            elif playerhas>=17:
                break
            elif playerhas>=13:
                if value(dhandu)<7:
                    break
                indexnext=random.randint(0,len(vcards)-1)
                addcard=vcards[indexnext]
                del vcards[indexnext]
                playerhas= playerhas+ value(addcard)
                totalplayer.extend([addcard])
            else:
                if playerhas==12:
                    if vdhandu>=7 or vdhandu<=3:
                        indexnext=random.randint(0,len(vcards)-1)
                        addcard=vcards[indexnext]
                        del vcards[indexnext]
                        playerhas= playerhas+ value(addcard)
                        totalplayer.extend([addcard])
                    elif vdhandu>=4 and vdhandu<=6:
                        break
                elif playerhas>=4 and playerhas<12:
                    if len(totalplayer)==2 and playerhas==11 or (playerhas==10 and vdhandu<9):
                        print("ATTENTION WE HAVE A DOUBLE DOWN")
                        doubledown=True
                        bet=bet*2
                        indexnext=random.randint(0,len(vcards)-1)
                        addcard=vcards[indexnext]
                        del vcards[indexnext]
                        playerhas= playerhas+ value(addcard)
                        totalplayer.extend([addcard])
                        break
                    indexnext=random.randint(0,len(vcards)-1)
                    addcard=vcards[indexnext]
                    del vcards[indexnext]
                    playerhas= playerhas+ value(addcard)
                    totalplayer.extend([addcard])
            if playerhas>21 and totalplayer.count("A")>i:
                i+=1
                playerhas-=10
            print('You draw a', addcard)
        print(totalplayer)
        print('Dealer has a downcard of', dhandd)
        while dealerhas<=17 and not(playerhas==21 and len(totalplayer)==2):
            if dealerhas==17 and totaldealer.count("A")==0:
                break
            if playerhas>21:
                break
            indexnext=random.randint(0,len(vcards)-1)
            addcard=vcards[indexnext]
            vcards.remove(addcard)
            dealerhas= dealerhas+ value(addcard)
            totaldealer.extend([addcard])
            print('Dealer draws a', addcard)
            if dealerhas>21 and totaldealer.count('A')>j:
                j+=1
                dealerhas-=10
        print(totaldealer)
        print('Dealer has', dealerhas, 'you have', playerhas, ';',end=' ')
        if bank-bet<minbank:
            minbank=bank-bet
            minhand=k
        if bet>maxwager:
            maxwager=bet
        if dealerhas>playerhas and dealerhas<22 or playerhas>21:
            print('LOSE')
            lose+=1
            tie=False
            bank-=bet
            loserow+=1
            winrow=0
            '''
            if loserow>2:
                infavor=False
            if loserow==1 and not(infavor):
                beglosingstreakbank=bank
                print('LETS END THE STREAK. WE START WITH',beglosingstreakbank)
            '''
            if bet>firstbet+2:
                beglosingstreakbank=bank
                danger=True
                print('LETS END THE STREAK. WE START WITH',beglosingstreakbank)
        elif dealerhas==playerhas and playerhas<22 and (playerhas!=21 or len(totalplayer)!=2):
            print('PUSH')
            push+=1
            tie=True
        elif (dealerhas>21 and playerhas<22) or (playerhas>dealerhas and playerhas<22) or (playerhas==21 and len(totalplayer)==2):
            print('WINNER')
            win+=1
            bank+=bet
            tie=False
            loserow=0
            winrow+=1
            '''
            if winrow>2:
                infavor=True
            '''
        if bank>maxbank:
            maxbank=bank
            besthand=k
        print("BANK IS", bank)
        if maxbank>=make:
            print('YOU LOGICALLY DECIDE TO LEAVE WITH YOUR WINNINGS')
            print()
            break
        if bank<1:
            print("Sorry... the house took all your money. Don't be so greedy!")
        print()
        k+=1
        if doubledown:
            bet=bet//2
    print('You won', win, 'out of',k, 'games, which is', format(100*win/k,'.2f')+'%')
    print('You pushed', push, 'out of',k, 'games, which is',format(100*push/k,'.2f')+'%')
    print('You lost', lose, 'out of',k, 'games, which is',format(100*lose/k,'.2f')+'%')
    print('Your max wager was', maxwager)
    print('Your min bank was', minbank, 'in hand', minhand)
    print('You leave with', bank)
    print('Your max bank was', maxbank, 'after hand', besthand)
    print()
    print('YOU PROFIT $', bank-initbank,sep='')
    totaltime=time.time()-starttime
    print("This code took", round(totaltime,4), 'seconds, which is', round(totaltime/(k),4),"seconds per hand")
               
blackjack()
