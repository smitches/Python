#Author: Brian Smith-Eitches
#Homework Number and Name: HW6, Donation Summary
#Due Date: March 20, 2017
#Program Description:   This program helps a nonprofit understand more about donations
#                       data found in an input file.



# create the matching amount function that will go through donation list and
# matching type to calculate the employer donations
def calculate_matching_amount(individual_donation_list,match_list):\
    
    #create a new empty list for the matched amounts
    match_amount=[]

    #go through all of the individual donation lists
    for index in range(len(individual_donation_list)):

        #find the matching program associated with that donation and calculate matching amount
        if match_list[index]=='Ratio':
            amount=individual_donation_list[index]/2
            if amount>15000:
                amount=15000
        elif match_list[index]=='Dollar':
            amount=individual_donation_list[index]
            if amount>10000:
                amount=10000
        elif match_list[index]=='None':
            amount=0

        #add the amount matched to a new list
        match_amount.append(amount)

    #return the new list with all the matched amounts
    return match_amount



#calculate the total donations from individual donations and matched donations
def calculate_total_donations(match_amount_list,individual_donation_list):

    #create a new list for the total donations associated with each individual
    total_donations_list=[]

    #go through all the data in the matched amounts
    for index in range(len(match_amount_list)):
        
        #create a variable 'total' representing this person's donation value
        # and add together the employer matched amount and individual donation
        total=match_amount_list[index]+individual_donation_list[index]

        #add the data into the total donations list
        total_donations_list.append(total)

    #return the list
    return total_donations_list




#define a calculate list sum for a given numeric list
def calculate_list_sum(data_list):

    #accumulator is zero
    total=0

    #go through all of the numbers and add it to total accumulator
    for data in data_list:
        total+=data

    #return the total accumulator value
    return total




#write to output the information given by name, matched amount, total donation, and file destination
def write_to_output_file(name,match_amount,total,file):

    #convert match amount and total to have zero decimals and a $ sign
    match_amount='$'+format(match_amount,',.0f')
    total='$'+format(total,',.0f')

    #write to the file the information as a string ending with new line character
    file.write(name+' has '+match_amount+' in employer matched donations and '+total+' total donations.\n')





#create a main function to be called later
def main():

    #create a try, except error to see that the file is found
    try:
        data=open("DonorData.txt","r")
    #end the program gracefully if file is not found
    except FileNotFoundError:
        print('"DonorData.txt" file is not found')
        return

    #open output file
    summary=open("DonorSummaryData.txt","w")

    #initialize the first name with the endline character stripped
    name=data.readline().rstrip('\n')

    #create accumulator for people
    people=0

    #initialize the name, donation, and match type lists
    name_list=[]
    individual_donation_list=[]
    match_program_list=[]

    #go through while loop until the name is blank
    while name!='' and name!=' ':

        #donation is the next line as integer
        donation=int(data.readline())

        #match type is next line without new line character
        match=data.readline().rstrip('\n')

        #add name, donation, and match type to their lists
        name_list.append(name)
        individual_donation_list.append(donation)
        match_program_list.append(match)

        #udpate the name to be the next line
        name=data.readline().rstrip('\n')

        #add 1 to the people accumulator
        people+=1

    #see if the input file was empty and end program if it is empty
    if people==0:
        print('Input file "DonorData.txt" is empty and has no data')
        return

    #create a new list with the matching amounts by calling matching amount function
    match_amount_list=calculate_matching_amount(individual_donation_list,match_program_list)

    #create a new list with total donations by calling total donatinos list
    total_donations_list=calculate_total_donations(match_amount_list,individual_donation_list)

    #go through each individual referenced by an index with all values associated
    for index in range(len(name_list)):
        
        #find the person's name, employer matching amount, and total donation to send to write function
        name=name_list[index]
        match_amount=match_amount_list[index]
        total=total_donations_list[index]

        #write to the output file sending the name match amount and total donation to summary file
        write_to_output_file(name, match_amount,total,summary)

    #close the two files
    data.close()
    summary.close()

    #calculate the total personal donations, total matched donations, and total received donations
    #by calling the calculate list sum function. THEN convert to a string with a dollar sign and commas
    total_personal_donations='$'+format(calculate_list_sum(individual_donation_list),',.0f')
    total_matched_donations='$'+format(calculate_list_sum(match_amount_list),',.0f')
    total_donations_received='$'+format(calculate_list_sum(total_donations_list),',.0f')

    #print the output to the console
    print('Number of donors processed:', people)
    print('Total personal donations received by donors:',total_personal_donations)
    print("Total donations matched by donors' employers:", total_matched_donations)
    print("Total donations received:", total_donations_received)

#call the main function
main()
    
        
        
