#Author: Brian Smith-Eitches
#Homework Number and Name: HW5, Average hours worked
#Due Date: March 6, 2017
#Program Description:   This program helps a boss automate the calculation of average
#                       weekly work hours from an input file and stores  the data
#                       in an output file.


#define a user input and validation function to take in number of weeks worked
def user_input_and_validation():

    #prompt user
    weeks=int(input('How many weeks did each employee work? '))

    #validate information; must be greater than zero
    while weeks<=0:
        weeks=int(input('Error. Weeks worked must be positive. How many weeks worked? '))

    #return the input
    return weeks


#define a function to help find hours worked from a list
def average_hours_worked(data):

    #total hours accumulator starts with zero
    total_hours=0

    #iterate through data from a list to modify accumulator to total sum
    for hours in data:
        total_hours+=hours

    #determine average to be total sum divided by number of items in the list
    average=total_hours/len(data)

    #return the average hours worked calculated in function as 'average'
    return average


#define what to write to file by taking in three pieces of data and the destination file
def write_to_file(last_name,first_name,hours,file):

    #destination file needs to write the 'last_name, first_name hours\n')
    file.write(last_name+', '+first_name+' '+hours+'\n')


#define the main function
def main():

    #use try, except to deal with errors that may occur. just try everything first
    try:

        #weeks comes from input function defined above
        weeks=user_input_and_validation()

        #start employees counter
        employees=0

        #open the file from 'Employees.txt' in read mode
        file=open('Employees.txt','r')

        #open outfile as 'EmployeeAverages.txt' in write mode
        outfile=open('EmployeeAverages.txt','w')

        # determine first and last name to be first two lines of the txt file
        first_name=file.readline().rstrip('\n')
        last_name=file.readline().rstrip('\n')

        #while the information is not  empty:
        while first_name!='' and last_name!='':

            #the hours list for the person starts empty
            hours_list=[]

            #make a for loop that iterates the number from input for weeks
            for data in range(weeks):
                #convert the line to an integer and add it to the hours list
                data=int(file.readline())
                hours_list.append(data)

            #this person's hours come from the helper function that takes hours list in
            person_hours=average_hours_worked(hours_list)

            #take the person's hours and convert to a string with two decimals
            person_hours=format(person_hours,'.2f')

            #write the file with the helper function giving it all information needed
            write_to_file(last_name,first_name,person_hours,outfile)

            #update first and last name to be next two lines
            first_name=file.readline().rstrip('\n')
            last_name=file.readline().rstrip('\n')

            #update employee counter
            employees+=1

        #print number of employees processed and output location
        print('Number of employees processed:',employees)
        print('Name of output file is EmployeeAverages.txt')

        #close the files
        file.close()
        outfile.close()


    #if this error happens, trouble converting a line to an int and return this statement
    except ValueError:
        print('Error. Non-Numeric number of hours worked found.')

        #still close the two files
        file.close()
        outfile.close()


    #if this error happens, the input file is not found. return statement and end gracefully
    except FileNotFoundError:
        print('Error. File was not found.')

#call the main function
main()
