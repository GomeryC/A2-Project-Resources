from ast import Try
import tkinter as tk
import pickle
from tkinter import PhotoImage
import sqlite3
import csv
import os
import pprint
from tkinter import messagebox


class User: #creates the User class blueprint, which can be called by the register page when saving data to pkl file,
            #with appropriate attributes for User Data
    def __init__(self, userID, uname, pword, fname, sname, Email, address, phone, staff=False, member=False, order_count=0):
        self.userID = userID
        self.uname = uname
        self.pword = pword
        self.fname = fname
        self.sname = sname
        self.email = Email
        self.address = address
        self.phone = phone
        self.staff = staff  
        self.member = member  
        self.order_count = order_count  




class Product: #creates  the Product class blueprint, which can be called when the stcreate menu is called and the data is saves to a pkl file
               #contains appropriate attributes which can be called in list boxes throughout the program
    def __init__(self, prodID, Name, prodesc, prodprice, prodtags, stocknum):
        self.prodID = prodID
        self.Name = Name
        self.prodesc = prodesc
        self.prodprice = prodprice
        self.prodtags = prodtags
        self.stocknum = stocknum
       
    def __repr__(self) -> str:
        return f"Product(prodID={self.prodID}, name={self.Name}, prodesc={self.prodesc}, prodprice={self.prodprice}, prodtags={self.prodtags}, stocknum={self.stocknum})"




class Orders: #creates the Order class which can be called throughout the program to save user data, product data and more to a list to allow employees to
              #correctly prepare and ship orders to customers
    def __init__(self, orderID, orderprice, userID, prodID):
        self.orderID = orderID
        self.orderprice = orderprice
        self.userID = userID
        self.prodID = prodID


class Discount: #creates the Discount class that allows for the user to input a discount code which will remove a certain amount from the total value.
    def __init__(self, code, value):
        self.code = code
        self.value = value








def import_toys():


    with open("toys.csv", mode='r', newline='') as file:
    # Create a CSV reader object to allow for the toys CSV to be converted to a PKL file for use in the program
        csv_reader = list(csv.reader(file))


   


    toy_list = []
    for i in range(len(csv_reader)):
        temp = Product(csv_reader[i][0],csv_reader[i][1],csv_reader[i][2],csv_reader[i][3],csv_reader[i][4], int(csv_reader[i][7]))
        toy_list.append(temp)
    pprint.pprint(toy_list)
    #Prints the Toy data to ensure that the data is correct, to prevent against corruption or errors when converting data


    with open('toys.pkl', 'wb+') as file:
        pickle.dump(toy_list, file)
        #Saves the data to the new PKL file
        print("Updataed")
        pprint.pprint (Product)
    #Prints the new data in the Product class in order to allow you to compare it with the previous data to outline any errors during conversion


def import_users():
    with open("users.csv", mode='r', newline='') as file:
    # Create a CSV reader object to allow for the user CSV to be converted into a PKL file for use in the program
            csv_reader = list(csv.reader(file))


   


    user_list = []
    for i in range(len(csv_reader)):
        temp = User(csv_reader[i][0],csv_reader[i][1],csv_reader[i][2],csv_reader[i][3],csv_reader[i][4], csv_reader[i][5], csv_reader[i][6], csv_reader[i][7], csv_reader[i][8])
        user_list.append(temp)


    with open('users.pkl', 'wb') as file:
        pickle.dump(user_list, file)
    #Saves the data to the new PKL file by appending the new list.


def homepage():
    home_page = tk.Tk()
    home_page.resizable(False, False)
    #Prevents the vindow being resized by users
    home_page.config(bg = "#351c75")
    home_page.geometry("1600x900")  
    menu_Frame = tk.Frame(home_page, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    #creates the size for the window and the menu bar, as well as the background colour
    buttonLi = tk.Button(menu_Frame, text = "Signup/Login", command = lambda: Linker(home_page), width = 20, height = 2)
    buttonLi.pack(side = tk.LEFT, padx = 20)
    #Creates the button to allow the user to access the SignUp/Login linker page
    buttonE = tk.Button(menu_Frame, text = "Employee Access", width = 20, height = 2, command = lambda: emplin(home_page))
    buttonE.pack(side = tk.LEFT, padx = 20)
    #Allows the user to open the Employee Page, and will be checked to ensure that they will have sufficient permission to access the data
    buttonbas = tk.Button(menu_Frame, width = 20, height = 10, command = lambda: ordhold(home_page))
    buttonbas.pack(side = tk.RIGHT, padx = 20)
    #Creates the button that allows the user to access the order display window
    button_search = tk.Button(home_page, width = 15, height = 5, text  = "Search", command = lambda: search_results(search_e, home_page))
    button_search.place(x =850, y = 200)
    #Creates a button that allows the user to access the Search Results window
    search_e = tk.Entry(home_page)
    search_e.place(x = 550 , y = 200, width = 300, height =60)
    #Allows the user to input a search variable to specify the products they are searching for
    home_page.mainloop()
    #Establishes the window








def save_user(entryfn, entrysn, entryp, entrye, entryad, entryun, entrypw, entrypw2, register, buttone):
    fname = entryfn.get()
    sname = entrysn.get()
    Email = entrye.get()
    Phone = entryp.get()
    address = entryad.get()
    uname = entryun.get()
    pword1 = entrypw.get()
    pword2 = entrypw2.get()
    Valid = True
    #Ensures the function can access the data input into the entries on the Sign up page


    def reset():
        buttone.config(text = "login", fg = "black")
    #Resets the text on the button back to its original state
   
    def error(text):
        buttone.config(text = text, fg = "red")
        register.after(1000, reset)
    #Displays an error message to inform the user of invalid data beinmg input
    #Alters the text on the button to match the error message before restoring the original text after 1000 milliseconds




    if len(fname) < 1:
        error("Input First Name")
        Valid = False
    #Ensusres that there is data input into the entry, else the error is triggered
   
    if len(sname) < 1:
        error("Input Second Name")
        Valid = False
    #Ensures that there is data input into the entry, esle the error is triggered
   
   
    found = Email.find("@")
    found2 = Email.find(".")
    if found == - 1 or found2 == - 1:
        error("Email not valid")
        Valid = False
    #Ensures the data is in the correct format for an email (contains @ and .), else the error is triggered


    if not(Phone.isdigit()) and len(Phone) < 11 or len(Phone) > 11:
        error("Input Valid Phone Number")
        Valid = False
    #Ensures that the length of the Phone number is correct, else the error is triggered


    if len(address) < 1:
        error("Please Input Address")
        Valid = False
    #Ensures there is data input into the entry, else the error is triggered




    if pword1 != pword2:
        error("passwords don't match")
        Valid = False
    #Compares the two passwords entered into the entries, and if they do not match, then the error is called
       
    if not Valid:
        return
    #If any of the data is invalid, then this boolean ensures that the data is not accidentaly saved to file, which would cause errors in the database
       
    try:
        with open("users.pkl", 'rb') as file:
            users = pickle.load(file)
            for i in range(len(users)):
                if users[i].uname == uname:
                #Checks if the username already exists
                    error(uname, "already exists, choose another")
                    return
            pkey = len(users)+1
            temp = User(pkey, uname, pword1, fname, sname, Email, address, Phone)
            users.append(temp)
            #Appends the newly entred data to the pre-existing data list
            with open('users.pkl', 'wb') as file:
                pickle.dump(users, file)
            #The new data is added to the file in the specified format
            register.destroy()
            #Destroys the Register window
            homepage()
            #Opens the Homepage after successful signup
    except:
        #Runs an exception in case there is no data in the file, or the file does not exist
        users = []
        pkey = 1
        temp = User(pkey, uname, pword1, fname, sname, Email, address, Phone)
        users.append(temp)
        with open('users.pkl', 'wb') as file:
            pickle.dump(users, file)
            messagebox.showinfo("Account Creation:", "Account created Successfully")
            register.destroy()
            homepage()
           
current_user_id = None
current_username = None
#Creates two global variables which can be called to obtain user details later in the program
           
def get_user_details(username):
    global user_details_string
    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
        for user in users:
            if user.uname == username:
                    user_details_string = f"User  Details:\nUserID: {user.userID}\nUsername: {user.uname}\nFirst Name: {user.fname}\nLast Name: {user.sname}\nEmail: {user.email}\nAddress: {user.address}\nPhone: {user.phone}"
                    return user_details_string
            #Creates a string of user details for use in programs such as adding orders and checking out.
    return "User  not found."
    #Runs an exception if the user is not found in the file


   
def login_user(entryun, entrypw, login_screen, buttone):
    global current_user_id, current_username
    uname = entryun.get()
    pword = entrypw.get()
    valid = False
    #Obtains the data from the entries in the login screen as well as sets the boolean Valid to False
   
    def reset():
        buttone.config(text = "login", fg = "black")
    #Resets the login button to its original state
   
    def error(text):
        buttone.config(text = text, fg = "red")
        login_screen.after(1000, reset)
    #Creates the error message, which is displayed on the login button, and then reset after 1000 seconds


    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
        for user in users:
            if user.uname == uname and user.pword == pword:
                valid = True
                #Ensures the username and password match the data in the database, else the error is called
                current_user_id = user.userID
                current_username = user.uname
                #Adds the relevant data to the global variables
                login_screen.destroy()
                #Destroys the window
                messagebox.showinfo("Successful Login", "You are logged in")
                user_details = get_user_details(uname)
                #Calls the user details function to ensure that the data matches the user currently logged in
                homepage()
                #Opens the Homepage after successful login
                return


        if not valid:
            error("Username or Password not found")
            return


def Linker(home_page):
    home_page.destroy()
    linker = tk.Tk()
    linker.resizable(False, False)
    #Prevents the user from resizing the window and causing issues with the menu bar and button placement.
    linker.config(bg = "#351c75")
    linker.geometry("1600x900")  
    menu_Frame = tk.Frame(linker, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    #Establishes the Linker window size, background and menu frame.
    buttonr = tk.Button(linker, width = 40, height = 6, bg = "#e8d619", font = ("Prompt", 20), text = ("Sign Up"), command = lambda: register_form(linker, home_page))
    buttonr.place(x = 100, y = 600)
    #Creates the button that allows the user to access the Register page, where they can create a new account
    buttonl = tk.Button(linker, width = 40, height = 6, bg = "#e8d619", font = ("Prompt", 20), text = "Login", command = lambda: login(linker, home_page))
    buttonl.place(x = 850, y = 600)
    #Creates the button that allows the user to access the login page, to sign into a pre-existing account
    labelSU = tk.Label(linker, width = 50, height = 6, font = ("Prompt", 20), fg = "white", bg = "#351c75", text = "Click here to create an account:")
    labelSU.place(x = 65, y = 450)
    labelLG = tk.Label(linker, width = 50, height = 6, font = ("Prompt", 20), fg = "white", bg = "#351c75", text = "If you already have an account, click here to log in:")
    labelLG.place(x = 785, y = 450)
    #Places labels above the respective buttons, informing the user which window would be appropriate to use.


    def backs():
        linker.destroy()
        homepage()
    #Destroys the linker window and reopens the home page window


    buttonb = tk.Button( menu_Frame, text = "Back", command = backs)
    buttonb.pack(side = tk.LEFT, padx = 20)
    #Creates the back button to allow the user to go back to the previous page
    linker.mainloop()
    #Ensures the window remains open suring use
 
def login(linker, home_page):
    global username
    #Establishes the global variable to allow the get_user_data function to access the correct data for the current user logged in
    linker.destroy()
    #Destroys the linker window
    login_screen = tk.Tk()
    login_screen.resizable(False, False)
    #Prevents the user from resizing the window
    login_screen.config(bg="#351c75")
    login_screen.geometry("1600x900")  
    menu_Frame = tk.Frame(login_screen, width=1600, height=60, bg="#8e7cc3")
    menu_Frame.place(x=0, y=75)
    menu_Frame.pack_propagate(False)
    #Establishes the Login window, as well as the size, background and menu bar
   
    labelun = tk.Label(login_screen, width=50, height=6, font=("Prompt", 15), text="Username")
    labelun.place(x=900, y=300)
    #Labes the Username entry to distinguish the entry to allow for better navigation


    entryun = tk.Entry(login_screen, font=("Prompt", 15), bg="#b7b7b7")
    entryun.place(x=300, y=300, width=500, height=140)
    #Creates the Username entry, which data can be taken from and compared
   
    labelpw = tk.Label(login_screen, width=50, height=6, font=("Prompt", 15), text="Password")
    labelpw.place(x=900, y=500)
    #Labels the password entry to distinguish between it and the username entry.
   
    entrypw = tk.Entry(login_screen, font=("Prompt", 15), bg="#b7b7b7", show="*")
    entrypw.place(x=300, y=500, width=500, height=140)
    #Creates the Password entry for the usedr to input data
   
    loginframe = tk.Frame(login_screen, width=1600, height=60, bg="#8e7cc3")
    loginframe.place(x=0, y=840)
    loginframe.pack_propagate(False)
    #creates the frame on the bottom of the window for the login button to be placed in
   
    buttone = tk.Button(loginframe, width=40, height=6, bg="#e8d619", font=("Prompt", 20), text="login", command=lambda: login_user(entryun, entrypw, login_screen, buttone))
    buttone.pack()
    #Creates the login button, which when clicked, calles the login_user function, logging in the user if the data is valid
   
    username = entryun.get()
    #Assigns the data to the global variable relating to the current user logged in
       
    login_screen.mainloop()
    #Ensures the window remains open during use


def register_form(linker, home_page):
    linker.destroy()
    #Destroys the Liknker window when the register window is opened
    register = tk.Tk()
    register.resizable(False, False)
    #Prevents the window from being resized
    register.config(bg = "#351c75")
    register.geometry("1600x900")  
    menu_Frame = tk.Frame(register, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    #Establishes the register window, as well as its size, background and menu frame
    labelfn = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "First Name")
    labelfn.place(x = 900, y = 150)
    entryfn = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entryfn.place(x = 450, y = 150)
    labelsn = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Second Name")
    labelsn.place(x = 900, y = 225)
    entrysn = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrysn.place(x = 450, y = 225)
    labele = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Email")
    labele.place(x = 900, y = 300)
    entrye = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrye.place(x = 450, y = 300)
    labelad = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Address")
    labelad.place(x = 900, y = 375)
    entryad = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entryad.place(x = 450, y = 375)
    labelp = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Phone")
    labelp.place(x = 900, y = 450)
    entryp = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entryp.place(x = 450, y = 450)
    labelun = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Username")
    labelun.place(x = 900, y = 525)
    entryun = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entryun.place(x = 450, y = 525)
    labelpw = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Password")
    labelpw.place(x = 900, y = 600)
    entrypw = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7", show = "*")
    entrypw.place(x = 450, y = 600)
    labelpw2 = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Re-Enter Password")
    labelpw2.place(x = 900, y = 675)
    entrypw2 = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7", show ="*")
    entrypw2.place(x = 450, y = 675)
    sframe = tk.Frame(register, width = 1600, height = 80, bg = "#8e7cc3")
     #Creates the various Lables and entries for users to input relavent data into in order to create an account
    sframe.place(x = 0, y = 820)
    sframe.pack_propagate(False)
    buttone = tk.Button(sframe, width = 40, height = 9, bg = "#e8d619", font = ("Prompt", 20), text = "save", command = lambda : save_user(entryfn, entrysn, entryp, entrye, entryad, entryun, entrypw, entrypw2, register, buttone))
    buttone.pack()
    #Creates the sign_up button, which calls the sign_up funtion, saving the data to the User file and creates an account if the data is valid
   
    register.mainloop()
    #Ensures the window remains open suring execution




def search_results(search_e, home_page):
    global user_details_string
    search_string = search_e.get().lower()
    #Ensures the function can access the user_details_string and the search_e variable from the homepage
    search = tk.Tk()
    search.resizable(False, False)
    #Ensures the window can't be resized
    search.config(bg = "#351c75")
    search.geometry("1600x900")  
    menu_Frame = tk.Frame(search, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    #Establishes the Search results window, as well as its size, background and menu frame
    home_page.destroy()
    #Destroys the homepage after the search string data has been assigned from the obtained variable.
    with open("toys.pkl", 'rb') as file:
        toys = pickle.load(file)
    #Opens the Toys PKL file and saves the contents to the toys variable
    toy_list = []
    for i in range (len(toys)):  
        if search_string in toys[i].Name.lower() or search_string in toys[i].prodesc.lower():
            toy_list.append(toys[i])
    #Appends each product in the the Toys variable to the Toy_list list if it matches the search variable input by the user


    toys_found = []
    #Creates the Toys_found list
    for i in range(len(toy_list)):
        temp = toy_list[i].Name, "£"+ toy_list[i].prodprice
        toys_found.append(temp)
    #Appends the Name and Price of each product that matches the search variable to the Toys_found list
   


    lboxtoys = tk.Listbox(search, height = 17, width = 106, font = ("Prompt", 20), selectmode=tk.SINGLE)
    #Eatablishes the listbox size and other attributes


    for i in range(len(toys_found)):
        lboxtoys.insert(tk.END, toys_found[i])
    #Inserts the contents of the Toys_found list into the list box


    scrollbar = tk.Scrollbar(search, orient=tk.VERTICAL, command=lboxtoys.yview)
    lboxtoys.config(yscrollcommand=scrollbar.set)
    #Creates the scrollbar to navigate the listbox with


    lboxtoys.place(x = 0, y = 200)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    #Places the Listbox and scrollbar onto the window
   
    try:
        get_user_details(username)
    except:
        messagebox.showinfo("User not logged in:", "Please Log in or create a new account")
    #Attempts the obtain the user details, if none exist, then the error box is called
   
    lboxtoys.bind("<<ListboxSelect>>", lambda event: Proddisplay(lboxtoys, toys, user_details_string, search))
    #Binds the listox to the current window
   
    def backs():
        search.destroy()
        homepage()
        #Destroys the window and opens the homepage


    buttonb = tk.Button( menu_Frame, text = "Back", command = backs)
    buttonb.pack(side = tk.LEFT, padx = 20)
    #Creates and places the back button onto the window
   
    search.mainloop()
    #Ensures the window remains open during execution


def Proddisplay(lboxtoys, toys, users, search):
    index = lboxtoys.curselection()[0]
    toy_n = toys[index]
    #Establishes the toy_n and index variables from the selected value on the listbox on the Search_results window
    prod = tk.Tk()
    prod.resizable(False, False)
    prod.config(bg = "#351c75")
    prod.geometry("1600x900")  
    menu_Frame = tk.Frame(prod, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    bottom = tk.Frame(prod, width=1600, height = 60, bg="#8e7cc3")
    bottom.place(x = 0, y = 940)
    bottom.pack_propagate(False)
    #Establishes the window as well as the necassary attributes such as background, size and the me3nu frames
    lbn = tk.Label(prod, text = toy_n.Name, font = ("Prompt", 30))
    lbn.place(x = 250, y = 200)
    lbp = tk.Label(prod, text = '£'+ toy_n.prodprice, font = ("Prompt", 30))
    lbp.place(x = 250, y = 350)
    lbd = tk.Label(prod, text = toy_n.prodesc, font = ("Prompt", 30))
    lbd.place(x = 250, y = 550)
    #Creates the labels which contain the data attributed to the product selected from the listbox on the previous window
   
    def addtoorder():
        global current_user_id, current_username
        #Calls the global variables so that the function is able to access them
        curorder_string = f"User  ID: {current_user_id}, Username: {current_username}, ProductID: {toy_n.prodID}, ProductName: {toy_n.Name}, ProductPrice: £{toy_n.prodprice}"
        #Defines the current order string, if one exists, with the correct attributes
        orders_file_path = 'temp_orders.pkl'
        #Opens the Temporary orders PKL file
        if not os.path.exists(orders_file_path):
            with open(orders_file_path, 'wb+') as f:
                pickle.dump([], f)
        #If the file doesn't exist, the function creates a new file called temp_orders.pkl


        try:
            with open(orders_file_path, 'rb') as f:
                existing_orders = pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            existing_orders = []
        #Attempts to load the current ordedr string from the temp orders file, however if there is none, then the try, except function works to prevent a system crash
        #and loads an empty form the existing orders string for data to be appended to.


        total_price = float(toy_n.prodprice)  
        for order in existing_orders:
            total_price += float(order['ProductPrice'])
        #Calculates the total price of the current order


        new_order = {
            'User  ID': current_user_id,
            'Username': current_username,
            'ProductID': toy_n.prodID,
            'ProductName': toy_n.Name,
            'ProductPrice': toy_n.prodprice,
            'TotalPrice': str(total_price)
        }
        #Assigns the correct variables to the attributes of the order object


        existing_orders.append(new_order)
        with open(orders_file_path, 'wb') as f:
            pickle.dump(existing_orders, f)
        #Appends the new order string into the temp_orders file to be called at another point


        prod.destroy()
        #Destroys the window


    buttonor = tk.Button(prod, width=30, height=4, bg="#e8d619", font=("Prompt", 20), text="Add to Order", command=lambda: addtoorder())
    buttonor.place(x=500, y=700)
    #places the add to order button onto the window, which calls the addtoorder function to add the product to a temporary order string


    def backs():
        prod.destroy()
        search_results()
    #Destoys the current window and allows the user to return to the search_results window


    buttonb = tk.Button( menu_Frame, text = "Back", command = backs)
    buttonb.pack(side = tk.LEFT, padx = 20)
    #Places the back button onto the window


    prod.mainloop()
    #Ensures the window remains open during execution
def ordhold(home_page):
    home_page.destroy()
    #Destroys the home page
    orderdisp()
   
def orderdisp():
   
    def reset():
        buttonch.config(text = "Checkout", fg = "black")
    #Resets the checkout button back to its original state
   
    def error(text):
        buttonch.config(text = text, fg = "red")
        orderd.after(1000, reset)
    #Alters the text of the checkout button to be the error message, which is reset after 1000 milliseconds


    orderd = tk.Tk()
    orderd.resizable(False, False)
    #Prevents the windpw from being resized
    orderd.config(bg = "#351c75")
    orderd.geometry("1600x900")  
    menu_Frame = tk.Frame(orderd, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    oframe = tk.Frame(orderd, width = 1600, height = 80, bg = "#8e7cc3")
    oframe.place(x = 0, y = 820)
    oframe.pack_propagate(False)
    #Establishes the window and any necesarry attributes such as the frames and background
   
    labelad = tk.Label(orderd, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", fg = "#e4eff1",  text = "Address")
    labelad.place(x = 720, y = 360)
    entryad = tk.Entry(orderd, width = 20, font = ("Prompt", 15), bg = "#b7b7b7", fg = "#e4eff1")
    entryad.place(x = 550, y = 375)
    #Creates the address label and entry to allow for users to input their address
   
    user_label = tk.Label(orderd, text=f":User   {current_username}", font=("Prompt", 15), bg="#351c75", fg = "#e4eff1")
    user_label.place(x = 680, y = 300)
    #Creates and places the username label onto the window


    total_price_label = tk.Label(orderd, text = "Total Price: £0.00", font = ("Prompt", 15), bg="#351c75", fg = "#e4eff1")
    total_price_label.place(x = 670, y = 700)
    #Creates and places the total order price label onto the window


    orders_file_path = 'temp_orders.pkl'
    if os.path.exists(orders_file_path):
        try:
            with open(orders_file_path, 'rb') as file:
                orders = pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
             orders = []
    else:
        orders = []
    #Creates the orders file path to the temp_orders file, and creating a contingency for if the file is empty(the try and except function)
    #or if it doesn't exist(the else function) to ensure the program can still run without crashing.


    lboxorders = tk.Listbox(orderd, height = 10, width = 50, font =  ("Prompt", 15), selectmode=tk.SINGLE)
    lboxorders.place(x = 500, y = 430)
    #Establishes the listbox and places it onto the window
   
    scrollbar = tk.Scrollbar(orderd, orient = tk.VERTICAL, command=lboxorders.yview)
    lboxorders.config(yscrollcommand = scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    #Establishes the scrollbar and places it onto the window


    def calculate_total_price(order_items):
        total_price = sum(float(item['ProductPrice']) for item in order_items)
        #calculates the total price of the the order by adding each product price together


        with open("users.pkl", 'rb') as file:
            users = pickle.load(file)
        #Opens the users file and loads the contents to a variable


        for user in users:
            if user.uname == current_username:
                if user.member:
                    total_price *= 0.7  
                break
        #Checks if a user is a member, and then removes 30% of the total price


        return total_price
   
    total_price = calculate_total_price(orders)  
    total_price_label.config(text=f"Total Price: £{total_price:.2f}")
    #Appends the total price value to the variable and configures the label to display it


    for order in orders:
        toy_string = f"{order['ProductName']} - £{order['ProductPrice']}"
        lboxorders.insert(tk.END, toy_string)
    #Inserts the products in the order into the listbox


    def delete():
            selected_index = lboxorders.curselection()
            if selected_index:
                selected_item = lboxorders.get(selected_index)
                product_name = selected_item.split(" - ")[0]
                #gets the item selected from the listbox
                for order in orders:
                    if order['ProductName'] == product_name:
                        orders.remove(order)
                        fix = orders
                    #Removes the data attributed to the selected product from the order
                        with open('temp_orders.pkl', 'wb') as file:
                            pickle.dump(fix, file)
                    break

                lboxorders.delete(selected_index)
            nonlocal total_price
            total_price = lambda:calculate_total_price(orders)
            total_price_label.config(text=f"Total Price: £{total_price:.2f}")
            #recalculates and reappends the total price of the order 



   


    buttonre = tk.Button(oframe, width = 8, height = 3, text = "Delete", command = delete, font = ("Prompt", 15))
    buttonre.place(x = 950, y = 0)
    #creates and places the delete button onto the window, calling the delete function when clicked


    buttonch = tk.Button(oframe, width = 25, height = 3, text = "Checkout", command = lambda: checkout(orderd, entryad), font = ("Prompt", 15))
    buttonch.place(x = 400, y = 0)
    #creates and places the checkout button onto the window, which opens the checkout window when clicked


    def backs():
        orderd.destroy()
        homepage()
        #destroys the current window and opens the previous one


    buttonb = tk.Button(menu_Frame, text = "Back", command = backs)
    buttonb.pack(side = tk.LEFT, padx = 20)
    #Creates and places the back button whcih calls the back command
   
    orderd.mainloop()
    #Ensures the window remains open during execution


def checkout(orderd, entryad):
    address = entryad.get()
    orderd.destroy()
    #Destroys the window after the necassary data has been extracted in regards to the address entry
    check_out = tk.Tk()
    check_out.resizable(False, False)
    #Prevents the window being resized
    check_out.config(bg="#351c75")
    check_out.geometry("1600x900")
    menu_Frame = tk.Frame(check_out, width=1600, height=60, bg="#8e7cc3")
    menu_Frame.place(x=0, y=75)
    menu_Frame.pack_propagate(False)
    oframe = tk.Frame(check_out, width=1600, height=80, bg="#8e7cc3")
    oframe.place(x=0, y=820)
    oframe.pack_propagate(False)
    #Creates the window, along with the necassary attributes such as the menu bars, background colour etc
   
    orders_file_path = 'temp_orders.pkl'
    if os.path.exists(orders_file_path):
        try:
            with open(orders_file_path, 'rb') as file:
                orders = pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            orders = []
        #Prevents the system from crashing if the file is empty or does not exist
    else:
        orders = []
    #Creates the file path to access the temporary order file


    def calculate_total_price(order_items):
        total_price = sum(float(item['ProductPrice']) for item in order_items)


        with open("users.pkl", 'rb') as file:
            users = pickle.load(file)
        #Calculates and updates the total price of the orders and places it in file
        for user in users:
            if user.uname == current_username:
                if user.member:
                    total_price *= 0.7  
                break
            #Checks if the user is a member and provieds a 30% discount if they are
            #by multiplying the value by 0.7


        return total_price


    total_price = calculate_total_price(orders)  
    #Calls the total Price calculation function


    delivery_option_var = tk.StringVar(value="in store pickup")
    delivery_options = tk.OptionMenu(check_out, delivery_option_var, "in store pickup", "home delivery", command=lambda _: update_delivery_type_dropdown())
    delivery_options.place(x=670, y=350)
    #Creates tje dropdown menu for delivery options and p;laces it onto the window


    labeldis = tk.Label(check_out, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", fg = "#e4eff1",  text = "Enter discount code")
    labeldis.place(x = 720, y = 760)
    entrydis = tk.Entry(check_out, width = 20, font = ("Prompt", 15), bg = "#b7b7b7", fg = "#e4eff1")
    entrydis.place(x = 550, y = 775)
    #Creates the address label and entry to allow for users to input a discount code


    total_price_label = tk.Label(check_out, text=f"Total Price: £{total_price:.2f}", font=("Prompt", 15), bg="#351c75", fg="#e4eff1")
    total_price_label.place(x=670, y=700)
    #Applies the total price variable to the label


    delivery_type_var = tk.StringVar(value="standard")
    delivery_type_dropdown = tk.OptionMenu(check_out, delivery_type_var, "standard", "premium")
    delivery_type_dropdown.place(x=670, y=400)
    delivery_type_dropdown.config(state='disabled')
    #Creates the dropdown menu for delivery selection, however is defaulted to disabled until the opion for home delivery is selected


    def update_delivery_type_dropdown():
        if delivery_option_var.get() == "home delivery":
            delivery_type_dropdown.config(state='normal')
            #Specifies the dropdown to only be in its 'normal' state when the home delivery option is selected
        else:
            delivery_type_dropdown.config(state='disabled')
            delivery_type_var.set("standard")
            #Ensures the menu remains disabled at all other times
   
    def apply_discount_code(code):
        code_file_path = 'discount_codes.pkl'
        try:
            with open(code_file_path, 'rb') as f:
                existing_codes = pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            existing_codes = []


        for discount in existing_codes:
            if discount.code == code:
                return float(discount.value)




        return 0.0  # Return 0 if the code is invalid




    discount_code = entrydis.get()
    discount_value = apply_discount_code(discount_code)
    #Creates the variables for the discount code and the attributes associated with it.
    total_price -= discount_value
    #Subtracts the value of the discount code from the total price variable. 


    def add_order(total_price):  #Parse total_price as a parameter
        main_orders_file_path = 'orders.pkl'
        if os.path.exists(main_orders_file_path):
            with open(main_orders_file_path, 'rb') as file:
                existing_orders = pickle.load(file)
            #Creates a file path by opening the order file and appends the pre-existing data to a list
        else:
            existing_orders = []
            #If there is no data found, the list is declared as blank


        if len(address) < 1:
            messagebox.showerror("Error", "Please enter/re-enter your address")
            return
        #Ensures there is data input into the address entry

        with open("toys.pkl", 'rb') as file:
            toys = pickle.load(file)
            #Opens the toys file and loads the data into a list

        for order in orders:
                for toy in toys:  # Ensure that toy is an instance of Product
                    if isinstance(toy, Product):  # Check if toy is a Product instance
                        if toy.Name == order['ProductName']:
                            number = int(toy.stocknum)
                            number -= 1
                            break
                    elif isinstance(toy, dict):  #Checks to see if the toy is in dictionary form
                        if 'Name' in toy and toy['Name'] == order['ProductName']:
                            number = int(toy['stocknum'])
                            number -= 1
                            break
                    #If a product is present in the order being places, it's stock number is decreased by the amount of that product is in the order


        order['Address'] = address
        existing_orders.append(order)
        #Appends the address data to the order string


        if delivery_option_var.get() == "home delivery":
            if delivery_type_var.get() == "premium":
                total_price = float(total_price) + 4.99
        #Adds the premium delivery fee to the total price
                total_price_label.config(text=f"Total Price: £{total_price:.2f}")


        total_price_label.config(text=f"Total Price: £{total_price:.2f}")
        #Ensures the value displayed on the label is updated


        update_user_order_count(current_user_id)
        #Calls the function to update the number of orders a user has placed

        with open("toys.pkl", 'wb') as file:
            pickle.dump(toys, file)
        #Appends the updated data to the Toys file


        with open(main_orders_file_path, 'wb+') as file:
            pickle.dump(existing_orders, file)
        #Appends the new order to the orders file


        openfile = open("temp_orders.pkl", "w")
        openfile.close()
        #Clears the temp_orders file ready for the next order


        messagebox.showinfo("Order:", "Order placed successfully")
        check_membership_eligibility(current_user_id)
        #Calls the check user membership eligability function
        homepage()
        check_out.destroy()
        #Displays a message informing the user thier order has been placed
        #Destroys the checkout window and calls the home page to open


    def update_user_order_count(current_user_id):
        with open("users.pkl", 'rb') as file:
            users = pickle.load(file)
        #Opens the user file and loads the data into a file


        for user in users:
            if user.userID == current_user_id:
                user.order_count += 1
                break
        #Finds the currently logged in user and updates their order count by 1


        with open("users.pkl", 'wb') as file:
            pickle.dump(users, file)
        #Appends the data to file


    def check_membership_eligibility(current_user_id):
        with open("users.pkl", 'rb') as file:
            users = pickle.load(file)
    # Opens the user file and loads the data into a list


        for user in users:
            if user.userID == current_user_id:
                if user.order_count >= 3 and not user.member:
                    # Check if the user is eligible for membership
                    response = messagebox.askyesno("Become a Member",
                        "You have placed 3 orders! Would you like to become a member and receive a 30% discount?")
                   
                    if response:
                        user.member = True  # Update the user's membership status
                        with open("users.pkl", 'wb') as file:
                            pickle.dump(users, file)  # Save the updated user list
                        messagebox.showinfo("Membership",
                            "Congratulations! You are now a member and will receive a 30% discount on future orders.")
                    break  # Exit the loop after processing the current user


    buttonch = tk.Button(oframe, width=25, height=3, text="Place Order", command=lambda: add_order(total_price), font=("Prompt", 15))
    buttonch.place(x=400, y=0)
    #Creates and places the add order button  onto the window and calls the add order function when clicked


    def backs():
        check_out.destroy()
        orderdisp()
    #Destroys the current windoew and calls the homepage to open


    buttonb = tk.Button(menu_Frame, text="Back", command=backs)
    buttonb.pack(side=tk.LEFT, padx=20)
    #Creates and places the back button


    check_out.mainloop()
    #Ensures the window remains open during execution


def emplin(home_page):
    home_page.destroy()
    empwin()


def empwin():
    if not any(user.staff for user in pickle.load(open("users.pkl", "rb")) if user.uname == current_username):
        messagebox.showerror("Access Denied", "You do not have permission to access this area.")
        return
        #Ensures the user logging into the system has the appropriate permission to access this section of the file, otherwise they are prevented by doing so
        #Error messagebox informs the user they do not have the correct permissions
    employee = tk.Tk()
    employee.resizable(False, False)
    #Prevents the window being resized
    employee.config(bg = "#351c75")
    employee.geometry("1600x900")  
    menu_Frame = tk.Frame(employee, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    #Creates the window and all the necessary attributes such as the frames and the background colour
    buttonUs = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Users Database"), command = lambda: Userdb())
    buttonUs.place(x = 200, y = 600)
    #Creates and places the user database window, which calls the Userdb function when clicked
    buttonOr = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Order Log"), command = lambda: OrderLog())
    buttonOr.place(x = 900, y  =600)
    #Creates and places the Order Log window, which calls the OrderLog function when clicked
    buttonSt = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Stock Database"), command = lambda: stockhold(employee))
    buttonSt.place(x = 900 , y = 200)
    #Creates and places the Stock database window, which calls the Stockdata function when clicked
    def backs():
        employee.destroy()
        homepage()
    #Destroys the window and opens the home page
    buttonb = tk.Button( menu_Frame, text = "Back", command = backs)
    buttonb.pack(side = tk.LEFT, padx = 20)
    #Creates and places the Back button which calls the backs function when clicked
    employee.mainloop()


def Userdb():
    admin_window = tk.Tk()
    admin_window.resizable(False, False)
    #Prevents the window being resized
    admin_window.config(bg = "#351c75")
    admin_window.geometry("800x800")
    menu_Frame = tk.Frame(admin_window, width = 800, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    #Creates the window with all the necassary attributes such as the frames and background colour
    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
    #Opens the userss file and appends the data to a list


    user_listbox = tk.Listbox(admin_window, width = 133, height = 26)
    for user in users:
        user_listbox.insert(tk.END, f"{user.uname} (Staff: {user.staff}) (Member: {user.member}) (Orders: {user.order_count})")
    user_listbox.place(x = 0, y = 140)
    #Creates the listbox and appends the specified user data to the list


    def toggle_staff():
        selected_index = user_listbox.curselection()
        #ensures only the selected user data is affected
        if selected_index:
            user = users[selected_index[0]]
            user.staff = not user.staff
            #Flips the selected users staff permission, changing it to true
            with open("users.pkl", 'wb') as file:
                pickle.dump(users, file)
            #Appends the new data to the user file
            user_listbox.delete(selected_index)
            user_listbox.insert(selected_index, f"{user.uname} (Staff: {user.staff}) (Member: {user.member}) (Orders: {user.order_count})")
            #Updates the listbox to dsiplay the new staff permission value


    toggle_button = tk.Button(admin_window, width = 15, height = 3, bg = "#e8d619", font = ("Comfortaa", 15), text = ("Toggle Staff Status"), command=toggle_staff)
    toggle_button.place(x = 340, y = 600)
    #Creates and places the toggle staff button, which calls the function when clicked
    admin_window.mainloop()
       


def OrderLog():
    order_window = tk.Tk()
    order_window.resizable(False, False)
    #Prevents the window being resized
    order_window.config(bg = "#351c75")
    order_window.geometry("800x800")
    menu_Frame = tk.Frame(order_window, width = 800, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    #Creates the window with all the necessary attributes such as the frames and background colour


    with open("orders.pkl", 'rb') as file:
        order_list = []
        orders = pickle.load(file)
        order_list.append(orders)
    #Opens the Orders file and appends the data to a list




    order_listbox = tk.Listbox(order_window, width = 133, height = 26)
    for i in range(len(order_list)):
        order_listbox.insert(tk.END, order_list[i])
    order_listbox.place(x = 0, y = 140)
    #initialises a listbox and inserts all of the order data from the appended list


    order_window.mainloop()
    #Ensures the window remains open duting execution
def stockhold(employee):
    employee.destroy()
    stockdata()


def stockdata():
    stock = tk.Tk()
    stock.resizable(False, False)
    #Prevents the window being resized
    stock.config(bg = "#351c75")
    stock.geometry("1600x900")  
    menu_Frame = tk.Frame(stock, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    sframe = tk.Frame(stock, width = 1600, height = 80, bg = "#8e7cc3")
    sframe.place(x = 0, y = 820)
    sframe.pack_propagate(False)
    #Creates the window with all the necassary attributes such as the frames and background colour
   
    def plus():
        selection = lboxtoys.curselection()[0]
        if len(str(selection)) == 0:
            return
        #Obtains the selected data from the listbox
        if int(toys[selection].stocknum) < 999:
            toys[selection].stocknum = int(toys[selection].stocknum) + 1
            with open('toys.pkl', 'wb') as file:
                pickle.dump(toys, file)

            stock.destroy()
            stockdata()
        else:
            messagebox.showerror("Too much stock", "Cannot further incriment the stock number")
        #Increases the products stocknum value by one 

        #Updates the data in the Toys file
    def minus():
        selection = lboxtoys.curselection()[0]
        if len(str(selection)) == 0:
            return
        #Obtains the selected data from the listbox
        with open("toys.pkl", 'rb') as file:
            toys = pickle.load(file)
        if int(toys[selection].stocknum) >  0:
            toys[selection].stocknum = int(toys[selection].stocknum) -  1
            with open('toys.pkl', 'wb') as file:
                pickle.dump(toys, file)

            stock.destroy()
            stockdata()
        else:
            messagebox.showerror("Out of Stock", "Selected Product is out of stock")
        #Decreases the products stocknum value by one
        with open('toys.pkl', 'wb') as file:
            pickle.dump(toys, file)
        #Updates the data in the Toys file
           
    buttone = tk.Button(sframe, width = 25, height = 2, bg = "#e8d619", font = ("Prompt", 20), text = "Create New Stock", command = createstock)
    buttone.place(x =600, y = 0)
    #Creates and places the Create New Stock button, which calls the Createstock function when clicked
    buttond = tk.Button(sframe, width = 25, height = 2, bg = "#e8d619", font = ("Prompt", 20), text = "Add a New Discount Code", command = discount_create)
    buttond.place(x = 1000, y = 0)
    #Creates and places teh Add a New Discount Code button onto the window, which calls the discount_create function when clicked
    buttonM = tk.Button(sframe, width = 4, height = 2, font = ("Prompt", 20), text = "+", command = plus)
    buttonM.place(x = 100, y = 0)
    ButtonS = tk.Button(sframe, width = 4, height = 2, font = ("Prompt", 20), text = "-", command = minus)
    ButtonS.place(x = 200, y = 0)
    #Creates the plus and minus buttons and places them onto the window, which call the selected function when clicked


   
    with open("toys.pkl", 'rb') as file:
        toys = pickle.load(file)
    #Opens the userss file and appends the data to a list


    lboxtoys = tk.Listbox(stock, height = 28, width = 266, font =("Prompt", 15), selectmode=tk.SINGLE)
    #The listbox is initialised
    for Product in toys:
        lboxtoys.insert(tk.END, f"{Product.Name} (£: {Product.prodprice}) {Product.prodesc} {Product.stocknum}")
     #The necassary data is inserted into the listbox as an fstring


    scrollbar = tk.Scrollbar(stock, orient = tk.VERTICAL, command=lboxtoys.yview)
    #Creates the scrollbar and its arributes
    lboxtoys.config(yscrollcommand = scrollbar.set)
    #Configues the scrollbar to scroll through the listbox


    lboxtoys.place(x = 0, y = 150)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    #places the listbox onto the window and attatches the scrollbar to the right side of the window
    def backs():
        stock.destroy()
        empwin()
    #Destroys the current window and opens the mployee window
    buttonb = tk.Button( menu_Frame, text = "Back", command = backs)
    buttonb.pack(side = tk.LEFT, padx = 20)
    #Creates and places the back button onto the window
    stock.mainloop()
    #Ensures the window remains open during execution




def savestock(entrynam, entrypri, entrydesc, entrytag, stcreate, buttonsav):
    def reset():
        buttonsav.config(text = "Save Stock", fg = "black")
    #Resets the state of the button after the error message
    def error(text):
        buttonsav.config(text = text, fg = "red")
        stcreate.after(1000, reset)
    #Replaces the text on the button with the specified error text when called, resets to the original state after 1000 milliseconds
   
    Name = entrynam.get()
    prodesc = entrydesc.get()
    prodprice = '£' + entrypri.get()
    prodtags = entrytag.get()
    #Ensures the function is able to access the necassary variables to create a new product object
    try:
        with open("toys.pkl", 'rb') as file:
            toys = pickle.load(file)
            #Opens the toys file and saves the data to a list
            for i in range(len(toys)):
                if toys[i].Name == Name:
                    error("Product already exists")
                #Checks to see if the product being created already exists
                    return
                #Returns out of the function if it already exiss
            prodID = len(toys)+1
            stocknum = 1
            temp = Product(prodID, Name, prodesc, prodprice, prodtags, stocknum)
            toys.append(temp)
            with open('toys.pkl', 'wb') as file:
                pickle.dump(toys, file)
            #Saves the new product data to the toys file
                messagebox.showinfo("Product created", "Product created successfully")
            #Informs the user that the product has been creates succesfully
            stcreate.destroy()
            #Destroys the window once the function has complete
    except:
    #Runs if the toys file is empty to prevent crashes
        toys = []
        prodID = 1
        stocknum = 1
        temp = Product(prodID, Name, prodesc, prodprice, prodtags, stocknum)
        toys.append(temp)
        with open('toys.pkl', 'wb') as file:
            pickle.dump(toys, file)
            messagebox.showinfo("Product created", "Product created successfully")
        stcreate.destroy()
        #Saves the new data to the toys file and destroys the window
   
def createstock():
    stcreate = tk.Tk()
    stcreate.resizable(False, False)
    #Prevents the window being resized
    stcreate.config(bg = "#8e7cc3")
    stcreate.geometry("300x300")
    #Establishes the window and its necassary attributes
    labeln = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Name"))
    labeln.place(x= 30, y = 10)
    entrynam = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrynam.place(x = 30, y = 30)
    #Creates the label and entry for the product name and places them onto the window
    labelpri = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Price"))
    labelpri.place(x = 30, y = 60)
    entrypri = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrypri.place(x = 30, y = 80)
    #Creates the label and entry for the product price and places them onto the window
    labeldesc = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Description"))
    labeldesc.place(x = 30, y = 110)
    entrydesc = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrydesc.place(x = 30, y = 130)
    #Creates the label and entry for the product description and places them onto the window
    labeltag = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Tags"))
    labeltag.place(x = 30, y = 160)
    entrytag = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrytag.place(x= 30, y = 180)
    #Creates the label and entry for the product tags and places them onto the window
    buttonsav = tk.Button(stcreate, width = 10, height = 2, font = ("Prompt", 15), text = ("Create Stock"),  bg = "#e8d619", command = lambda: savestock(entrynam, entrypri, entrydesc, entrytag, stcreate, buttonsav))
    buttonsav.place(x = 125, y = 250)
    #Creates and places the Create stock button nonto the window, which calls the savestock function when clicked
    stcreate.mainloop()
    #Ensures the window remains open during execution


def discount_create():
    dccreate = tk.Tk()
    dccreate.resizable(False, False)
    #Prevents the window being resized
    dccreate.config(bg = "#8e7cc3")
    dccreate.geometry("300x300")
    #Establishes the window and its necassary attributes
    entrydc = tk.Entry(dccreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrydc.place(x = 70, y = 90)
    labeldc = tk.Label(dccreate, width = 20, font = ("Prompt", 15), bg = "#8e7cc3", fg = "white", text = ("Add New Discount Code:"))
    labeldc.place(x = 60, y = 50)
    #Creates and places both the discount code entry, and the label onto the window
    entryv = tk.Entry(dccreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entryv.place(x = 70, y = 170)
    labelv = tk.Label(dccreate, width = 20, font = ("Prompt", 15), bg = "#8e7cc3", fg = "white", text = ("Add Value:"))
    labelv.place(x = 60, y = 130)
    #Creates and places both the code value entry, and the label onto the window
    buttondisc = tk.Button(dccreate, width = 10, height = 2, font = ("Prompt", 15), text = ("Create Code"),  bg = "#e8d619", command = lambda: savecode(entrydc, entryv, buttondisc, dccreate))
    buttondisc.place(x = 115, y = 235)
    #Creates and places the Create Code buton onto the window, which calls the savecode function whenc clicked
    dccreate.mainloop()


def savecode(entrydc, entryv, buttondisc, dccreate):
    code = entrydc.get()
    value = entryv.get()
    # Ensures the function can access the entry variables

    def reset():
        buttondisc.config(text="Create Code", fg="black")
    # Resets the state of the button back to how it was

    def error(text):
        buttondisc.config(text=text, fg="red")
        dccreate.after(1000, reset)
    # Creates the error function which replaces the text of a button if called, which is reset
    # after 1000 milliseconds

    code_file_path = 'discount_codes.pkl'
    if not os.path.exists(code_file_path):
        with open(code_file_path, 'wb+') as f:
            pickle.dump([], f)
    # Creates the file path to the discount codes file
    # If the file doesn't exist, then it is created

    try:
        with open(code_file_path, 'rb') as f:
            existing_codes = pickle.load(f)
    # Loads the data from the file into a list
    except (EOFError, pickle.UnpicklingError):
        existing_codes = []
    # If the file is empty, creates an empty list and prevents the program from crashing

    # Check if the code already exists
    for discount in existing_codes:
        if discount.code == code:
            error("Code already exists")
            return  # Exit the function if the code already exists

    # If we reach here, the code does not exist, so we can add it
    temp = Discount(code, value)
    existing_codes.append(temp)
    # Appends the new code to the list

    # Save the new list to the file
    with open(code_file_path, 'wb+') as f:
        pickle.dump(existing_codes, f)
    # Saves the new list to the file

    dccreate.destroy()  # Destroys the window after saving

homepage()
#Calls the homepage function to start the program
