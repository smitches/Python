#  File: ISBN.py

#  Description: Tests validity of ISBN

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: October 31, 2016

#  Date Last Modified: October 31, 2016

def main():
    file=open("./isbn.txt", "r")
    output=open("./isbnOut.txt", "w")
    for line in file:
        a=[]
        b=[]
        sum1=0
        sum2=0
        withh=str(line)
        isbn=withh.replace('-','')
        for ch in range(10):
            if isbn[ch]=='X':
                add=10
            else:
                add=int(isbn[ch])
            sum1+=add
            sum2+=sum1
        if sum2%11==0 and sum2>0:
            valid="valid"
        else:
            valid='invalid'
        stuff=(withh[:-1])+' '*(18-len(withh))+(valid) +" \n"
        output.write(stuff)
    file.close
    output.close
main()
