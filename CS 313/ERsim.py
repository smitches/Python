#  File: ERsim.py
#  Description: This program runs simulated ER waiting room by implementing 
#               multiple queues
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: March 9, 2017
#  Date Last Modified: March 10, 2017


#create a Queue object as defined in class
class Queue(object):
   
   def __init__(self):
      self.items = [ ]
      
   def isEmpty (self):
      return self.items == [ ]

   def enqueue (self, item):
      self.items.insert(0,item)

   def dequeue (self):
      return self.items.pop ()

   def size (self):
      return len(self.items)

   def peek (self):
      return self.items [len(self.items)-1]

   def __str__(self):
      return str(self.items)

#create a function to determine which queue gets priority
def firstQueue(Critical, Serious, Fair):

   #deem critical comes first
   if not Critical.isEmpty():
      return 'Critical'

   #deem serious comes next
   elif not Serious.isEmpty():
      return 'Serious'

   #deem fair comes after
   elif not Fair.isEmpty():
      return 'Fair'

   #deem all queues to be empty
   else:
      return 'allEmpty'

#create a function to add a line of the file into a queue
def addQueue(linelist,Critical,Serious,Fair):

   #find person's name and lcoation from the queue
   person=linelist[1]
   queue=linelist[2]

   #if the queue is critical, add the person there and print a statement
   if queue=='Critical':
      Critical.enqueue(person)
      print('>>> Add patient',person,'to Critical queue')

   #if the queue is serious, add the person there and print a statement
   elif queue=='Serious':
      Serious.enqueue(person)
      print('>>> Add patient',person,'to Serious queue')

   #if the queue is fair, add them there and print a statement
   elif queue=='Fair':
      Fair.enqueue(person)
      print(">>> Add patient '"+person+"' to Fair queue")
 
   print()
   #call the printQueues function
   printQueues(Critical,Serious,Fair)

#define  a printQueues function to display the Queues
def printQueues(Critical,Serious,Fair):
   print('   Queues are:')
   print('   Critical:',Critical)
   print('   Serious: ',Serious)
   print('   Fair:    ',Fair)

#define a treatQueue function to be called whenever there is a treat command
def treatQueue(linelist,Critical,Serious,Fair):

   #call firstQueue fucntion to determine priority
   Queue=firstQueue(Critical,Serious,Fair)

   #if the command says "Treat next"
   if linelist[1]=='next':
      #print command output
      print('>>> Treat next patient')

      #determine the next line based on priority queue. if allempty, no patients available
      if Queue=='allEmpty':
         print()
         print('   No patients in queues')
         #end the treatqueue function
         return

      #if priority is critical, serious, or fair: dequeue that person
      if Queue=='Critical':
         person=Critical.dequeue()
      elif Queue=='Serious':
         person=Serious.dequeue()
      elif Queue=='Fair':
         person=Fair.dequeue()

      #print a statment that the person is being treated
      print()
      print("   Treating '"+person+"' from",Queue,'queue')

      #print the updated, dequeued queues and end the treatQueue function
      printQueues(Critical,Serious,Fair)
      return

   #if the command says treat critical, do this
   elif linelist[1]=='Critical':

      #print command as output
      print('>>> Treat next patient on Critical queue')

      #see if the queue is empty. if it is, end the treat queue function
      if Critical.isEmpty():
         print()
         print('   No patients in queue')
         return

      #figure out what person to treat by dequeuing that queue
      person=Critical.dequeue()

      #print a statement saying the person is being treated from this queue
      print()
      print("   Treating '"+person+"' from Critical queue")

      #print the updated, dequeued queues and end the treatQueue function
      printQueues(Critical,Serious,Fair)
      return

   #if the command says treat Serious, do this
   elif linelist[1]=='Serious':

      #print command as output
      print('>>> Treat next patient on Serious queue')

      #see if the queue is empty. if it is, end the treat queue function
      if Serious.isEmpty():
         print()
         print('   No patients in queue')
         return

      #figure out what person to treat by dequeuing that queue
      person=Serious.dequeue()

      #print a statement saying the person is being treated from this queue
      print()
      print("   Treating '"+person+"' from Serious queue")
      
      #print the updated, dequeued queues and end the treatQueue function
      printQueues(Critical,Serious,Fair)
      return

   #if the command says treat Fair, do this
   elif linelist[1]=='Fair':

      #print command as output
      print('>>> Treat next patient on Fair queue')

      #see if the queue is empty. if it is, end the treat queue function
      if Fair.isEmpty():
         print()
         print('   No patients in queue')
         return

      #figure out what person to treat by dequeuing that queue
      person=Fair.dequeue()

      #print a statement saying the person is being treated from this queue
      print()
      print("   Treating '"+person+"' from Fair queue")

      #print the updated, dequeued queues and end the treatQueue function
      printQueues(Critical,Serious,Fair)
      return

   #if the command says treat all, do this
   elif linelist[1]=='all':

      #update the line list so that when recursively calling treatQueue function,
      #    we know to not print a command line as output
      linelist[1]='continuing'

      #print command as output
      print('>>> Treat all patients')

      #see if all queues are empty. if they are, end the treatqueue function
      if Queue=='allEmpty':
         print()
         print('   No patients in queues')
         return

      #see if priority queue is critical, serious or fair and determine person
      #    to treat by dequeueing that priority queue
      elif Queue=='Critical':
         person=Critical.dequeue()
      elif Queue=='Serious':
         person=Serious.dequeue()
      elif Queue=='Fair':
         person=Fair.dequeue()

      #print the output that the person is being treated
      print()
      print("   Treating '"+person+"' from",Queue,'queue')

      #print the updated, dequeued queues
      printQueues(Critical,Serious,Fair)

      #recursively call the treatqueue function
      treatQueue(linelist, Critical,Serious,Fair)

   #linelist[1] is 'continuing' after treat all was commanded
   elif linelist[1]=='continuing':

      #print a blank line
      print()

      #find priority queue and dequeue that person to be treated
      if Queue=='allEmpty':
         #print a statement when all queues are empty and end the treatQueue function
         print('   No patient in queues')
         return
      elif Queue=='Critical':
         person=Critical.dequeue()
      elif Queue=='Serious':
         person=Serious.dequeue()
      elif Queue=='Fair':
         person=Fair.dequeue()
         
      #print the output that the person is being treated
      print("   Treating '"+person+"' from",Queue,'queue')      
      printQueues(Critical,Serious,Fair)
      
      #recursively call the treatqueue function
      treatQueue(linelist, Critical,Serious,Fair)
   

#define a main function to be called later
def main():

   #create three queues to be used by ER
   Critical=Queue()
   Serious=Queue() 
   Fair=Queue()

   #open the file
   file=open('ERsim.txt','r')

   #read through each line
   for line in file:
       
      #convert the line into a list to be used later
      linelist=line.split()
      
      #not necessary, but remove new line whitespace after the line
      line=line.rstrip('\n')

      #see if command line says exit and exit program after closing the file
      if linelist[0]=='exit':
         print('>>> Exit')
         file.close()
         return

      #see if the command line says add
      elif linelist[0]=='add':

         #call the addQueue function. send over command and three queue objects
         addQueue(linelist,Critical,Serious,Fair)

      #see if command line says treat
      elif linelist[0]=='treat':
         
         #call treatQueue function. send over command line and three queue objects
         treatQueue(linelist,Critical,Serious,Fair)
      print()

   #close the file if the program does not have an exit line of command anyway
   file.close()

#call the main function
main()
