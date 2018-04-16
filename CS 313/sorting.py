#  File: sorting.py
#  Description: This program runs several sorting functions/algorithms and times
#                them according to the list type given for best, worst, and average cases
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: April 21, 2017
#  Date Last Modified: April 21, 2017




#begin with all the code given
import random
import time
import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


##################################################################


#create a function almost sorted to return an almost sorted list
def almostSorted(alist):
    
    #make a deep copy
    newList=deepcopy(alist)

    #make 10% of the list deep swaps
    for i in range(len(newList)//10):

        #find two unique indexes
        indx1=random.randint(0,len(newList)-1)
        indx2=random.randint(0,len(newList)-1)
        while indx1==indx2:
            indx2=random.randint(0,len(newList)-1)

        #swap the two items
        temp=newList[indx2]
        newList[indx2]=newList[indx1]
        newList[indx1]=temp

    #return the almost sorted list
    return newList

#create a randomlist function to return a random list
def randomList(c):

    #make a deep copy and an empty list
    a=deepcopy(c)
    b=[]

    #for every item in the list
    for i in range(len(a)):

        #find a random item, remove it from a, and add it to b
        item=random.choice(a)
        a.remove(item)
        b.append(item)

    #return b, the randomlist
    return b

#define a reverse list function
def reverseList(c):

    #make a deepcopy of the list and a blank list
    a=deepcopy(c)
    b=[]

    #reverse the deep copy and add all the items to the return list
    a.reverse()
    for item in a:
        b.append(item)

    #return the reversed list
    return b


#define a main function
def main():

    #create variables to represent the five types of sorts
    b='b'
    s='s'
    i='i'
    m='m'
    q='q'

    #refer to teh function names in a dictionary
    funcname={b:'bubbleSort',s:'selectionsSort',i:'insertionSort',
                   m:"mergeSort",q:'quickSort'}

    #create a dictionary to hold all the times
    thistime={}

    #go through each type of listkind, random, sorted, reverse, almost sorted
    for listkind in ['Random','Sorted','Reverse','Almost sorted']:

        #add a dictionary to hold lists of the times for the functions of this listkind
        thistime[listkind]={b:[],s:[],i:[],m:[],q:[]}

        # go through all the functions
        for function in [b,s,i,m,q]:

            #refer to the timelist associated with this list kind and this function
            ntimelist=thistime[listkind][function]

            #go through the three trials of length 10,100,1000
            for n in [10,100,1000]:

                #create a list that has all the items
                regList=[i for i in range(n)]

                #if it's a random list, call the randomlist function
                if listkind=='Random':
                    myList=(randomList(regList))

                #if it's a sortedlist, pass through the original list
                elif listkind=='Sorted':
                    myList=regList

                #if it's a reversed list, pass through the reversed copy
                elif listkind=='Reverse':
                    myList=reverseList(regList)

                #if it's almost sorted, pass through an almost sorted list as myList
                elif listkind=='Almost sorted':
                    #call an almost sorted function
                    myList=almostSorted(regList)

                #create an empty time list to run the functions five times and find an average
                timelist=[]

                #go through the round five times
                for averageround in range (5):

                    #make a deep copy of the unordered list given myList
                    unordered=deepcopy(myList)


                    #determine which function to call as b,s,i,m,or q and time the time of the fucntion process
                    if function==b:
                        start_time=time.time()
                        bubbleSort(unordered)
                        end_time=time.time()
                    elif function==s:
                        start_time=time.time()
                        selectionSort(unordered)
                        end_time=time.time()
                    elif function==i:
                        start_time=time.time()
                        insertionSort(unordered)
                        end_time=time.time()
                    elif function==m:
                        start_time=time.time()
                        mergeSort(unordered)
                        end_time=time.time()
                    elif function==q:
                        start_time=time.time()
                        quickSort(unordered)
                        end_time=time.time()


                    #determine the length of time to be the end minus start time
                    length=end_time-start_time

                    #add this occurence of timelist to timelist
                    timelist.append(length)

                #find the average time of the five rounds
                averagetime=sum(timelist)/len(timelist)

                #format it to have 6 decimals
                averagetime=format(averagetime, ".6f")

                #add this average time to the ntimelist for this listkind and this function 
                ntimelist.append(averagetime)

        #print the output heading
        print('Input type =', listkind)
        print('                    avg time   avg time   avg time')
        print('   Sort function     (n=10)    (n=100)    (n=1000)')
        print('-----------------------------------------------------')

        #print the stats for all the types of functions addressed by 'letter'
        for letter in [b,s,i,m,q]:
            print(' '*(15-len(funcname[letter])),funcname[letter],end='    ')
            print(thistime[listkind][letter][0],thistime[listkind][letter][1], thistime[listkind][letter][2], sep='   ')

        #print a blank line
        print()

#call main
main()
