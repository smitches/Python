#  File: Day.py

#  Description: This application will return the day of the week for a given date

#  Student Name: Brian Smith-Eitches

#  Student UT EID: BTS867

#  Course Name: CS 303E

#  Unique Number: 51195

#  Date Created: September 21, 2016

#  Date Last Modified: September 21, 2016

def main():
  year=eval(input("Enter year: "))
  while year <1900 or year >2100:
    year= eval(input("Enter year: "))
  month=eval(input("Enter month: "))
  while month>12 or month<1:
    month=eval(input("Enter month: "))
  day=eval(input("Enter day: "))
  if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    while day<1 or day>31:
      day=eval(input("Enter day: "))
  if month==4 or month==6 or month==9 or month==11:
    while day<1 or day>30:
      day=eval(input("Enter day: "))
  if month==2:
    if year%4==0 and year!=1900 and year!=2100:
      while day<1 or day>29:
        day=eval(input("Enter day: "))
    if year%4!=0 or year==2100 or year==1900:
      while day<1 or day>28:
        day=eval(input("Enter day: "))
  if month>=3:
    month=month-2
  elif month==1 or month==2:
    month=month+10
    year=year-1
  a=month
  b=day
  c=year%100
  d=year//100
  w=(13*a-1)//5
  x=c//4
  y=d//4
  z=w+x+y+b+c-2*d
  r=z%7
  r=(r+7)%7
  if r==0:
    weekday='Sunday'
  if r==1:
    weekday='Monday'
  if r==2:
    weekday='Tuesday'
  if r==3:
    weekday='Wednesday'
  if r==4:
    weekday='Thursday'
  if r==5:
    weekday='Friday'
  if r==6:
    weekday='Saturday'
  print("The day is", weekday, end=('.'))
main()
