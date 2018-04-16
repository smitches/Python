#  File: MultiwayTree.py
#  Description: This programs looks at two Multiway Trees and determines if they have the same structure
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: April 27, 2017
#  Date Last Modified: April 28, 2017



#create a class of multiway trees
class MultiwayTree:


    #initialize the instance with a list object
    def __init__(self,pyTree):

        #the root is the first element
        self.root=pyTree[0]

        #the childlist contains all the children. they all exist as the second item
        self.childlist=[]

        #iterate through each item in the second item of the list(all the children)
        for child in pyTree[1]:

            #add the multiway tree object of the child into the childlist
            self.childlist.append(MultiwayTree(child))




    #make a command of preOrder that will print out the node and pointer 
    def preOrder(self):  #print out the node-and-pointer representation of a tree using preorder.

        #print the tree
        print(self)

    #create a __str__ method to read through everything in preorder
    def __str__(self):

        #string starts with a root
        string=str(self.root)

        #then add all the children and return the string
        for child in self.childlist:
            string+=' '+str(child)
        return string



        
    #create isIsomorphic method to see if two trees have the same structure
    def isIsomorphicTo(self,other):  #return True if the tree "self" has the same structure as the
 #            tree "other", "False" otherwise.

        #if the two objects have different amounts of children, not isomorphic
        if len(self.childlist)!=len(other.childlist):

            #return False if so
            return False

        #see if the roots are both empty lists or both not empty lists
        roots=(self.root!=[] and other.root!=[]) or (self.root==[] and other.root==[])


        #if the roots ever are not equal, return False
        if roots==False:
            return False

        #child_structure assumed to be the same structure
        child_structure=True

        #see if the tree has children
        if len(self.childlist)>0:

            #reference all the indexes 
            for i in range(len(self.childlist)):

                #children boolean to see if the child tree of self is isomorphic to other childlist
                child_structure=self.childlist[i].isIsomorphicTo(other.childlist[i])

                #if the boolean ever says false, break
                if child_structure==False:
                    break

        #return the childstructure if the same and the roots are the same
        return child_structure and roots
                
        
            

#create a main function
def main():



    #the infile must be opened
    infile=open('MultiwayTreeInput.txt','r')



    #number tree a and read a line from the file
    a=1
    line_a=(infile.readline())

    #number tree b and read a line from the file
    b=2
    line_b=(infile.readline())




    #as long as the two lines are not blank
    while line_a!='' and line_b!='':

        #convert the lines into lists
        line_a=eval(line_a)
        line_b=eval(line_b)

        #create trees from the lists
        tree_a=MultiwayTree(line_a)
        tree_b=MultiwayTree(line_b)

        #print out tree a and the preorder of tree a
        print('Tree ',a,': ', line_a)
        print('Tree ',a,' preorder: ',sep='',end='')
        tree_a.preOrder()
        print()

        #print out tree b and the preorder fo tree b
        print('Tree ',b,': ', line_b)
        print('Tree ',b,' preorder: ', sep='',end='')
        tree_b.preOrder()
        print()



        #see if the two trees are isomorphic and print a statement depending on if they are
        if tree_a.isIsomorphicTo(tree_b)==True:
            print('Tree',a,'is isomorphic to Tree',b)
        else:
            print('Tree',a,'is not isomorphic to Tree',b)

        #print two blank lines
        print('\n\n')



        #read two more lines and update the tree numbers
        line_a=(infile.readline())
        a+=1
        line_b=(infile.readline())
        b+=1





#call the main function
main()
