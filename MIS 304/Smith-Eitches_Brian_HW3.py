#Author: Brian Smith-Eitches
#Homework Number and Name: HW3, Pizza Business
#Due Date: February 13, 2017
#Program Description:   This program allows a pizza business to take in orders
#                       with simple item numbers being ordered. Then it displays
#                       a receipt to the customer.


#print the menu items with correct flush spacing
print('MENU ITEMS\t\tPRICES')
print('1. Pizza\t\t$7.29 sm  $12.39 lg')
print()
print('TOPPINGS')
print('2. Green peppers\t$1.50')
print('3. Mushrooms\t\t$1.00')
print('4. Pepperoni\t\t$2.00')
print('5. Complete my order')
print()

#prompt user for name
customer_name=input('Please enter customer name: ')

#prompt user for item number
purchase_item=int(input('What item number would you like to purchase? '))

#initialize cost, pizzas, and toppings accumulator values as zero
cost=0
pizzas=0
toppings=0

#enter a loop that continues until the user presses '5'
while (purchase_item)!=5:
    
    #determine if item number is invalid
    if purchase_item not in range(1,5):
        #prompt user to re-enter their item to be ordered
        purchase_item=int(input('Incorrect menu option. Please re-enter item number: '))
        #restart the while loop
        continue

    #see if it is a pizza
    if (purchase_item)==1:
        
        #determine if it is a small or alarge
        size=input('Small or Large? (enter "sm" or "lg"): ')
        #test validity of pizza size, wait until valid size is chosen
        while size!='sm' and size!='lg':
            #prompt user to reenter pizza size until valid input
            size=input('Invalid pizza size. Re-enter "sm" or "lg": ')
        #see if it is a small
        if size=='sm':
            #tell the user what he purchased
            print("You purchased a small pizza")
            #add 7.29 to the total cost
            cost+=7.29
            
        #else it is a large
        else:
            #tell user large is ordered
            print("You purchased a large pizza")
            #add 12.39 to the total cost
            cost+=12.39
        #add 1 to pizza accumulator
        pizzas+=1

    #see if green peppers bought
    elif (purchase_item)==2:
        #add 1 to topping accumulator
        toppings+=1
        #tell user what he ordered
        print('Green peppers added')
        #add the cost
        cost+=1.5
        
    #see if mushrooms bought
    elif (purchase_item)==3:
        #add 1 to topping accumulator
        toppings+=1
        #tell user mushrooms added
        print('Mushrooms added')
        #add the cost
        cost+=1

    #see if pepperoni added    
    elif (purchase_item)==4:
        #add 1 to topping accumulator
        toppings+=1
        #tell user pepperoni added
        print('Pepperoni added')
        #add the cost
        cost+=2
        
    #prompt user to enter the next item he wants to purchase
    purchase_item=int(input('What item number would you like to purchase? ("5" completes order) '))    

#compute sales tax and total due
sales_tax=.0825*cost
total_due=cost+sales_tax

#print blank line
print()

#see if nothing was ordered
if cost==0:
    #tell user that he did not purchase anything
    print('User did not purchase anything')

#else they ordered something and a receipt must be printed
else:
    #convert cost, sales tax, and total due into a string with '$x.xx' format
    cost='$'+format(cost,'.2f')
    sales_tax='$'+format(sales_tax,'.2f')
    total_due='$'+format(total_due,'.2f')
    
    #print out the receipt
    print('Customer name:',customer_name)
    print('Total number of pizzas ordered:',pizzas)
    print('Total number of toppings ordered:', toppings)
    print('Price of pizzas and toppings before sales tax:', cost)
    print('Sales tax:', sales_tax)
    print('Total amount due:', total_due)
