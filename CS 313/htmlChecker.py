#  File: htmlChecker.py
#  Description: This program ensures that all tags
#               in an html code have the closing matches by implementing a stack
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: March 2, 2017
#  Date Last Modified: March 3, 2017

#create stack class
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def size(self):
        return(len(self.items))
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return(self.items[-1])

    def __str__ (self):
        return str(self.items)

#create taglist function to return a whole list with all tags
def getTaglist(htmlfile):
    #empty taglist created
    taglist=[]
    add=False

    #read through lines
    for line in htmlfile:
        
        #read through characters
        for ch in line:
            
            #see is character is beginning of tag
            if ch=='<':
                add=True
                #begin string
                s=''

            #find end of tag
            elif (ch=='>' or ch==' ' or ch=='\n') and add==True:
                add=False
                #add to taglist
                taglist.append(s)

            #determine name of tag
            if add==True and ch!='<':
                s+=ch

    #return taglist
    return taglist

#make main function
def main():

    #create a new stack object
    htmlstack=Stack()

    #open file
    htmlfile=open('htmlfile.txt','r')

    #print out all tags using gettaglist function
    print('List of tags: \n')
    taglist=getTaglist(htmlfile)
    print(taglist,'\n')

    #initialize validtags and exceptionlist
    VALIDTAGS=[]
    exceptionlist=['meta','br','hr']

    #read through taglist
    for item in taglist:

        #make sure it is not the closing tag
        if item[0]!='/':
            #see if needs to be added to validtags list
            if item not in VALIDTAGS:
                VALIDTAGS.append(item)
                print('New tag',item,'found and added to list of valid tags')

            #see if item is not an exception and is needed in stack
            if item not in exceptionlist:
                htmlstack.push(item)
                print('Tag '+item+' pushed: stack is now', htmlstack)

            #else, tag is an exception and does not get pushed on stack
            else:
                print('Tag '+item+' does not need to match: stack is still',htmlstack)

        #else, item is a closing tag
        else:

            #make sure stack is not empty
            if htmlstack.isEmpty():
                print('Error. stack is empty but we are trying to remove tag',item)
                return

            #make sure the closing tag matches the top of stack
            if item[1:]==htmlstack.peek():
                #pop top element of stack
                htmlstack.pop()
                print('Tag',item,'matches top of stack: stack is now',htmlstack)

            #else, tag does not match the top of the stack
            else:
                print('Error: tag is '+item[1:]+' but top of stack is',htmlstack.peek())
                return

    #make sure stack is empty at end
    if htmlstack.isEmpty():
        print('\nProcessing complete. No mismatches found.')

    #else, there are unmatched tags still on stack
    else:
        print('\nProcessing complete. Unmatched tags remain on stack:',htmlstack)

    #sort validtags and exceptionlist
    VALIDTAGS.sort()
    exceptionlist.sort()

    #print out validtags and exceptionlist
    print('\nSorted Valid Tags are:\n',VALIDTAGS)
    print('\nSorted Exceptions List is:\n',exceptionlist)

    #close the file
    htmlfile.close()

#call the main function
main()
