#  File: LinkedLists.py
#  Description: This code converts unordered lists and ordered lists
#                   into one overarching linked list class
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: March 23, 2017
#  Date Last Modified: March 24, 2017



#initiate a class node that has all the previously defined information
class Node(object):
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data=newData
    def setNext(self,newNext):
        self.next=newNext


#developp a new Linked List class
class LinkedList:

    #initiating a list has a head pointer to none
    def  __init__(self):
        self.head=None


    #convert a linked list to a string
    def __str__ (self):
         # Return a string representation of data suitable for printing.
         #    Long lists (more than 10 elements long) should be neatly
         #    printed with 10 elements to a line, two spaces between
         #    elements

        #counter for new spacing
        elements=0
        #start at head pointer
        current=self.head
        #string is blank
        string=''

        #until the end of the linked list
        while current!=None:

            #add info to string and update current
            string+=str(current.getData())+'  '
            current=current.getNext()
            elements+=1

            #add new line character
            if elements%10==0:
                string+='\n'

        #return the string
        return string


    #point temp to where the head pointer is and replace head with temp
    def addFirst (self, item):
        # Add an item to the beginning of the list
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp


    #addLast method
    def addLast (self, item): 
        # Add an item to the end of a list

        #Node of item
        temp=Node(item)
        current=self.head
        previous=None

        #traverse through the list until you get to end
        while current!=None:
            previous=current
            current=current.getNext()

        #if list is blank, head is temp
        if previous==None:
            self.head=temp

        #otherwise set the last node to point to temp
        else:
            previous.setNext(temp)



    #create add in order method
    def addInOrder (self, item): 
        # Insert an item into the proper place of an ordered list.
        # This assumes that the original list is already properly
        #    ordered.

        #create a node of the item
        temp=Node(item)
        current=self.head
        previous=None

        #if empty list, update head
        if self.head==None:
            self.head=temp
            #end the call
            return

        #if item belongs before first item, place it there
        elif current.getData()>item:
            temp.setNext(current)
            self.head=temp
            #end the call
            return

        #traverse through the list until you go past place or hit end of list
        while current!=None and current.getData()<item:
            previous=current
            current=current.getNext()

        #place the item there by updating pointers
        previous.setNext(temp)
        temp.setNext(current)


    #find length
    def getLength (self):

        # Return the number of items in the list 
        current=self.head
        count=0
        #traverse through the list and update counter
        while current!=None:
            current=current.getNext()
            count+=1
        return count



    #search for an item
    def findUnordered (self, item):
        
        # Search in an unordered list
        #    Return True if the item is in the list, False
        #    otherwise.
        current=self.head
        found=False

        #traverse through list until found or hit end
        while not found and current!=None:
            #if found, found=True
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()

        #return whether it was found
        return found


    #find in ordered list
    def findOrdered (self, item):
        
        # Search in an ordered list
        #    Return True if the item is in the list, False
        #    otherwise.
        # This method MUST take advantage of the fact that the
        #    list is ordered to return quicker if the item is not
        #    in the list.
        current=self.head
        found=False

        #traverse through list until found or hit the end or go past location of item
        while not found and current!=None and current.getData()<=item:

            #if found, found=True
            if current.getData()==item:
                found=True

            #otherwise, continue through the list
            else:
                current=current.getNext()

        #return found
        return found

     
    #delete a node
    def delete (self, item):
        # Delete an item from an unordered list
        #    if found, return True; otherwise, return False
        current=self.head
        previous=None
        found=False

        #traverse until end or item is found
        while current!=None and not found:

            #if item is found, found=True and delete the item
            if current.getData()==item:
                found=True

                #delete item if item is first in list by updating head
                if previous==None:
                    self.head=current.getNext()
                #delete all other nodes by previous pointer to next node
                else:
                    previous.setNext(current.getNext())

            #update previous and current
            else:
                previous=current
                current=current.getNext()

        #return if command was deleted
        return found


    #create a new list in this method
    def copyList (self):
     # Return a new linked list that's a copy of the original,
     #    made up of copies of the original elements

        #start at beginning of list        
        current=self.head

        #make a new linked list for the copy
        copyList=LinkedList()

        #traverse through the list and add the new info in the last place of new list
        while current!=None:
            copyList.addLast(current.getData())
            #update current
            current=current.getNext()

        #return the copy of the list
        return copyList



    #similar concept, different order
    def reverseList (self):
     # Return a new linked list that contains the elements of the
     #    original list in the reverse order.

        #start at beginning of list
        current=self.head

        #make a new list to be the reversed copy
        revList=LinkedList()

        #traverse through the list
        while current!=None:

            #add the item at the front and continue through the list
            revList.addFirst(current.getData())
            current=current.getNext()

        #return the reversed list
        return revList



    #go through a list and order it
    def orderList (self):
     # Return a new linked list that contains the elements of the
     #    original list arranged in ascending (alphabetical) order.
     #    Do NOT use a sort function:  do this by iteratively
     #    traversing the first list and then inserting copies of
     #    each item into the correct place in the new list.


        #start at beginning
        current=self.head

        #create a new list that is to be ordered
        orderList=LinkedList()

        #traverse through the list and add the info in the right order in the new list
        while current!=None:
            orderList.addInOrder(current.getData())
            current=current.getNext()

        #return the new ordered list
        return orderList



    #see if list is ordered
    def isOrdered (self):
        # Return True if a list is ordered in ascending (alphabetical)
        #    order, or False otherwise
        
        #it is ordered if the ordered version of the list equals the original version
        return self.orderList().isEqual(self)
       

    #list is empty  or not
    def isEmpty (self):
        # Return True if a list is empty, or False otherwise

        #list is empty if head points to none        
        return self.head==None


    #create a merged list
    def mergeList (self, b):
        # Return an ordered list whose elements consist of the 
        #    elements of two ordered lists combined.

        #start at head of first list
        current=self.head

        #create a new list to be the merged copy
        mergeList=LinkedList()

        #traverse through the first list and add the info in order
        while current!=None:
            mergeList.addInOrder(current.getData())
            current=current.getNext()

        #start at head of second list
        current=b.head

        #traverse through the second list and add the info in the right order
        while current!=None:
            mergeList.addInOrder(current.getData())
            current=current.getNext()

        #return the merged list
        return mergeList

    
    #see if two lists are equal 
    def isEqual (self, b):
        # Test if two lists are equal, item by item, and return True.

        #assume equality begins with the two having the same length
        equal=(self.getLength()==b.getLength())
        current=self.head
        currentb=b.head

        #while still True and not at end of list, traverse through
        while equal and current!=None:

            #if the info is unequal, equality is false
            if current.getData()!=currentb.getData():
                equal=False

            #otherwise, continue traversing until end
            else:
                current=current.getNext()
                currentb=currentb.getNext()

        #return the equality
        return equal



    def removeDuplicates (self):
        # Remove all duplicates from a list, returning a new list.
        #    Do not change the order of the remaining elements.

        #start at head of original and create a new empty list
        current=self.head
        newList=LinkedList()

        #traverse through the list
        while current!=None:

            #see if the item is already in the new list
            if newList.findUnordered(current.getData()):
                pass

            #otherwise, add this item to the new list
            else:
                newList.addLast(current.getData())

            #update current
            current=current.getNext()

        #return the new list
        return newList






# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
