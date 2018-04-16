#  File: CalculatePI.py

#  Description: this function estimates Pi

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: October 12, 2016

#  Date Last Modified: October 13, 2016


import math
import random

def computePI(numthrows):
    counter=0
    incir=0
    while counter<numthrows:
        xPos= random.uniform (-1.0, 1.0)
        yPos= random.uniform (-1.0, 1.0)
        if math.hypot(xPos, yPos) <1:
            incir=incir+1
        counter=counter+1
    PI=4*incir/numthrows
    return PI
def main():
    print("Computation of PI using Random Numbers")
    print()
    numthrows=100
    while numthrows<=10000000:
        numthrowsb=str(numthrows)
        numthrowsp='{:10s}'.format(numthrowsb)
        estpi=computePI(numthrows)
        a="num ="
        b="Calculated PI ="
        calc="{:7.6f}".format((estpi))
        d="Difference ="
        dif="{:+7.6f}".format(estpi-math.pi)
        print(a, numthrowsp, b, calc,"  ", d, dif)
        numthrows=numthrows*10
    print()
    print("Difference = Calculated PI - math.pi")
main()
