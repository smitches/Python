#Author: Brian Smith-Eitches
#Homework Number and Name: HW7, Customer Analysis
#Due Date: March 27, 2017
#Program Description:   This program helps a local restaurant understand more
#                       about their customer base and improve marketing strategies







#Use literals for the input files
file_a='Pizza.txt'
file_b='Salad.txt'

#Use literals for the output files
file_c='Pizza-output.txt'
file_d='Salad-ouptut.txt'

#Use literals for menu options
both=1
either_or_both=2
pizza_only=3
salad_only=4
only_pizza_or_salad=5
most_pizza=6
most_salad=7
least_pizza=8
least_salad=9

#Use literals for sentinal
exit=10



#create input file to be analyzed and converted to a dictionary function
def process_input_file(file):

    #initialize blank dictionary
    dictionary={}

    #read through lines in file
    for line in file:

        #convert lines to list
        line_list=line.rstrip('\n').split()

        #name a person as the first two list items capitalized and connected by string
        person=line_list[0].capitalize()+' '+line_list[1].capitalize()

        #see if person in dictionary already and increment by 1
        if person in dictionary:
            dictionary[person]+=1

        #else, add the person to the dictionary
        else:
            dictionary[person]=1

    #return the dictionary
    return dictionary



#create a find best function that takes in a dictionary
def find_best(dictionary):

    #most is 0 ordered
    most=0

    #read through dictionary
    for key in dictionary:

        #if the value of a person is greater than most, update most and name the person responsible
        if dictionary[key]>most:
            most=dictionary[key]
            person=key

    #return the name of the person responsible
    return person



#create a find worst function that takes in a dictionary
def find_worst(dictionary):

    #randomly take one item from a dicitionary
    for key in dictionary:
        
        #store this person as a person and its value as the least number
        least=dictionary[key]
        person=key

        #don't read through the entire dictionary; break out
        break


    #read through all items in the dictionary
    for key in dictionary:

        #see if the value is less than least
        if dictionary[key]<least:

            #update least and name the person responsible
            least=dictionary[key]
            person=key

    #return the name of the person
    return person



#display names from a set that takes in a set
def display_names_in_set(set_1):

    #iterate throught the set and print the name on a new line
    for name in set_1:
        print(name)

    #write out names in this set
    print('There are',len(set_1),'customers')



#write info to the output file that takes in file location and dictionary
def write_info_to_output_file(file,dictionary):

    #read through dictionary
    for key in dictionary:

        #find the value of the person
        value=dictionary[key]

        #write the name, space
        file.write(str(key))
        file.write(' ')

        #write the value, new line character
        file.write(str(value))
        file.write('\n')



#define a print menu function to be called after all commands
def print_menu():

    #print all of the menu
    print('CUSTOMER ANALYSIS')
    print('1. Which customers purchased both pizza and salad?')
    print('2. Which customers purchased either product or both products?')
    print('3. Which customers purchased only pizza?')
    print('4. Which customers purchased only salad?')
    print('5. Which customers purchased only pizza or only salad?')
    print('6. Which customer purchased the most pizza?')
    print('7. Which customer purchased the most salad?')
    print('8. Which customer purchased the least pizza (of customers who purchased pizza)?')
    print('9. Which customer purchased the least salad (of customers who purchased salad)?')
    print('10. Exit')
    print()


#create a main function
def main():


    #name the input files as read
    pizza=open(file_a,'r')
    salad=open(file_b,'r')

    #name the output files as write mode
    out_pizza=open(file_c,'w')
    out_salad=open(file_d,'w')


    #create the dictionary by processing pizza input
    pizza_dict=process_input_file(pizza)

    #create the dictionary by processing salad input
    salad_dict=process_input_file(salad)

    #create pizza and salad sets as blank sets
    pizza_set=set()
    salad_set=set()


    #read through pizza dictionary and add the keys to the pizza set
    for key in pizza_dict:
        pizza_set.add(key)

    #read through the salad dictionary and add the keys to the salad set
    for key in salad_dict:
        salad_set.add(key)


    #write the output files by calling command and giving the file location and dictionary
    write_info_to_output_file(out_pizza,pizza_dict)
    write_info_to_output_file(out_salad,salad_dict)
    


    # call the print menu function
    print_menu()

    #ask the user what analysis he'd like to do
    menu_item=int(input('What analysis would you like to do?'))

    #validate input
    while menu_item not in range(1,11):
        menu_item=int(input('Please enter a number from 1-10. Which analysis would you like to do?'))



    #while the menu item doesn't say to exit
    while menu_item!=exit:

        #print blank line
        print()



        #see if menu item says both
        if menu_item==both:

            #find the intersect of the two sets
            set_a=pizza_set & salad_set
            print('CUSTOMERS PURCHASED BOTH PIZZA AND SALAD')

            #call to display the names in the intersect set
            display_names_in_set(set_a)



        #see if menu item asks for either or both
        elif menu_item==either_or_both:

            #name a new set as the union of the two sets
            set_b=pizza_set|salad_set
            print('CUSTOMERS PURCHASED EITHER OR BOTH PIZZA AND SALAD')

            #display the names in the union set
            display_names_in_set(set_b)


        #see if menu item asks for only pizza
        elif menu_item==pizza_only:

            #call it the difference of the pizza set minus the salad set
            set_c=pizza_set-salad_set
            print('CUSTOMERS PURCHASED ONLY PIZZA')

            #display the names in the difference set
            display_names_in_set(set_c)


        #see if menu item asks for only salad
        elif menu_item==salad_only:

            #name a new set as the difference of the salad set minus the pizza set
            set_d=salad_set-pizza_set
            print('CUSTOMERS PURCHASED ONLY SALAD')

            #display the names in the difference set
            display_names_in_set(set_d)


        #see if menu item asks for the symmetric difference
        elif menu_item==only_pizza_or_salad:

            #call the new set the union of the two differences
            set_e= (salad_set-pizza_set)|(pizza_set-salad_set)
            print('CUSTOMERS PURCHASED ONLY PIZZA OR ONLY SALAD')

            #display the names in this set of the symmetric difference
            display_names_in_set(set_e)


        #see if user asked for most pizza
        elif menu_item==most_pizza:

            #find the name by calling the find best of pizza dict function
            person = find_best(pizza_dict)

            #print the name and value of this person from the dictionary
            print('WHO PURCHASED THE MOST PIZZA?')
            print(person,'bought',pizza_dict[person],'pizzas')


        #see if user asked for most salad
        elif menu_item==most_salad:

            #find the name by calling the find best of salad dict function
            person= find_best(salad_dict)

            #print the name and value of this person from the dictionary
            print('WHO PURCHASED THE MOST SALAD?')
            print(person,'bought',salad_dict[person],'salads')


        #see if user asked for least pizza
        elif menu_item==least_pizza:
            
            #find the name by calling the find worst of pizza dict function
            person = find_worst(pizza_dict)

            #print the name and value of this person from the dictionary
            print('WHO PURCHASED THE LEAST PIZZA?')
            print(person,'bought',pizza_dict[person],'pizza(s)')


        #see if user asked for least salad
        elif menu_item==least_salad:

            #find the name by calling the find worst of salad dict function
            person= find_worst(salad_dict)

            #print the name and value of this person from the dictionary
            print('WHO PURCHASED THE LEAST SALAD?')
            print(person,'bought',salad_dict[person],'salad(s)')


        #print a blank line and call the print menu function
        print()
        print_menu()

        #ask the user for a menu item and validate input
        menu_item=int(input('What analysis would you like to do? (10 is to exit)'))
        while menu_item not in range(1,11):
            menu_item=int(input('Please enter a number from 1-10. Which analysis would you like to do?'))


    #close all four files
    pizza.close()
    salad.close()
    out_pizza.close()
    out_salad.close()

#call the main function
main()
