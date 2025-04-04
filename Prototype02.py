import tkinter as tk
import pickle
from tkinter import PhotoImage
import sqlite3

class User:
    def __init__ (self, userID, uname, pword, fname, sname, email, postcode, phone, address):
        self.userID = userID
        self.uname = uname
        self.pword = pword
        self.fname = fname
        self.sname = sname
        self.email = email
        self.postcode = postcode
        self.address = address
        self.phone = phone
        self.staff = False
        self.admin = False

class Product:
    def __init__(self, prodID, Name, prodesc, prodprice, prodtags):
        self.prodID = prodID
        self.Name = Name
        self.prodesc = prodesc
        self.prodprice = prodprice
        self.prodtags = prodtags

class Orders:
    def __init__(self, orderID, orderprice, userID, prodID):
        self.orderID = orderID
        self.orderprice = orderprice
        self.userID = userID
        self.prodID = prodID


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
    icon = PhotoImage(file="Basket.png")
    buttonbas = tk.Button(menu_Frame, image = icon , width = 20, height = 10, command = orderdisp)
    buttonbas.pack(side = tk.RIGHT, padx = 20)
    home_page.mainloop()


def save_user(entryfn, entrysn, entryp, entrye, entrypc, entryad, entryun, entrypw, entrypw2, register):
    fName = entryfn.get()
    sName = entrysn.get()
    Email = entrye.get()
    Phone = entryp.get()
    postcode = entrypc.get()
    address = entryad.get()
    uname = entryun.get()
    pword1 = entrypw.get()
    pword2 = entrypw2.get()
    Count = 8
    Valid = True


    if len(fName) < 1:
        Count - 1
    else:
        print("Please Input Your First Name")
        return
   
    if len(sName) < 1:
        Count - 1
    else:
        print("Please Input Your Second Name")
        return
   
    #validation for email


    if Phone.isdigit() and len(Phone) == 11:
        return
    else:
        Count - 1
        print("Please Input A Valid Phone Number")
        return
   
    if postcode[:2].isnumeric() and postcode [-2:].isnumeruic():
        Count - 1
        print("Please Input A Valid Postcode")
        return


    if len(address) < 1:
        Count - 1
        print("Please Input Your Address")
    else:
        return


    if pword1==pword2:
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
            if Count == 8:
                with open('users.pkl', 'wb') as file:
                    pickle.dump(users, file)
                register.destroy()
    else:
        print("passwords don't match")
        return
   
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
    labelad = tk.Label(register, width = 20, height = 2, font = ("Prompt", 15), bg = "#351c75", text = "Postcode")
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
    sframe = tk.Frame(register, width = 1600, height = 80, bg = "#8e7cc3")
    sframe.place(x = 0, y = 820)
    sframe.pack_propagate(False)
    buttone = tk.Button(sframe, width = 40, height = 9, bg = "#e8d619", font = ("Prompt", 20), text = "save", command = lambda: save_user(entryfn, entrysn, entryp, entrye, entryad, entryun, entrypw, entrypw2))
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




#register_form()
#login()
def searchresults():
    search = tk.Tk()
    search.resizable(False, False)
    search.config(bg = "#351c75")
    search.geometry("1600x900")  
    menu_Frame = tk.Frame(search, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)


def Proddisplay():
    prod = tk.Tk()
    prod.resizable(False, False)
    prod.config(bg = "#351c75")
    prod.geometry("1600x900")  
    menu_Frame = tk.Frame(prod, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)


def orderdisp():
    order = tk.Tk()
    order.resizable(False, False)
    order.config(bg = "#351c75")
    order.geometry("1600x900")  
    menu_Frame = tk.Frame(order, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)

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


def stockdata():
    stock = tk.Tk()
    stock.resizable(False, False)
    stock.config(bg = "#351c75")
    stock.geometry("1600x900")  
    menu_Frame = tk.Frame(stock, width=1600, height = 60, bg="#8e7cc3")
    menu_Frame.place(x = 0, y = 75)
    menu_Frame.pack_propagate(False)
homepage()
