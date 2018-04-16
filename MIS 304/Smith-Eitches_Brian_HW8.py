#Author: Brian Smith-Eitches
#Homework Number and Name: HW8, Cellular Plan Invoice
#Due Date: April 10, 2017
#Program Description:   This program allows a Cellular Plan provider a way to 
#                       create customer invoices using object oriented programing



#import the other python file with the class in it
import cellphoneusage


#create global variables for constants and sentinels
UPDATE_INFO=1
MAKE_CALL=2
SEND_TEXTS=3
VIEW_USAGE=4
FINALIZE_BILL=5

#print menu function where each line of the menu is printed
def print_menu():
    print()
    print('CELL PHONE PLAN USAGE')
    print('1. Update account info')
    print('2. Make call')
    print('3. Send texts')
    print('4. View current usage')
    print('5. Finalize bill')
    print()


#get menu option to be called
def get_menu_option():

    #option is input
    option=int(input('What would you like to do? '))

    #while the input is not valid
    while not valid_input(option):

        #print an error method and ask for a new input
        print('Error. Item must be a number from 1-5.',end=' ')
        option=int(input('What would you like to do? '))

    #return the valid input
    return option


#valid input function determines if option is valid or not
def valid_input(option):

    #returns false if the opiton is invalid
    if option not in range(1,6):
        return False

    #returns true otherwise
    else:
        return True


#main function
def main():


    #plan is an instance of the class; OOP
    plan=cellphoneusage.CellPhoneUsage()

    #print the menu calling the function
    print_menu()

    #first option calls the function get menu option
    option=get_menu_option()

    #until the user finalizes the bill,
    while option!= FINALIZE_BILL:

        #if the option updates info
        if option==UPDATE_INFO:

            #ask for number
            number=input('What is your account number? ')

            #use method to set acct number to number
            plan.set_account_num(number)

            #ask for name
            name=input('What is your account name? ')

            #use mutator method to set acct name to name
            plan.set_account_name(name)


        #if option says make a call
        elif option==MAKE_CALL:

            #ask for how many minutes
            minutes=int(input('How many minutes? '))

            #if the make call is False, ask for a new (positive) set of minutes
            while not plan.make_call(minutes):
                minutes=int(input('How many minutes? '))


        #if option says send texts
        elif option==SEND_TEXTS:

            #ask how many texts
            texts=int(input('How many texts? '))

            #if the send texts method is False, ask for a new (positive) set of texts
            while not plan.send_texts(texts):
                texts=int(input('How many texts? '))


        #if the option says view the usage
        elif option==VIEW_USAGE:
            #print the plan taking advantage of the __str__ method
            print(plan)

        #print a blank line
        print()

        #ask for a new option
        option=get_menu_option()

    #display the bill
    plan.display_bill()

#call the main function
main()
