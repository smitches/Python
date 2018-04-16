#  File: CreditCard.py

#  Description: This code will test the validity of the a credit card

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: November 17, 2016

#  Date Last Modified: November 17, 2016
def is_valid(card):
    i=-1
    total=''
    sumcard=0
    while len(card)>0:
        lastdig=card[-1]
        i+=1
        if i%2==1:
            lastdig=str(2*int(lastdig))
        total+=lastdig
        card=card[:-1]
        print('total',total)
        print('card',card)
        print('lastdig',lastdig)
        print()
    for i in range(len(total)):
        sumcard+=int(total[i])
        print(sumcard)
    if sumcard%10==0:
        return True
    else:
        return False
    
def is_type(card):
    x=int(card[0])
    y=int(card[1])
    z=int(card[2])
    zz=int(card[3])
    if x==3 and (y ==4 or y==7):
        return "American Express"
    elif x==6 and ((y==0 and z==1 and zz==1)or(y==4 and z==4)or(y==5)):
        return "Discover"
    elif x==5 and (y<=5 and y>=0):
        return "MasterCard"
    elif x==4:
        return "Visa"
    else:
        return ""
def main():
    card=str(input('Enter 15 or 16-digit credit card number: '))
    print()
    if len(card)!=15 and len(card)!=16:
        print('Not a 15 or 16-digit credit card number')
    elif is_valid(card):
        print('Valid', is_type(card),'credit card number')
    else:
        print('Invalid credit card number')
main()
