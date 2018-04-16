#  File: numberPath.py
#  Description: This program runs a depth first search through a maze of numbers
#                 and attempts to sum the running count to a given target ending
#                 at a certain index
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: April 13, 2017
#  Date Last Modified: April 14, 2017


#import deepcopy function
from copy import deepcopy


#create a class state that includes a sum method and __str__
class State:

    #sum is the sum of the pathHistory attribute
    def sum(self):
        return sum(self.pathHistory)

    #string is to be used when printing.
    def __str__(self):

        #include the grid formatted
        string='  Grid:'
        for line in self.grid:
            string+='\n    '
            for item in line:
                string+=str(item)+' '*(5-len(str(item)))

        #include the history as the pathHistory
        string+='\n  history: '+str(self.pathHistory)

        #include the start point with the start row and start col
        string+='\n  start point: ('+str(self.start_row)+','+str(self.start_col)+')'

        #include the sum so far by calling sum method
        string+='\n  sum so far: '+str(self.sum())+'\n'

        #return the string
        return string


#create method isValid to see if a direction can be used
def isValid(state,direction):

    #if direction says right:
    if direction=='right':
        
        #see if the right column is out of index and return false
        if state.start_col+1>=state.grid_cols:
            return False

        #see if the right item says 'None' and return false
        if state.grid[state.start_row][state.start_col+1]=='None':
            return False

        #return True otherwise
        return True

    #if direction says up:    
    elif direction=='up':

        #see if the above row is out of index and return false        
        if state.start_row-1<0:
            return False

        #see if the above item says 'None' and return false
        if state.grid[state.start_row-1][state.start_col]=='None':
            return False

        #return true otherwise
        return True


    #if direction says down:        
    elif direction=='down':

        #see if the below row is out of index and return false        
        if state.start_row+1>=state.grid_rows:
            return False

        #see if the below item says 'None' and return false
        if state.grid[state.start_row+1][state.start_col]=='None':
            return False

        #else, return True
        return True

    #if direction says down:        
    elif direction=='left':

        #see if the left item is out of index and return false        
        if state.start_col-1<0:
            return False

        #see if the left item says 'None' and return false
        if state.grid[state.start_row][state.start_col-1]=='None':
            return False

        #return true otherwise
        return True
                
#create solve function to be called recursively
def solve(state):

    #start by printing the grid to debug
    print(state)



    #ask if goal state
    print('Is this a goal state?')
    
    #if in end postion and sum is right, print solution found and return the pathHistory to main
    if state.start_row==state.end_row and state.start_col==state.end_col and state.sum()==state.targetValue:
        print('Solution found!')
        return state.pathHistory


    #otherwise, print No and ask next question
    else:
        print('No. ',end='')



    #see is the state's sum exceeds target Value. return none if so
    if state.sum()>state.targetValue:
        print('Target exceeded: abandoning path')
        return None


    #else, not a goal state and not exceeding running count
    else:


        #ask if right is an option by calling isValid with the state and right command
        print('Can I move right?')
        if isValid(state,'right'):

            print('Yes!\n\nProblem is now:')


            #create a new state
            newState1=State()

            #give all the same values updating only start col
            newState1.start_row=state.start_row
            newState1.start_col=state.start_col+1
            newState1.grid_rows=state.grid_rows
            newState1.grid_cols=state.grid_cols
            newState1.end_row=state.end_row
            newState1.end_col=state.end_col
            newState1.targetValue=state.targetValue

            #deepcopy the grid and pathHistory to alter
            newState1.grid=deepcopy(state.grid)
            newState1.pathHistory=deepcopy(state.pathHistory)

            #item is the item in the new location we are going
            item=state.grid[newState1.start_row][newState1.start_col]

            #add this item to newstate's pathHistory
            newState1.pathHistory.append(item)

            #update the grid to have none in the new location
            newState1.grid[newState1.start_row][newState1.start_col]='None'

            #find result going this way and recursively call the function
            result = solve(newState1)

            #see if the result is None and return result if so
            if result!=None:
                return result

        #if you cant move this direction, say 'No'
        else:
            print('No.',end=' ')


        #ask if left is an option by calling isValid with the state and left command
        print('Can I move up?')
        if isValid(state,'up'):
            
            print('Yes!\n\nProblem is now:')


            #create a new state
            newState2=State()

            #give all the same values updating only start row
            newState2.start_row=state.start_row-1
            newState2.start_col=state.start_col
            newState2.grid_rows=state.grid_rows
            newState2.grid_cols=state.grid_cols
            newState2.end_row=state.end_row
            newState2.end_col=state.end_col
            newState2.targetValue=state.targetValue

            #deepcopy the grid and pathHistory to alter
            newState2.grid=deepcopy(state.grid)
            newState2.pathHistory=deepcopy(state.pathHistory)
            
            #item is the item in the new location we are going
            item=state.grid[newState2.start_row][newState2.start_col]

            #add this item to newstate's pathHistory
            newState2.pathHistory.append(item)

            #update the grid to have none in the new location
            newState2.grid[newState2.start_row][newState2.start_col]='None'

            #see if the result is None and return result if so
            result = solve(newState2)

            #see if the result is None and return result if so
            if result!=None:
                return result

        #if you cant move this direction, say 'No'
        else:
            print('No.',end=' ')



        #ask if down is an option by calling isValid with the state and down command
        print('Can I move down?')

        #do exactly the same stuff as above, only with the start row as row+1
        if isValid(state,'down'):
            print('Yes!\n\nProblem is now:')
            newState3=State()
            newState3.start_row=state.start_row+1
            newState3.start_col=state.start_col
            newState3.grid_rows=state.grid_rows
            newState3.grid_cols=state.grid_cols
            newState3.end_row=state.end_row
            newState3.end_col=state.end_col
            newState3.targetValue=state.targetValue
            newState3.grid=deepcopy(state.grid)
            newState3.pathHistory=deepcopy(state.pathHistory)
            item=state.grid[newState3.start_row][newState3.start_col]
            newState3.pathHistory.append(item)
            newState3.grid[newState3.start_row][newState3.start_col]='None'
            result = solve(newState3)
            if result!=None:
                return result
        else:
            print('No.',end=' ')


        #ask if left is an option by calling isValid with the state and left command            
        print('Can I move left?')

        #do exactly the same stuff only with the column minus 1 as new start col
        if isValid(state,'left'):
            newState4=State()
            newState4.start_row=state.start_row
            newState4.start_col=state.start_col-1
            newState4.grid_rows=state.grid_rows
            newState4.grid_cols=state.grid_cols
            newState4.end_row=state.end_row
            newState4.end_col=state.end_col
            newState4.targetValue=state.targetValue
            newState4.grid=deepcopy(state.grid)
            newState4.pathHistory=deepcopy(state.pathHistory)
            print('Yes!\n\nProblem is now:')
            item=state.grid[newState4.start_row][newState4.start_col]
            newState4.pathHistory.append(item)
            newState4.grid[newState4.start_row][newState4.start_col]='None'
            result = solve(newState4)
            if result!=None:
                return result
        else:
            print('No.',end=' ')
            #if we get to this point, couldn't move in any direction. backtrack now by returning None
            print("Couldn't move in any direction. Backtracking")
            return None

    #if we get to this point, no solution was found. return none to main program
    print('\nThere is no solution found')
    return None

#create main function           
def main():

    #open the file
    file=open('pathdata.txt','r')

    #create a myState as an instance of State class
    myState=State()

    #create varslist from the first line
    varslist=file.readline().split()

    #give myState instance variables from items in first line
    myState.targetValue=int(varslist[0])
    myState.grid_rows=int(varslist[1])
    myState.grid_cols=int(varslist[2])
    myState.start_row=int(varslist[3])
    myState.start_col=int(varslist[4])
    myState.end_row=int(varslist[5])
    myState.end_col=int(varslist[6])

    #give mystate a grid and pathHistory as lists
    myState.grid=[]
    myState.pathHistory=[]

    #convert each line in the file to a list
    for line in file:
        line=line.split()

        #convert the list of str's into a list of ints
        for i in range(len(line)):
            line[i]=int(line[i])

        #add these lists into the grid instance variable
        myState.grid.append(line)


    #append pathHistory as where you start
    myState.pathHistory.append(myState.grid[myState.start_row][myState.start_col])

    #update the grid to have 'None' where you start
    myState.grid[myState.start_row][myState.start_col]='None'

    #solve the answer calling the recursive solve
    answer=solve(myState)

    #if the answer is not None, print the answer!
    if answer!=None:
        print(answer)


    #close the file
    file.close()

#call main()
main()
