#  File: Grid.py

#  Description: This will find the greatest product in a grid

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Partner Name: none

#  Partner UT EID: none

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: November 13, 2016

#  Date Last Modified: November 13,2016

def main():
    maxprod=1
    infile=open("./grid.txt","r")
    dim = infile.readline()
    dim=dim.strip()
    dim=int(dim)
    grid=[]
    for i in range(dim):
        row=infile.readline()
        row=row.strip()
        row=row.split()
        for j in range(dim):
            row[j]=int(row[j])
        grid.append(row)
    infile.close()
    for row in grid:
        for i in range(0, dim-3):
            prod=1
            for  j in range(i,i+4):
                prod=prod*row[j]
            if prod>maxprod:
                maxprod=prod
    for j in range(dim):
        for i in range(0,dim-3):
            prod=1
            for k in range(i, i+4):
                prod= prod*grid[k][j]
            if prod>maxprod:
                maxprod=prod
    for i in range(dim-3):
        for j in range(dim-3):
            prod=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if prod>maxprod:
                maxprod=prod
    for i in range(3,dim):
        for j in range(dim-3):
            prod=grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
            if prod>maxprod:
                maxprod=prod
    print('The greatest product is', maxprod, end='.')
main()
