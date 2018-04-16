#  File: Dice.py
#  Description: This program runs a Monte Carlo simulation
#               to show the distribution of rolls of two dice
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: January 30, 2017
#  Date Last Modified: January 30, 2017

import random

def main():
    #start psuedorandom at seet 1314
    random.seed(1314)

    #input from user how many times to run simulation
    trials=int(input("How many times do you want to roll the dice? "))
    #initiate output list
    output=[0,0,0,0,0,0,0,0,0,0,0]

    #make a loop that runs through all simulations
    for i in range(trials):
        #find values for both dice
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        #sum the two dice
        sumdice=dice1+dice2
        #find index for that sum
        sumindex=sumdice-2
        #add 1 to the list for that index
        output[sumindex]+=1
    #print the output with the totals
    print(output)

    #decide if we need to scale the output list down for the histogram
    if trials>100:
        #go through each item in the list and scale down
        for i in range(11):
            #make sure rounding is correct with '+.5'
            output[i]=int(output[i]*100/trials+.5)

    #add blank line        
    print()

    #find the height necessary for the histogram
    counter=max(output)

    #go through line by line starting from top
    for i in range(max(output)):
        #start out the histogram with the bertical line and two spaces
        print('|', end='  ')
        for i in range(11):
            #decide to print a star or a blank space and standardize spacing
            if output[i]>=counter:
                print('*', end='  ')
            else:
                print(' ', end='  ')
        #reduce the line reference as you go down a line
        counter-=1
        #go to the next line
        print()

    #print out the base of the histogram
    print('+--+--+--+--+--+--+--+--+--+--+--+-')
    print('   2  3  4  5  6  7  8  9 10 11 12')

main()
    
