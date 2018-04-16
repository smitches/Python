#  File: Spiral.py

#  Description: This will find the neighboring numbers in a spiral for a given integer and grid size

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: November 21, 2016

#  Date Last Modified: November 21, 2016

def main():
    dim=eval(input('Enter dimension: '))
    while dim==1:
        dim=eval(input('Please enter a dimension greater than 1: '))
    num=eval(input('Enter number in spiral: '))
    print()
    if dim%2==0:
        dim+=1
    grid=[]
    dims=dim**2
    if num<1 or num>dim**2:
        print('Number not in Range')
        return
    elif (dim-2)**2<num:
        print('Number on Outer Edge')
        return
    for i in range(dim):
        line=[]
        for j in range(dim):
            line.append(int('0'))
        grid.append(line)
    dims=dim**2
    c=0
    while dims>0:
        for i in range(dim):
            grid[c][(-1*(i+1))-c]=dims
            dims-=1
        for i in range(dim-1):
            grid[c+i+1][c]=dims
            dims-=1
        for i in range(dim-1):
            grid[-1*(c+1)][c+i+1]=dims
            dims-=1
        for i in range(dim-2):
            grid[-1*(c+i+2)][-1*(c+1)]=dims
            dims-=1
        dim-=2
        c+=1
    a=0
    b=0
    for line in grid:
        for column in line:
            if column==num:
                break
            b+=1
        if column==num:
            break
        a+=1
        b=0
    for line in grid:
        print (line)
    print(grid[a-1][b-1],grid[a-1][b],grid[a-1][b+1])
    print(grid[a][b-1],grid[a][b],grid[a][b+1])
    print(grid[a+1][b-1],grid[a+1][b],grid[a+1][b+1])
main()
