# Author: Brian Smith-Eitches
# Homework Number & Name: HW1, The Hardware Store
# Due Date: January 30, 2017
# Program Description:  This program will identify products with highest profit
#                       margin and most popularity for a Hardware store

def main():


    #ask for name of the product
    name=input("Please enter the product name: ")
    #ask for the sales price of the product
    price=float(input("Please enter the product price: $"))
    #ask for the cost of the product
    cost=float(input("Please enter the product cost: $"))
    #ask for the quantity sold of the product
    quant=int(input("Please enter the quantity of the product sold: "))


    #calculate revenue for the product and round to two decimals
    revenue=format((price*quant),'.2f')
    #calculate cost of the goods sold of this product and round to two decimals
    expense=format((cost*quant),'.2f')
    #calculate the profit of the product and round to two decimals
    profit=format((price-cost)*quant,'.2f')
    #calculate profit_margin and round to two decimals
    profit_margin=format(100*float(profit)/float(revenue),'.2f')


    #print a blank line
    print()


    #print name of the product
    print("Product: ",name, sep='')
    #print revenue with dollar sign
    print("Total revenue is $",(revenue), sep='')
    #print cost with dollar sign
    print("Total cost is $",(expense),sep='')
    #print quantity
    print("Quantity of the product sold is", quant)
    #print the profit as a long string including dollar sign
    print("Total profit (in dollars) generated by the product is $",(profit), sep='')
    #print the percentage profit as a long string
    print("Percentage profit generated by the product is ", profit_margin, '%', sep='')


main()