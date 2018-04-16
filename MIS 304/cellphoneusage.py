#Author: Brian Smith-Eitches
#Homework Number and Name: HW8, Cellular Plan Invoice
#Due Date: April 10, 2017
#Program Description:   This program allows a Cellular Plan provider a way to 
#                       create customer invoices using object oriented programing



#constant for monthly pay rate
MONTHLY_PAY_RATE= 79.95

#constants for text and minutes allowed in the plan
MINUTES_PLAN = 500
TEXTS_PLAN = 100


#constants for the rate that are charged when minutes and texts go over allowed
OVER_MINUTES_RATE = .25
OVER_TEXT_RATE = .2

#constant for the tax rate
TAX_RATE = .0825


#create a class called CellPhoneUsage
class CellPhoneUsage:
     

    #Initialize the object giving it hidden attributes with values of zero
    def __init__(self):
        self.__account_num=0

        #give the accountname attribute a name string 'name'; will be changed later
        self.__account_name='name'
        self.__minutes_used=0
        self.__texts_sent=0


    #method to get account number; accessor
    def get_account_num(self):
        return self.__account_num

    #method to mutate the account number
    def set_account_num(self,new_account_num):
        #update the hidden attribute to the given new account num
        self.__account_num=new_account_num

    #accessor method to get the account name returns the hidden attribute
    def get_account_name(self):
        return self.__account_name

    #mutator method to update the account name to a new name
    def set_account_name(self, name):
        self.__account_name=name

    #accessor for how many minutes were used
    def get_minutes_used(self):
        return self.__minutes_used

    #accessor for how many texts were sent
    def get_texts_sent(self):
        return self.__texts_sent


    #make a call method passed through with 'minutes'
    def make_call(self,minutes):

        #if minutes are not positive, print error and return False
        if minutes<=0:
            print('Error. Minutes must be a positive number')
            return False

        #otherwise, add minutes to attribute self.__minutes_used; return True
        else:
            self.__minutes_used+=minutes
            return True


    #make a send texts method passed through with 'texts'
    def send_texts(self,texts):

        #if texts are not positive, print error and return False
        if texts<=0:
            print('Error. Texts sent must be a positive number')
            return False

        #otherwise, add texts to attribute self.__texts_sent; return True
        else:
            self.__texts_sent+=texts
            return True


    #method to calculate the overage charge for minutes
    def calculate_minutes_charge(self):

        #see if the minutes used are less than the plan. if so, 0 charge
        if self.get_minutes_used()<=MINUTES_PLAN:
            return 0

        #else, the overcharge is the excess times the constant of the over minutes rate
        else:
            overcharge=((self.get_minutes_used()-MINUTES_PLAN)*OVER_MINUTES_RATE)

            #return the overcharge
            return overcharge


    #method to calculate the overage charge for texts
    def calculate_texts_charge(self):

        #see if the texts sent are less than the plan. if so, 0 charge
        if self.get_texts_sent()<=TEXTS_PLAN:
            return 0

        #else, the overcharge is the excess times the constant of the over text rate
        else:
            overcharge=((self.get_texts_sent()-TEXTS_PLAN)*OVER_TEXT_RATE)

            #return the overcharge
            return overcharge


    #method to calculate total due before tax
    def calculate_total(self):

        #find mins and text overcharges
        mins_overcharge = self.calculate_minutes_charge()
        text_overcharge = self.calculate_texts_charge()

        #add the monthly pay rate constant to the two overcharges
        total=MONTHLY_PAY_RATE+mins_overcharge+text_overcharge

        #return the total
        return total

    #define a way to display the bill method
    def display_bill(self):
        
        print()
        #title
        print('CELLPHONE USAGE BILL')

        #account num uses the accessor
        print('Account Number: ', self.get_account_num())

        #account name uses the accessor
        print('Account Name: ',self.get_account_name())

        #minutes allowed is the global constant
        print('Minutes Allowed: ',MINUTES_PLAN)

        #minutes used uses accessor
        print('Minutes Used: ', self.get_minutes_used())

        #minutes overcharge calls the calculate method. format to include decimals and'$'
        print('Minutes Overage Charge: $', format(self.calculate_minutes_charge(), ".2f"), sep="")

        #texts allowed are the global constant
        print('Texts Allowed: ',TEXTS_PLAN)

        #texts used uses accessor
        print('Texts Used: ', self.get_texts_sent())
        
        #texts overcharge calls the calculate method. format to include decimals and'$'
        print('Texts Overage Charge: $', format(self.calculate_texts_charge(), ".2f"), sep="")

        #total charge calls calculate total mehtod and format properly
        print('Total Charge (before tax): $',format(self.calculate_total(), ".2f"), sep="")

        #create a variable for the tax that uses tax rate constant. print and format
        tax=self.calculate_total()*TAX_RATE
        print('Tax amount: $', format(tax, ".2f"), sep="")

        #calculate total due as tax plus the total before. format properly and print
        total=self.calculate_total()+tax
        print('Total due: $', format(total, ".2f"), sep="")


    #create a __str__ method to be used when printing
    def __str__(self):

        #create a string that will add all of the information with new line characters
        #using accessor methods
        string='\n'
        string+='Account Name: '
        string+=str(self.get_account_name())
        string+='\nAccount Number: '
        string+=str(self.get_account_num())
        string+='\nMinutes Used: '
        string+=str(self.get_minutes_used())
        string+='\nTexts Sent: '
        string+=str(self.get_texts_sent())

        #return the string
        return string
    
