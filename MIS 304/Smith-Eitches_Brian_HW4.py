#Author: Brian Smith-Eitches
#Homework Number and Name: HW4, Electronics Business
#Due Date: March 1, 2017
#Program Description:   This program allows GrapeFruit Elecronics to take online orders
#                       and displays a receipt at the end of the program.

#define a function that will print out the menu with prices and spacing
def print_menu():
    print('GRAPEFRUIT ELECTRONICS')
    print('1. gPod               $249')
    print('2. gPad Pro           $599')
    print('3. gPhone 7 Plus      $769')
    print('4. gMac               $1,499')
    print('5. gMacBook Pro       $1,999')
    print('6. gMac Pro           $2,999')
    print('7. Grapefruit Watch   $299')
    print('8. Complete order')
    print()


#create a function that will ask for an item and validate the input
def item_input_and_validation():
    
    #ask user for an item
    item=(input('What item would you like to order? (8 completes order) '))

    #enter infinite while loop
    while True:

        #see if the item can be converted to an integer
        try:
            
            #convert string to integer and break out of infinite loop
            item=int(item)
            break

        #if there is an error making the string an item number, prompt user to enter a number
        except:
            item=input('Please enter an item number: ')

    #make sure the item is from 1 to 8 inclusive (validate data)
    while item not in range(1,9):
        item=int(input('Error. Please enter a number from 1 to 8 for the item: '))

    #return the value of item
    return item

#create a function to take in quantity and validate data
def quantity_input_and_validation():

    #ask user for quantity
    quantity=int(input('How much of this item would you like to order? '))

    #enter an infinite loop that breaks when an integer is entered
    while True:
        try:
            quantity=int(quantity)
            break
        except:
            item=input('Please enter a quantity number: ')

    #validate quantity by making sure it is positive
    while quantity<=0:
        quantity=int(input('Error. Please enter a positive number'))

    #return valid quantity
    return quantity

#create a function to find price of item
def item_price(item):
    
    #create a list will all prices in correct index
    item_cost_list=[249,599,769,1499,1999,2999,299]

    #return price associated with item number
    return item_cost_list[item-1]

#create a function to find name of item
def item_name(item):

    #have a list with item names in correct indices
    item_name_list=['gPod','gPad Pro','gPhone 7 Plus', 'gMac','gMacbookPro',
                    'gMac Pro', 'Grapefruit Watch']

    #return the item name
    return item_name_list[item-1]

#create a bulk discount function to return the discount percent as a decimal 
def bulk_discount_percent(quantity):

    #return the discount percent based on size of quantity
    if quantity>15:
        return .25
    elif quantity>=10:
        return .2
    elif quantity >=5:
        return .1
    else:
        return 0

#create a main function                    
def main():
    #print the menu calling menu function
    print_menu()

    #get name from user
    name=input('Customer name: ')

    #initialize order quantity size and cost as 0
    total_quantity=0
    total_cost=0

    #force this to happen forever as long as user does not hit number "8"
    while True:
        
        #getting item and making sure it is a valid number
        item=item_input_and_validation()
        
        #break out of loop when he types 8
        if item==8:
            break

        #gather valid quantity
        quantity=quantity_input_and_validation()

        #retrieve unit price
        unit_price=item_price(item)

        #repeat to user what was ordered
        print('You purchased', quantity,'of item', item_name(item))

        #add the quantity purchased to total quantity
        total_quantity+=quantity

        #add the cost to the total cost
        total_cost+=(quantity*unit_price)

    #see if nothing was ordered and print no receipt
    if total_quantity==0:
        print('\nNothing purchased. Thank you for visiting!')

    #else, print receipt
    else:
        print()

        #calculate discount amount by calling percent function
        bulk_discount_amount=total_cost*bulk_discount_percent(total_quantity)
        
        #convert the discount percentage into a string with a percent sign
        discount_percent=str(int(bulk_discount_percent(total_quantity)*100))+'%'

        #find the new price after discount
        discounted_price=total_cost-bulk_discount_amount

        #calculate sales tax
        sales_tax=discounted_price*.0825

        #calculate total due
        total_due=sales_tax+discounted_price

        #convert all numbers into strings with commas and 2 decimals
        bulk_discount_amount='$'+format(bulk_discount_amount,',.2f')
        discounted_price='$'+format(discounted_price,',.2f')
        total_cost='$'+format(total_cost,',.2f')
        sales_tax='$'+format(sales_tax,',.2f')
        total_due='$'+format(total_due,',.2f')

        #print the receipt
        print('Cutomer name:',name)
        print('Total price before discount:',total_cost)
        print('Total quantity of electronics purchased:',total_quantity)

        #print the discount amount if discount is applied
        if total_quantity>=5:
            print('Discount percentage earned:', discount_percent)
            print('Discount amount:', bulk_discount_amount)
            print('Total price after discount:', discounted_price)

        #print rest of receipt
        print('Sales tax:', sales_tax)
        print('Total amount due:', total_due)

#call main function    
main()
