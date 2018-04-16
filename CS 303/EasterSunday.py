#  File: EasterSunday.py

#  Description: This program determines what day Easter Sunday falls on in the year

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: 9/11/16

#  Date Last Modified: 9/11/16

def main():
# determine year from input
    y=eval(input("Enter year: "))
# calculate remainder a
    a=y%19
# calculate qotient b
    b=y//100
# calculate remainder c
    c=y%100
# calculate quotient d
    d=b//4
# calculate remainder e
    e=b%4
# calculate quotient g
    g=(8*b+13)//25
# calculate remainder h
    h=(19*a+b-d-g+15)%30
# calculate quotient h
    j=c//4
# calculate remainder k
    k=c%4
# calculate quotient m
    m=(a+11*h)//319
# calculate remainder r
    r=(2*e+2*j-k-h+m+32)%7
# calculate quotient n
    n=(h-m+r+90)//25
# calculate remainder p
    p=(h-m+r+n+19)%32
# print blank line
    print ()
# print statement
    if (n==3):
        print("In",y,"Easter Sunday is on",p,"March.")
    if(n==4):
        print("In",y,"Easter Sunday is on",p,"April.")
main()
