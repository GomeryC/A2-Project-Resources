import tkinter as tk
import pickle
from tkinter import PhotoImage
import sqlite3
import csv
import os
import pprint

class User:
    def __init__(self, userID, uname, pword, fname, sname, Email, address, phone):
        self.userID = userID
        self.uname = uname
        self.pword = pword
        self.fname = fname
        self.sname = sname
        self.email = Email
        self.address = address
        self.phone = phone
        self.staff = False
        self.admin = False

class Product:
    def __init__(self, prodID, Name, prodesc, prodprice, prodtags, stocknum):
        self.prodID = prodID
        self.Name = Name
        self.prodesc = prodesc
        self.prodprice = prodprice
        self.prodtags = prodtags
        self.stocknum = stocknum
        
    def __repr__(self) -> str:
        return f"Product(prodID={self.prodID}, name={self.Name}, prodesc={self.prodesc}, prodprice={self.prodprice}, prodtags={self.prodtags}, stocknum={self.stocknum})"

class Orders:
    def __init__(self, orderID, orderprice, userID, prodID):
        self.orderID = orderID
        self.orderprice = orderprice
        self.userID = userID
        self.prodID = prodID

def import_toys():
    try:
        with open("toys.csv", mode='r', newline='', encoding='ISO-8859-1') as file:
            csv_reader = list(csv.reader(file))
    except UnicodeDecodeError:
        with open("toys.csv", mode='r', newline='', encoding='utf-8', errors='replace') as file:
            csv_reader = list(csv.reader(file))

    toy_list = []
    for i in range(len(csv_reader)):
        temp = Product(csv_reader[i][0], csv_reader[i][1], csv_reader[i][2], csv_reader[i][3], csv_reader[i][4], int(csv_reader[i][7])) 
        toy_list.append(temp)
    pprint.pprint(toy_list)
    
    with open('toys.pkl', 'wb+') as file:
        pickle.dump(toy_list, file)
        print("Updated")
        pprint.pprint(Product) 

def import_users():
    try:
        with open("users.csv", mode='r', newline='') as file:
            csv_reader = list(csv.reader(file))
    except UnicodeDecodeError:
        with open("users.csv", mode='r', newline='') as file:
            csv_reader = list(csv.reader(file))

    user_list = []
    for i in range(len(csv_reader)):
        temp = User(csv_reader[i][0], csv_reader[i][1], csv_reader[i][2], csv_reader[i][3], csv_reader[i][4], csv_reader[i][5], csv_reader[i][6], csv_reader[i][7], csv_reader[i][8])
        user_list.append(temp)
    print(user_list)
    
    with open('users.pkl', 'wb') as file:
        pickle.dump(user_list, file)

def homepage():
    home_page = tk.Tk()
    home_page.resizable(False, False)
    home_page.config(bg="#351c75")
    home_page.geometry("1600x900")  
    menu_Frame = tk.Frame(home_page, width=1600, height=60, bg="#8e7cc3")
    menu_Frame.place(x=0, y=75)
    menu_Frame.pack_propagate(False)
    buttonLi = tk.Button(menu_Frame, text="Signup/Login", command=Linker, width=20, height=2)
    buttonLi.pack(side=tk.LEFT, padx=20)
    buttonE = tk.Button(menu_Frame, text="Employee Access", width=20, height=2, command=employee)
    buttonE.pack(side=tk.LEFT, padx=20)
    buttonbas = tk.Button(menu_Frame, width=20, height=10, command=orderdisp)
    buttonbas.pack(side=tk.RIGHT, padx=20)
    button_search = tk.Button(home_page, width=15, height=5, text="Search", command=lambda: search_results(search_e))
    button_search.place(x=850, y=200)
    search_e = tk.Entry(home_page)
    search_e.place(x=550, y=200, width=300, height=60)
    home_page.mainloop()




def save_user(entryfn, entrysn, entryp, entrye, entryad, entryun, entrypw, entrypw2, register):
    fname = entryfn.get()
    sname = entrysn.get()
    Email = entrye.get()
    Phone = entryp.get()
    address = entryad.get()
    uname = entryun.get()
    pword1 = entrypw.get()
    pword2 = entrypw2.get()
    Valid = True




    if len(fname) < 1:
        print("Please Input Your First Name")
        Valid = False
   
    if len(sname) < 1:
        print("Please Input Your Second Name")
        Valid = False
   
    
    found = Email.find("@")
    found2 = Email.find(".")
    if found == - 1 or found2 == - 1:
        print("Email not valid")
        Valid = False



    if not(Phone.isdigit()) and len(Phone) < 11 or len(Phone) > 11:
        print("Please Input A Valid Phone Number")
        Valid = False

    if len(address) < 1:
        print("Please Input Your Address")
        Valid = False



    if pword1 != pword2:
        print("passwords don't match")
        Valid = False
        
    if not Valid:
        return
        
    try:
        with open("users.pkl", 'rb') as file:
            users = pickle.load(file)
            for i in range(len(users)):
                if users[i].uname == uname:
                    print(uname, "already exists, choose another")
                    return
            pkey = len(users)+1
            temp = User(pkey, uname, pword1, fname, sname, Email, address, Phone)
            users.append(temp)
            with open('users.pkl', 'wb') as file:
                pickle.dump(users, file)
            register.destroy()
    except:
        users = []
        pkey = 1
        temp = User(pkey, uname, pword1, fname, sname, Email, address, Phone)
        users.append(temp)
        with open('users.pkl', 'wb') as file:
            pickle.dump(users, file)
            register.destroy() 
            
current_user_id = None
current_username = None
            
def get_user_details(username):
    global user_details_string
    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
        for user in users:
            if user.uname == username:
                    user_details_string = f"User  Details:\nUserID: {user.userID}\nUsername: {user.uname}\nFirst Name: {user.fname}\nLast Name: {user.sname}\nEmail: {user.email}\nAddress: {user.address}\nPhone: {user.phone}"
                    return user_details_string
    return "User  not found."

   
def login_user(entryun, entrypw, login_screen):
    global current_user_id, current_username
    uname = entryun.get()
    pword = entrypw.get()
    valid = False

    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
        for user in users:
            if user.uname == uname and user.pword == pword:
                valid = True
                current_user_id = user.userID
                current_username = user.uname
                login_screen.destroy()
                print("You are logged in")
                user_details = get_user_details(uname)
                homepage()
                return

        if not valid:
            print("Username or password not found")
            return


def login():
    global username
    login_screen = tk.Tk()
    login_screen.resizable(False, False)
    login_screen.config(bg = "#351c75")
    login_screen.geometry("1600x900")  
    menu_Frame = tk.Frame(login_screen, width = 1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    labelun = tk.Label(login_screen, width =50, height = 6,font = ("Prompt", 15), text = "Username")
    labelun.place(x = 900, y = 300)
    entryun = tk.Entry(login_screen, font = ("Prompt", 15), bg = "#b7b7b7")
    entryun.place(x = 300, y = 300, width = 500, height =140)
    labelpw = tk.Label(login_screen, width =50, height = 6, font = ("Prompt", 15), text = "Password")
    labelpw.place(x = 900, y = 500)
    entrypw = tk.Entry(login_screen, font = ("Prompt", 15), bg = "#b7b7b7")
    entrypw.place(x = 300, y = 500, width = 500, height = 140)
    loginframe = tk.Frame(login_screen, width = 1600, height  = 60, bg = "#8e7cc3")
    loginframe.place(x = 0, y  = 840)
    loginframe.pack_propagate(False)
    buttone = tk.Button(loginframe, width = 40, height = 6, bg = "#e8d619", font = ("Prompt", 20), text = "login", command = lambda: login_user(entryun, entrypw, login_screen))
    buttone.pack()
    username = entryun.get()
        
    login_screen.mainloop()
    






def register_form():
    register = tk.Tk()
    register.resizable(False, False)
    register.config(bg = "#351c75")
    register.geometry("1600x900")  
    menu_Frame = tk.Frame(register, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
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
    entrypw = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrypw.place(x = 450, y = 600)
    labelpw2 = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Re-Enter Password")
    labelpw2.place(x = 900, y = 675)
    entrypw2 = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrypw2.place(x = 450, y = 675)
    sframe = tk.Frame(register, width = 1600, height = 80, bg = "#8e7cc3")
    sframe.place(x = 0, y = 820)
    sframe.pack_propagate(False)
    buttone = tk.Button(sframe, width = 40, height = 9, bg = "#e8d619", font = ("Prompt", 20), text = "save", command = lambda : save_user(entryfn, entrysn, entryp, entrye, entryad, entryun, entrypw, entrypw2, register))
    buttone.pack()
    register.mainloop()




def Linker():
    linker = tk.Tk()
    linker.resizable(False, False)
    linker.config(bg = "#351c75")
    linker.geometry("1600x900")  
    menu_Frame = tk.Frame(linker, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    buttonr = tk.Button(linker, width = 40, height = 6, bg = "#e8d619", font = ("Prompt", 20), text = ("Sign Up"), command = lambda: register_form())
    buttonr.place(x = 100, y = 600)
    buttonl = tk.Button(linker, width = 40, height = 6, bg = "#e8d619", font = ("Prompt", 20), text = "Login", command = lambda: login())
    buttonl.place(x = 850, y = 600)
    linker.mainloop()



def search_results(search_e):
    global user_details_string
    search = tk.Tk()
    search.resizable(False, False)
    search.config(bg = "#351c75")
    search.geometry("1600x900")  
    menu_Frame = tk.Frame(search, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    search_string = search_e.get().lower()
    with open("toys.pkl", 'rb') as file:
        toys = pickle.load(file)
    toy_list = []
    for i in range (len(toys)):
       
        if search_string in toys[i].Name.lower() or search_string in toys[i].prodesc.lower():
            toy_list.append(toys[i])
   
   
 

    toys_found = []

    for i in range(len(toy_list)):
        temp = toy_list[i].Name, "£"+ toy_list[i].prodprice
        toys_found.append(temp)



    lboxtoys = tk.Listbox(search, height = 17, width = 106, font = ("Prompt", 20), selectmode=tk.SINGLE)


    for i in range(len(toys_found)):
        lboxtoys.insert(tk.END, toys_found[i])


    scrollbar = tk.Scrollbar(search, orient=tk.VERTICAL, command=lboxtoys.yview)

    lboxtoys.config(yscrollcommand=scrollbar.set)
   

    lboxtoys.place(x = 0, y = 200)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    get_user_details(username)
    
    lboxtoys.bind("<<ListboxSelect>>", lambda event: Proddisplay(lboxtoys, toys, user_details_string))
    
    


    
    def backs():
        search.destroy()
        homepage()

    buttonb = tk.Button( menu_Frame, text = "Back", command = backs)
    buttonb.pack(side = tk.LEFT, padx = 20)
    
    search.mainloop()
    
    


def Proddisplay(lboxtoys, toys, users):
    index = lboxtoys.curselection()[0]
    toy_n = toys[index]
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
    
    lbn = tk.Label(prod, text = toy_n.Name, font = ("Prompt", 30))
    lbn.place(x = 250, y = 200)
    lbp = tk.Label(prod, text = '£'+ toy_n.prodprice, font = ("Prompt", 30))
    lbp.place(x = 250, y = 350)
    lbd = tk.Label(prod, text = toy_n.prodesc, font = ("Prompt", 30))
    lbd.place(x = 250, y = 550)
    
    def addorder():
        global current_user_id, current_username 

        curorder_string = f"User  ID: {current_user_id}, Username: {current_username}, ProductID: {toy_n.prodID}, ProductName: {toy_n.Name}, ProductPrice: £{toy_n.prodprice}"

        orders_file_path = 'temp_orders.pkl'
    
        if not os.path.exists(orders_file_path):
            with open(orders_file_path, 'wb') as f:
                pickle.dump([], f)

        try:
            with open(orders_file_path, 'rb') as f:
                existing_orders = pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            existing_orders = []

        total_price = float(toy_n.prodprice)  
        for order in existing_orders:
            total_price += float(order['ProductPrice'])

        new_order = {
            'User  ID': current_user_id,
            'Username': current_username,
            'ProductID': toy_n.prodID,
            'ProductName': toy_n.Name,
            'ProductPrice': toy_n.prodprice,
            'TotalPrice': str(total_price)
        }

        existing_orders.append(new_order)
        with open(orders_file_path, 'wb') as f:
            pickle.dump(existing_orders, f)

        prod.destroy()

    buttonor = tk.Button(prod, width=30, height=4, bg="#e8d619", font=("Prompt", 20), text="Add to Order", command=lambda: addorder())
    buttonor.place(x=500, y=700)

    prod.mainloop()
    






def orderdisp():
    orderd = tk.Tk()
    orderd.resizable(False, False)
    orderd.config(bg = "#351c75")
    orderd.geometry("1600x900")  
    menu_Frame = tk.Frame(orderd, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    oframe = tk.Frame(orderd, width = 1600, height = 80, bg = "#8e7cc3")
    oframe.place(x = 0, y = 820)
    oframe.pack_propagate(False)
    
    labelad = tk.Label(orderd, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", fg = "#e4eff1",  text = "Address")
    labelad.place(x = 720, y = 360)
    entryad = tk.Entry(orderd, width = 20, font = ("Prompt", 15), bg = "#b7b7b7", fg = "#e4eff1")
    entryad.place(x = 550, y = 375)
    
    user_label = tk.Label(orderd, text=f":User  {current_username}", font=("Prompt", 15), bg="#351c75", fg = "#e4eff1")
    user_label.place(x = 680, y = 300)

    total_price_label = tk.Label(orderd, text = "Total Price: £0.00", font = ("Prompt", 15), bg="#351c75", fg = "#e4eff1")
    total_price_label.place(x = 670, y = 700)

    orders_file_path = 'temp_orders.pkl'
    if os.path.exists(orders_file_path):
        try:
            with open(orders_file_path, 'rb') as file:
                orders = pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
             orders = []
    else:
        orders = []
    


    lboxorders = tk.Listbox(orderd, height = 10, width = 50, font =  ("Prompt", 15), selectmode=tk.SINGLE)
    lboxorders.place(x = 500, y = 430)
    
    scrollbar = tk.Scrollbar(orderd, orient = tk.VERTICAL, command=lboxorders.yview)
    lboxorders.config(yscrollcommand = scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    


    total_price = 0
    for order in orders:
        item_string = f"{order['ProductName']} - £{order['ProductPrice']}"
        lboxorders.insert(tk.END, item_string)
        total_price += float(order['ProductPrice'])

    total_price_label.config(text=f"Total Price: £{total_price:.2f}")

    def delete():
        selected_index = lboxorders.curselection()
        if selected_index:
            selected_item = lboxorders.get(selected_index)
            product_name = selected_item.split(" - ")[0]

            for order in orders:
                if order['ProductName'] == product_name:
                    orders.remove(order)
                break

            lboxorders.delete(selected_index)
        nonlocal total_price
        total_price = sum(float(order['ProductPrice']) for order in orders)
        total_price_label.config(text=f"Total Price: £{total_price:.2f}")

    def add_order():
        address = entryad.get()
        main_orders_file_path = 'orders.pkl'
        if os.path.exists(main_orders_file_path):
            with open(main_orders_file_path, 'rb') as file:
                existing_orders = pickle.load(file)
        else:
            existing_orders = []
            
        if len(address) < 1:
            print("Please enter/re-enter your address")
            return

        for order in orders:
            with open("toys.pkl", 'rb') as file:
                toys = pickle.load(file)

            for toy in toys:
                if toy.Name == order['ProductName']:
                    number = int(toy.stocknum)
                    number -= 1
                    break

        order['Address'] = address
        existing_orders.append(order)
           
        with open("toys.pkl", 'wb') as file:
            pickle.dump(toys, file)

        with open(main_orders_file_path, 'wb') as file:
            pickle.dump(existing_orders, file)
            
        openfile = open("temp_orders.pkl", "w")
        openfile.close()

        print("Order added to main orders file and stock updated.")
        orderd.destroy() 
    


    buttonre = tk.Button(oframe, width = 8, height = 3, text = "Delete", command = delete, font = ("Prompt", 15))
    buttonre.place(x = 950, y = 0)

    buttonch = tk.Button(oframe, width = 25, height = 3, text = "Checkout", command = add_order, font = ("Prompt", 15))
    buttonch.place(x = 400, y = 0)
    orderd.mainloop()


def employee():
    employee = tk.Tk()
    employee.resizable(False, False)
    employee.config(bg = "#351c75")
    employee.geometry("1600x900")  
    menu_Frame = tk.Frame(employee, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    buttonTr = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Transaction Log"))#, command = TransactionLog())
    buttonTr.place(x = 200, y = 200)
    buttonUs = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Users Database"), command = lambda: Userdb())
    buttonUs.place(x = 200, y = 600)
    buttonOr = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Order Log"), command = lambda: Orderlog())
    buttonOr.place(x = 900, y  =600)
    buttonSt = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Stock Database"), command = lambda: stockdata())
    buttonSt.place(x = 900 , y = 200)
    employee.mainloop()
    
def Userdb():
    with open("users.pkl","rb", protocol=pickle.HIGHEST_PROTOCOL) as file:
        userdata = pickle.load(file)


        
   
def OrderLog():
    with open("orders.pkl", "rb", protocol=pickle.HIGHEST_PROTOCOL) as file:
        orderdata = pickle.load(file)



def stockdata():
    stock = tk.Tk()
    stock.resizable(False, False)
    stock.config(bg = "#351c75")
    stock.geometry("1600x900")  
    menu_Frame = tk.Frame(stock, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    sframe = tk.Frame(stock, width = 1600, height = 80, bg = "#8e7cc3")
    sframe.place(x = 0, y = 820)
    sframe.pack_propagate(False)
    
    def plus():
        selection = lboxtoys.curselection()
        if len(selection) == 0:
            return
        
        with open("toys.pkl", 'rb') as file:
            toys = pickle.load(file)
        print(toys[selection[0]].stocknum)
        toys[selection[0]].stocknum = int(toys[selection[0]].stocknum) +  1   
        print(toys[selection[0]].stocknum)
        with open('toys.pkl', 'wb') as file:
            pickle.dump(toys, file)

    def minus():
        selection = lboxtoys.curselection()
        if len(selection) == 0:
            return
        
        with open("toys.pkl", 'rb') as file:
            toys = pickle.load(file)
        print(toys[selection[0]].stocknum)
        toys[selection[0]].stocknum = int(toys[selection[0]].stocknum) -  1   
        print(toys[selection[0]].stocknum)
        with open('toys.pkl', 'wb') as file:
            pickle.dump(toys, file)
    
            
    buttone = tk.Button(sframe, width = 40, height = 2, bg = "#e8d619", font = ("Prompt", 20), text = "Create New Stock", command = createstock)
    buttone.place(x = 840, y = 0)
    buttonM = tk.Button(sframe, width = 2, height = 2, text = "+", command = lambda: plus)
    buttonM.place(x = 100, y = 0)
    ButtonS = tk.Button(sframe, width = 2, height = 2, text = "-", command = lambda: minus)
    ButtonS.place(x = 130, y = 0)

    with open("toys.pkl", 'rb') as file:
        toys = pickle.load(file)

    toy_list = []
    for i in range(len(toys)):
        temp = toys[i].Name, "£"+ toys[i].prodprice
        toy_list.append(temp)



    lboxtoys = tk.Listbox(stock, height = 28, width = 266, font =("Prompt", 15), selectmode=tk.SINGLE)


    for i in range(len(toy_list)):
        lboxtoys.insert(tk.END, toy_list[i])


    scrollbar = tk.Scrollbar(stock, orient = tk.VERTICAL, command=lboxtoys.yview)

    lboxtoys.config(yscrollcommand = scrollbar.set)
    

    lboxtoys.place(x = 0, y = 150)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    stock.mainloop()
    
def savestock(entrynam, entrypri, entrydesc, entrytag, stcreate):
    Name = entrynam.get()
    prodesc = entrydesc.get()
    prodprice = '£' + entrypri.get()
    prodtags = entrytag.get()

    try:
        with open("toys.pkl", 'rb') as file:
            toys = pickle.load(file)
            for i in range(len(toys)):
                if toys[i].Name == Name:
                    print("Product already exists")
                    return
            prodID = len(toys)+1
            stocknum = 1
            temp = Product(prodID, Name, prodesc, prodprice, prodtags, stocknum)
            toys.append(temp)
            with open('toys.pkl', 'wb') as file:
                pickle.dump(toys, file)
            stcreate.destroy()
    except:
        toys = []
        prodID = 1
        stocknum = 1
        temp = Product(prodID, Name, prodesc, prodprice, prodtags, stocknum)
        toys.append(temp)
        with open('toys.pkl', 'wb') as file:
            pickle.dump(toys, file)
            stcreate.destroy()
    
    
def createstock():
    stcreate = tk.Tk()
    stcreate.resizable(False, False)
    stcreate.config(bg = "#8e7cc3")
    stcreate.geometry("300x300")
    labeln = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Name"))
    labeln.place(x= 30, y = 10)
    entrynam = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrynam.place(x = 30, y = 30)
    labelpri = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Price"))
    labelpri.place(x = 30, y = 60)
    entrypri = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrypri.place(x = 30, y = 80)
    labeldesc = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Description"))
    labeldesc.place(x = 30, y = 110)
    entrydesc = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrydesc.place(x = 30, y = 130)
    labeltag = tk.Label(stcreate, width = 20, font = ("Prompt", 15), text = ("Add Product Tags"))
    labeltag.place(x = 30, y = 160)
    entrytag = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrytag.place(x= 30, y = 180)
    buttonsav = tk.Button(stcreate, width = 10, height = 2, font = ("Prompt", 15), text = ("Create Stock"),  bg = "#e8d619", command = lambda: savestock(entrynam, entrypri, entrydesc, entrytag, stcreate))
    buttonsav.place(x = 125, y = 290)
    stcreate.mainloop()

#homepage()
import_users()