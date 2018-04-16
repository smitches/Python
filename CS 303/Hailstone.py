#  File: Hailstone.py

#  Description: This function goes through a process to see how many times
#  through a function a number has to go through until it ends at the number 1.

#  Student Name: Brian Smith-Eitches

#  Student UT EID: bts867

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: 9/25/16

#  Date Last Modified: 9/27/16

def main():
  start=eval(input("Enter starting number of the range: "))
  end=eval(input("Enter ending number of the range: "))
  count=0
  countmax=count
  while start>=end or start<=0 or end<=0:
    start=int(input("Enter starting number of the range: "))
    end=int(input("Enter ending number of the range: "))
  for i in range(start, end+1, 1):
    numorig=i
    while i!=1:
      if i%2==0:
        i=i//2
      elif i%2!=0:
        i=3*i+1
      count=count+1
    if count>=countmax:
        countmax=count
        num=numorig
    count=0
  print("The number", num, "has the longest cycle length of",countmax, end=".")
main()

