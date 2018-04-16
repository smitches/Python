# File: Deal.py

# Description: This program simulates a game where you choose a prize behind
# three closed doors and then one is shown and you have an option to change choice

# Student Name: Brian Smith-Eitches

# Student UT EID: bts867

# Course Name: CS 303E

# Unique Number: 51195

# Date Created: October 19, 2016

# Date Last Modified: October 19, 2016
import random
def main():
    play= eval(input("Enter the number of times you want to play: "))
    print()
    print("Prize".center(10),end='')
    print("Guess".center(10),end='')
    print("View".center(10),end='')
    print("New Guess".center(10))
    countnewguess=0
    countoldguess=0
    for i in range(1,play+1):
        choice=random.randint(1,3)
        prize=random.randint(1,3)
        if prize!=choice:
            view=6-prize-choice
        elif prize==choice:
            if prize==1:
                view=random.randint(2,3)
            elif prize==2:
                view=random.randint(1,2)
                if view==2:
                    view=3
            elif prize==3:
                view=random.randint(1,2)
        newguess=6-choice-view
        print(str(prize).center(10), end='')
        print(str(choice).center(10), end='')
        print(str(view).center(10), end='')
        print(str(newguess).center(10))
        if prize==newguess:
            countnewguess+=1
        if prize==choice:
            countoldguess+=1
    print()
    print("Probability of winning if you switch =", round(countnewguess/play,2))
    print("Probability of winning if you do not switch =", round(countoldguess/play,2))
main()
