


#import the two tkinter modules
import tkinter
import tkinter.messagebox

#create literals for the prices of items
HAT=21.99
MUG=10.99
SHIRT=26

#literals for the prices of shipping
SHIPPING_3_5_DAYS=1.99
SHIPPING_2_DAYS=2.99
SHIPPING_1_DAY=5.99



#create a class
class MyGUI:

    #initialize an instance
    def __init__(self):

        #create main window
        self.main_window=tkinter.Tk()

        #create three frames
        self.product_frame=tkinter.Frame(self.main_window)
        self.shipping_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)


        #use cb variables stored as ints to represent if the checkbox is checked
        self.cb_hat=tkinter.IntVar()
        self.cb_mug=tkinter.IntVar()
        self.cb_shirt=tkinter.IntVar()

        #start out with none of the boxes checked
        self.cb_hat.set(0)
        self.cb_mug.set(0)
        self.cb_shirt.set(0)


        #create a header for the product header to go in the product frame
        self.product_label=tkinter.Label(self.product_frame, text='Products:')

        #create three check box buttons to go in the product frame with their names; update the associated variables
        self.cb_hat_button=tkinter.Checkbutton(self.product_frame, text='Hat', variable=self.cb_hat)
        self.cb_mug_button=tkinter.Checkbutton(self.product_frame, text='Mug', variable=self.cb_mug)
        self.cb_shirt_button=tkinter.Checkbutton(self.product_frame,text='T-Shirt', variable=self.cb_shirt)

        #create a blank label to separate product frame from shipping frame
        self.space_label=tkinter.Label(self.product_frame,text='')


        #pack the label, the three buttons, and the blanks pace label
        self.product_label.pack()
        self.cb_hat_button.pack(side='top')
        self.cb_mug_button.pack(side='top')
        self.cb_shirt_button.pack(side='top')
        self.space_label.pack()





        #create a radio variable to decide which shipping is chosen
        self.radio_var=tkinter.IntVar()

        #set it to automatically choose three day shipping
        self.radio_var.set(3)

        # create a shipping header in the shipping frame
        self.shipping_label=tkinter.Label(self.shipping_frame,text='Shipping:')

        #make a radio button for 3-5 day shipping where the variable value is set to three
        self.rbshipping3=tkinter.Radiobutton(self.shipping_frame, text='3-5 days',
                                             variable=self.radio_var, value=3)

        #make a radio button for 2 day shipping where the variable value is set to two        
        self.rbshipping2=tkinter.Radiobutton(self.shipping_frame, text='2 days',
                                             variable=self.radio_var, value=2)

        #make a radio button for 1 day shipping where the variable value is set to 1
        self.rbshipping1=tkinter.Radiobutton(self.shipping_frame,text='1 day',
                                             variable=self.radio_var,value=1)
         

        #pack the header and three radio buttons
        self.shipping_label.pack()
        self.rbshipping3.pack()
        self.rbshipping2.pack()
        self.rbshipping1.pack()
        

        #create a done button to destroy the program when clicked
        self.done_button=tkinter.Button(self.bottom_frame, text='Done',
                                        command=self.main_window.destroy)

        #create a checkout button to call the self.checkout function when clicked
        self.checkout_button=tkinter.Button(self.bottom_frame, text='Checkout',
                                            command=self.checkout)

        #pack the two buttons
        self.checkout_button.pack(side='left')        
        self.done_button.pack(side='left')





        #pack the three frames
        self.product_frame.pack()
        self.shipping_frame.pack()
        self.bottom_frame.pack()

        #call the mainloop
        tkinter.mainloop()




    #create a subtotal function to sum up the subtotal
    def subtotal(self):
        subtotal=0

        #see if the person got a hat and add price
        if self.cb_hat.get()==1:
            subtotal+=HAT

        #see if person got a mug and add price
        if self.cb_mug.get()==1:
            subtotal+=MUG

        #see if person got a shirt and add price
        if self.cb_shirt.get()==1:
            subtotal+=SHIRT

        #return the subtotal
        return subtotal




    #create a shipping function to find the shipping price
    def shipping(self):

        #see if 3 day shipping was chosen and give it that cost
        if self.radio_var.get()==3:
            cost=SHIPPING_3_5_DAYS

        #see if two day shipping was chosen and give it that cost
        elif self.radio_var.get()==2:
            cost=SHIPPING_2_DAYS

        #see if one day shipping was chosen and give it that cost
        elif self.radio_var.get()==1:
            cost=SHIPPING_1_DAY

        #return the cost
        return cost
            



    #this is the checkout function called when checkout button is clicked
    def checkout(self):

        #find the shipping total and subtotal
        subtotal=self.subtotal()
        shipping=self.shipping()
        total=subtotal+shipping

        #format the shipping total and subtotal
        subtotal='$'+format(subtotal,'.2f')
        shipping='$'+format(shipping,'.2f')
        total='$'+format(total,'.2f')

        #display the invoice with the subtotal, shipping, and total as a string
        tkinter.messagebox.showinfo('Invoice', 'Subtotal: '+subtotal+'\n'+
                                    'Shipping: '+shipping+'\n'+
                                    'Total: '+total)
mygui=MyGUI()
