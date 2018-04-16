# Author: Brian Smith-Eitches
# Homework Number & Name: HW1, The Hardware Store
# Due Date: January 30, 2017
# Program Description:  This program will determine prices and fees
#       associated with book purchases that match the current promotion

def main():
    #prompt user for name
    name=input("Customer Name: ")
    #prompt user for books purchased
    books_purchased=int(input('Books purchased: '))
    #prompt user for membership type
    member_type=input('Membership type (R or P): ')
    
    #initiate variable 'upgrade'
    upgrade='N'
    #create boolean variable 'add_upgrade_fee'
    add_upgrade_fee=False

    #see if member type is regular and decide if they will upgrade
    if member_type=='R' or member_type=='r':
        #initiate member_type_full as the whole string representing membership type
        member_type_full='Regular'
        #Prompt user to answer if he would like to upgrade
        upgrade=input('Would you like to upgrade your membership? (Y or N): ')
        #see if they want to upgrade
        if upgrade=='Y' or upgrade=='y':
            #update the member type to premium
            member_type_full='Premium'
            #change boolean add_upgrade_fee to True
            add_upgrade_fee=True
            #Thank the user for upgrading
            print('Thank you for upgrading!')

    #if member is not regular, the member is Premium        
    else:
        member_type_full='Premium'

    #see if member is still a regular member
    if member_type_full=='Regular':
        #sales price is computed as $10.95 per book puchased times books purchased
        sales_price=10.95*books_purchased
        #go through process to see how many free books they will receive
        if books_purchased>11:
            #add two free books
            total_books=books_purchased+2
        elif books_purchased>=7:
            #add one free book
            total_books=books_purchased+1
        else:
            #add zero free books
            total_books=books_purchased

    #if not a regular member, the member is a premium member
    else:
        #sales price for premium member is 9.49 per book times books purchased
        sales_price=9.49*books_purchased
        #decide how many free books they will receive
        if books_purchased>8:
            #add two free books
            total_books=books_purchased+2
        elif books_purchased>=5:
            #add one free book
            total_books=books_purchased+1
        else:
            #add zero free books
            total_books=books_purchased

    #compute sales tax on the sales price
    sales_tax=.0825*sales_price
    #compute total due as sum of sales price and sales tax
    total_due=sales_tax+sales_price
    #note if we need to add an upgrade fee
    if add_upgrade_fee:
        #add 5.95 to the total due
        total_due+=5.95
        
    #convert the final numbers into strings with two decimals
    sales_price=format(sales_price,'.2f')
    total_due=format(total_due,'.2f')
    sales_tax=format(sales_tax,'.2f')

    #print a blank line
    print()

    #print customer name
    print('Customer:', name)
    #print the type of customer with the full name type
    print('Customer type:',member_type_full)
    #print the number of books received, which includes the free books
    print('Total books received:', total_books)
    #print the selling price as calculated earlier
    print('Selling price: $', sales_price,sep='')
    #print the sales tax amount as calculated earlier
    print('Sales tax: $', sales_tax,sep='')
    #see if the member upgraded today
    if add_upgrade_fee:
        #add $5.95 to the total cost if they upgraded today
        print('Membership fee: $5.95')
    #print out the total amount due
    print('Total amount due: $', total_due,sep='')
main()
