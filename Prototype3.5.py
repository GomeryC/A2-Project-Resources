import tkinter as tk
import pickle
from tkinter import PhotoImage
import sqlite3
import csv
import pprint


class User:
    def __init__ (self, userID, uname, pword, fname, sname, Email, postcode, phone, address):
        self.userID = userID
        self.uname = uname
        self.pword = pword
        self.fname = fname
        self.sname = sname
        self.email = Email
        self.postcode = postcode
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

    with open("toys.csv", mode='r', newline='') as file:
    # Create a CSV reader object
        csv_reader = list(csv.reader(file))

   

    toy_list = []
    for i in range(len(csv_reader)):
        temp = Product(csv_reader[i][0],csv_reader[i][1],csv_reader[i][2],csv_reader[i][3],csv_reader[i][4], int(csv_reader[i][7])) 
        toy_list.append(temp)
    pprint.pprint(toy_list)
    

    with open('toys.pkl', 'wb+') as file:
        pickle.dump(toy_list, file)
        print("Updataed")
        pprint.pprint (Product) 

def import_users():
    with open("users.csv", mode='r', newline='') as file:
    # Create a CSV reader object
            csv_reader = list(csv.reader(file))

   

    user_list = []
    for i in range(len(csv_reader)):
        temp = User(csv_reader[i][0],csv_reader[i][1],csv_reader[i][2],csv_reader[i][3],csv_reader[i][4], csv_reader[i][5], csv_reader[i][6], csv_reader[i][7], csv_reader[i][8])
        user_list.append(temp)
    print(user_list)
    

    with open('users.pkl', 'wb') as file:
        pickle.dump(user_list, file)
    







def homepage():
    home_page = tk.Tk()
    home_page.resizable(False, False)
    home_page.config(bg = "#351c75")
    home_page.geometry("1600x900")  
    menu_Frame = tk.Frame(home_page, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    #creates the size for the window and the menu bar
    buttonLi = tk.Button(menu_Frame, text = "Signup/Login", command = Linker, width = 20, height = 2)
    buttonLi.pack(side = tk.LEFT, padx = 20)
    buttonE = tk.Button(menu_Frame, text = "Employee Access", width = 20, height = 2, command = employee)
    buttonE.pack(side = tk.LEFT, padx = 20)
    buttonbas = tk.Button(menu_Frame, width = 20, height = 10, command = orderdisp)
    buttonbas.pack(side = tk.RIGHT, padx = 20)
    button_search = tk.Button(home_page, width = 15, height = 5, text  = "Search", command = lambda: search_results(search_e))
    button_search.place(x = 800, y = 200)
    search_e = tk.Entry(home_page)
    search_e.place(x = 550 , y = 200, width = 300, height =60)
    home_page.mainloop()






   
def login_user(entryun, entrypw, login_screen):
    uname = entryun.get()
    pword = entrypw.get()
    valid = False




    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
        for i in range(len(users)):
            if users[i].uname == uname and users[i].pword == pword:
                valid = True
                login_screen.destroy()
                print("you are logged in")
            homepage()
       
        if valid == False:
            print("username or password not found")
            return








def login():
    global usern
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
    usern = entryun.get
        
    login_screen.mainloop()
    
def GetUser():
    global users
    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)

    user_list = []
    for i in range(len(users)):
        temp = users[i].uname
        user_list.append(temp)
        try:
            usern
        except:
            print("User not logged in")
        else: 
            for i in range(0, len(user_list)):
                if user_list[i] == usern :
                    print (usern)
                    return User
            else:
                return





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
    # This creates the sign in page
    
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
                temp = User(pkey, uname, pword1, fName, sName, Email, postcode, Phone)
                users.append(temp)
                with open('users.pkl', 'wb') as file:
                    pickle.dump(users, file)
                register.destroy()
        except:
            users = []
            pkey = 1
            temp = User(pkey, uname, pword1, fName, sName, Email, postcode, Phone)
            users.append(temp)
            with open('users.pkl', 'wb') as file:
                pickle.dump(users, file)
                register.destroy()
            
    sframe = tk.Frame(register, width = 1600, height = 80, bg = "#8e7cc3")
    sframe.place(x = 0, y = 820)
    sframe.pack_propagate(False)
    buttone = tk.Button(sframe, width = 40, height = 9, bg = "#e8d619", font = ("Prompt", 20), text = "save", command = save_user(entryfn, entrysn, entryp, entrye, entryad, entryun, entrypw, entrypw2, register))
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
            print(toys[i].Name, toys[i].prodesc)
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
    
    GetUser()
    
    lboxtoys.bind("<<ListboxSelect>>", lambda event: Proddisplay(lboxtoys, toys, users))
    
    


    
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
    lbn.place(x = 600, y = 200)
    lbp = tk.Label(prod, text = '£'+ toy_n.prodprice, font = ("Prompt", 30))
    lbp.place(x = 250, y = 350)
    lbd = tk.Label(prod, text = toy_n.prodesc, font = ("Prompt", 30))
    lbd.place(x = 300, y = 550)
    
    def addorder():
        with open("toys.pkl", 'rb') as file:
            order = pickle.load(file)
            order = (str(toy_n))
            ordstring = ()
            if len(ordstring) >1:
                ordstring = usern + ',' + order
                print(ordstring)
            else:
                ordstring +=',' + order
                print(ordstring)
    
    buttonor = tk.Button(prod, width = 40, height = 6, bg = "#e8d619", font = ("Prompt", 20), text = "Add to Order", command = addorder())
    buttonor.place(x = 850, y = 600)
    
    Proddisplay.mainloop()
    






def orderdisp():
    order = tk.Tk()
    order.resizable(False, False)
    order.config(bg = "#351c75")
    order.geometry("1600x900")  
    menu_Frame = tk.Frame(order, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
    user(GetUser(user))
    labelad = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Address")
    labelad.place(x = 900, y = 375)
    entryad = tk.Entry(register, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entryad.place(x = 450, y = 375)
    

def checkout():
    check = tk.Tk()
    check.resizable(False, False)
    check.config(bg = "#351c75")
    check.geometry("1600x900")  
    menu_Frame = tk.Frame(check, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)


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
    buttonUs = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Users Database"), command = Userdb())
    buttonUs.place(x = 200, y = 600)
    buttonOr = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Order Log"), command = Orderlog())
    buttonOr.place(x = 900, y  =600)
    buttonSt = tk.Button(employee, width = 20, height = 5, bg = "#e8d619", font = ("Comfortaa", 30), text = ("Access to Stock Database"), command = stockdata())
    buttonSt.place(x = 900 , y = 200)
    employee.mainloop()
    
def Userdb():
    with open("users.pkl","rb") as file:
        userdata = pickle.load(file)


        
   
def OrderLog():
    with open("orders.pkl", "rb") as file:
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
    
            
    buttone = tk.Button(sframe, width = 40, height = 2, bg = "#e8d619", font = ("Prompt", 20), text = "Here", command = createstock)
    buttone.place(x = 840, y = 0)
    buttonM = tk.Button(sframe, width = 2, height = 2, text = "+", command = plus)
    buttonM.place(x = 120, y = 0)
    ButtonS = tk.Button(sframe, width = 2, height = 2, text = "-", command = minus)
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
    
def createstock():
    stcreate = tk.Tk()
    stcreate.resizable(False, False)
    stcreate.config(bg = "#8e7cc3")
    stcreate.geometry("300x300")
    entrynam = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrynam.place(x = 30, y = 30)
    entrypri = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrypri.place(x = 30, y = 80)
    entrydesc = tk.Entry(stcreate, width = 20, font = ("Prompt", 15), bg = "#b7b7b7")
    entrydesc.place(x = 30, y = 130)
    stcreate.mainloop()

def add_order():

    toy = tk.Tk()
 

    with open("toys.pkl", 'rb') as file:
        toys = pickle.load(file)

    toy_list = []
    for i in range(len(toys)):
        temp = toys[i].Name, "£"+ toys[i].prodprice
        toy_list.append(temp)



    lboxtoys = tk.Listbox(toy, height=8, width=50, selectmode=tk.SINGLE)


    for i in range(len(toy_list)):
        lboxtoys.insert(tk.END, toy_list[i])


    scrollbar = tk.Scrollbar(toy, orient=tk.VERTICAL, command=lboxtoys.yview)

    lboxtoys.config(yscrollcommand=scrollbar.set)
    

    lboxtoys.pack(side=tk.LEFT)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    wizbutton = tk.Button(toy, text = ">>", command = lambda: get_users(lboxtoys, toy))
    wizbutton.pack()
    toy.mainloop()
###################################################################
def get_users(lboxtoys, toy):
    toy_index = lboxtoys.curselection()[0]
    toy.destroy()
    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
    user_win = tk.Tk()
    users_list = []
    for i in range(len(users)):
        temp = users[i].uname, users[i].fname, users[i].sname, 
        print(temp)
        users_list.append(temp)


    lboxusers = tk.Listbox(user_win, height=8, width=50, selectmode=tk.SINGLE)


    for i in range(len(users_list)):
        print(users_list[i])
        lboxusers.insert(tk.END, users_list[i])


    scrollbaruser = tk.Scrollbar(user_win, orient=tk.VERTICAL, command=lboxusers.yview)

    lboxusers.config(yscrollcommand=scrollbaruser.set)
    lboxusers.pack(side=tk.LEFT)
    scrollbaruser.pack(side=tk.RIGHT, fill=tk.Y)
    wizuser_button = tk.Button(user_win, text = ">>", command = lambda: create_order(toy_index, lboxusers, user_win))
    wizuser_button.pack()
    user_win.mainloop()

def create_order(toy_index, lboxusers, user_win):
    with open("toys.pkl", 'rb') as file:
        toys = pickle.load(file)
    with open("users.pkl", 'rb') as file:
        users = pickle.load(file)
    
    
    user_index = lboxusers.curselection()[0]
    user_win.destroy()
    user_object = users[user_index]
    toy_object = toys[toy_index]

    userID = user_object.userID
    prodID = toy_object.prodID
    toyPrice = toy_object.prodprice


    try:
            with open("orders.pkl", 'rb') as file:
                order_list = pickle.load(file)
                pkey = len(order_list)+1
                temp = Orders(pkey, toyPrice, userID, prodID)
                order_list.append(temp)
                with open('orders.pkl', 'wb') as file:
                    pickle.dump(order_list, file)
                print("order_created")
            
    except:
            order_list = []
            pkey = 1
            temp = Orders(pkey, toyPrice, userID, prodID)
            order_list.append(temp)
            
            with open('orders.pkl', 'wb') as file:
                pickle.dump(order_list, file)
            print("order_created")

    with open("orders.pkl", 'rb') as file:
        order_list = pickle.load(file)
    for i in range(len(order_list)):
        print(order_list[i].prodID)



    


#stockdata()
homepage()
#import_users()
#add_order()
#import_toys()