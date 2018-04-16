#  File: Friends.py
#  Description: This code simulates a 'Facebook' like program where users exist
#                  and can be friends with one another implementing unordered lists
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: April 1, 2017
#  Date Last Modified: April 7, 2017


#create a class node as described in class
class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this – saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER



#create an unordered list class as described in class
class UnorderedList ():

   def __init__(self):
      self.head = None

   def isEmpty (self):
      return self.head == None

   def add (self,item):
      # add a new Node to the beginning of an existing list
      temp = Node(item)
      temp.setNext(self.head)
      self.head = temp

   def length (self):
      current = self.head
      count = 0
      while current != None:
         count += 1
         current = current.getNext()
      return count

   def search (self,item):
      current = self.head
      found = False
      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()
      return found

   def remove (self,item):
      current = self.head
      previous = None
      found = False
      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()
      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )



#create a class user
class User():

   #initiate the user giving them a name and an empty friendlist
   def __init__(self,name):
      self.name=name
      self.friendlist=UnorderedList()

   #add friends by adding a user to the friendlist using this method
   def addFriend(self,user):
      self.friendlist.add(user)

   #query two friends to see if they are friends
   def query(self,other):

      #look in the friendlist of the user and return boolean for if user is there
      return self.friendlist.search(other)
   
   # unfriend a user by removing the user from the friendlist
   def unfriend(self,user):
      self.friendlist.remove(user)

   #return whether a user has friends if the friendlist is not empty   
   def hasFriends(self):
      return (not self.friendlist.isEmpty())

   #print friends to look as a list using a string
   def printFriends(self):

      #start at current at head of friendlist
      current=self.friendlist.head

      #initiate namestring with a left bracket
      namestring='[ '

      #traverse through the friendlist and get the name of the objects in the list
      while current!=None:

         #add the node's name to the namestring with a space
         namestring+=current.getData().name+' '

         #continue traversing by updating current pointer
         current=current.getNext()

      #end the namestring with a right bracket
      namestring+=']'

      #print the namestring
      print(namestring)




#define a userObject function to find the user's object
def userObject(unorderedlist,name):

   #start at the unordered list of users with the head pointer as current
   current=unorderedlist.head

   #flag found is false
   found=False

   #traverse through the list and see if it is in the user list
   while current!=None and not found:
      if current.getData().name==name:
         found=True
         break
      current=current.getNext()

   #if the user is in the list, return a pointer to the user object
   if found:
      return current.getData()

   #else, return a new user with this name
   else:
      return User(name)


#add a person to the user list function
def newPerson(unorderedlist,person):

   #see if the person user is in the userlist
   if unorderedlist.search(person):
      print('A person with the name',person.name,'already exists.')

   #else, it is a new user
   else:
      #add the user 'person' in the userlist
      unorderedlist.add(person)

      #print that this user's name has an account
      print(person.name,'now has an account.')



#add a friend using the userlist and two user objects
def addFriend(unorderedlist,person1,person2):

   #add flag is true
   add=True

   #person cannot friend or unfriend himself. 
   if person1.name==person2.name:
      
      print('A person cannot friend him/herself.')
      add=False
      return

   #make sure user 1 exists
   if not unorderedlist.search(person1):

      #print an error if not and update add flag
      print('A person with the name',person1.name,'does not currently exist.',end='\n    ')
      add=False

   #make sure user 2 exists
   if not unorderedlist.search(person2):

      #print an error if not and update add flag
      print('A person with the name',person2.name,'does not currently exist.')
      add=False

   #end the program if the add flag si false
   if add==False:
      return

   #see if the two are already friends and update add flag if so
   if person1.query(person2):
      print(person1.name,'and',person2.name,'are already friends.')
      add=False

   #if still adding the friends, update user's friendlists to include each other
   if add:
      
      person1.addFriend(person2)
      person2.addFriend(person1)
      
      #print a message
      print(person1.name,'and',person2.name,'are now friends.')



#unfriend two users from the userlist
def unfriend(unorderedlist, person1, person2):

   #create a delete flag as true
   delete=True

   #make sure person is not trying to unfriend himself. end program if so
   if person1.name==person2.name:
      print('A person cannot unfriend him/herself.')
      delete=False
      return

   #make sure person1 is a real user. if not, print error and update delete flag
   if not unorderedlist.search(person1):
      print('A person with the name',person1.name,'does not currently exist.',end='\n    ')
      delete=False

   #make sure person2 is a real user. if not, print error and update delete flag
   if not unorderedlist.search(person2):
      print('A person with the name',person2.name,'does not currently exist.')
      delete=False

   #see if delete says false and return if so
   if delete==False:
      return

   #make sure the two users are already friends. if not, update delete flag and print error
   if not person1.query(person2):
      print(person1.name,'and', person2.name,"aren't friends, so you can't unfriend them.")
      delete=False

   #if still deleting, use the unfriend methods for the two user objects
   if delete:
      person1.unfriend(person2)
      person2.unfriend(person1)
      print(person1.name,'and',person2.name,'are no longer friends.')


#list all friends for a user in the userlist
def listFriends(unorderedlist,person):

   #see if the user is not a valid user and return if not valid user
   if not unorderedlist.search(person):
      print('A person with the name',person.name,'does not currently exist.')
      return

   #see if the person does not have friends. if not, print statement
   if not person.hasFriends():
      print(person.name,'has no friends.')

   #else, call print frineds method
   else:
      person.printFriends()


#define query to see if two users are friends in the user list
def query(unorderedlist,person1,person2):

   #start a true query flag
   query=True

   #see if the person is trying to query himself and return if so
   if person1.name==person2.name:
      print('A person cannot query him/herself.')
      return

   #see if person one is an invalid user and updater query flag if so
   if not unorderedlist.search(person1):
      print('A person with the name',person1.name,'does not currently exist.',end='\n    ')
      query=False

   #see if person two is an invalid user and updater query flag if so
   if not unorderedlist.search(person2):
      print('A person with the name',person2.name,'does not currently exist.')
      query = False

   #see if the query flag is still true
   if not query:
      return

   #determine if the two people are friends by calling the query method
   if person1.query(person2):
      print(person1.name,'and',person2.name,'are friends.')

   #if they are not friends, print they are not friends
   else:
      print(person1.name,'and',person2.name,'are not friends.')

      

#create the main function
def main():

   #initiate a file to be opened with the data
   infile=open('FriendData.txt','r')

   #create an unorderedlist object for the userlist to store current users
   userList=UnorderedList()
   

   #read through the lines in the file
   for line in infile:
      

      #print the line with the proper formating
      line=line.rstrip('\n')
      print('-->',line,end='\n    ')


      #create a linelist as the line split into pieces
      linelist=line.split()


      #see if the first word is 'Person'
      if linelist[0]=='Person':

         #call the new person function with the proper user list and the user object
         user=userObject(userList,linelist[1])
         newPerson(userList, user)


      #see if the first word is 'Friend'
      elif linelist[0]=='Friend':

         #find the user objects of the two names
         user1=userObject(userList,linelist[1])
         user2=userObject(userList,linelist[2])

         #call the addFriend function with the two users
         addFriend(userList,user1,user2)


      #see if the first word is 'Unfriend'
      elif linelist[0]=='Unfriend':

         #find the user objects of the two names
         user1=userObject(userList,linelist[1])
         user2=userObject(userList,linelist[2])
         
         #call the unFriend function with the two users
         unfriend(userList,user1,user2)


      #see if the first word is 'List'
      elif linelist[0]=='List':

         #call the listFriends function with the user list and the user object
         user=userObject(userList,linelist[1])
         listFriends(userList,user)


      #see if the first word is 'Query'
      elif linelist[0]=='Query':

         #find the user objects of the two names
         user1=userObject(userList,linelist[1])
         user2=userObject(userList,linelist[2])
         
         #call the query function with the two users
         query(userList,user1,user2)


      #see if the first word is 'Exit'
      elif linelist[0]=='Exit':
         print('Exiting...')
         break

      #print a blank line
      print()


   #close the file
   infile.close()

#call the main function
main()
