import tkinter
from tkinter import *


window = Tk()
window.title("Calculator")
window.geometry("500x500")
window.config(bg="black")


entry = Entry(window,width=56, borderwidth=5)
entry.place(x=80 , y=20)

def click(num):
    result = entry.get()
    
    if num == '.' and '.' in result:
        return
    
    entry.delete(0,END)
    entry.insert(0, str(result) + str(num)) 
    
b1 = Button(window, text="1" , width=10, command=lambda :click(1))
b1.place(x=90 , y=80)

b1 = Button(window, text="2" , width=10, command=lambda :click(2))
b1.place(x=160 , y=80)

b1 = Button(window, text="3" , width=10, command=lambda :click(3))
b1.place(x=230 , y=80)

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1]) 

b1 = Button(window, text="<-" , width=5, command= backspace)
b1.place(x=320 , y=80)

def clear():
    entry.delete(0, END)

b1 = Button(window, text="AC" , width=5, command= clear,bg="orange",fg="white")
b1.place(x=370 , y=80)

b1 = Button(window, text="4" , width=10, command=lambda :click(4))
b1.place(x=90 , y=140)

b1 = Button(window, text="5" , width=10, command=lambda :click(5))
b1.place(x=160 , y=140)

b1 = Button(window, text="6" , width=10, command=lambda :click(6))
b1.place(x=230 , y=140)

def add():
    n1 = entry.get()
    entry.delete(0,END)
    global math
    math = "addition"
    global i 
    if '.' in n1:
        i = float(n1)
    else:    
        i = int(n1)

b1 = Button(window, text="+" , width=5, command= add)
b1.place(x=320 , y=140)

def sub():
    n1 = entry.get()
    entry.delete(0,END)
    global math
    math = "subtraction"
    global i 
    if '.' in n1:
        i = float(n1)
    else:    
        i = int(n1)
   

b1 = Button(window, text="-" , width=5, command= sub)
b1.place(x=370 , y=140)

b1 = Button(window, text="7" , width=10, command=lambda :click(7))
b1.place(x=90 , y=200)

b1 = Button(window, text="8" , width=10, command=lambda :click(8))
b1.place(x=160 , y=200)

b1 = Button(window, text="9" , width=10, command=lambda :click(9))
b1.place(x=230 , y=200)

def mul():
    n1 = entry.get()
    entry.delete(0,END)
    global math
    math = "multiplication"
    global i 
    if '.' in n1:
        i = float(n1)
    else:    
        i = int(n1)
        
b1 = Button(window, text="*" , width=5, command= mul)
b1.place(x=320 , y=200)

def div():
    n1 = entry.get()
    entry.delete(0,END)
    global math
    math = "division"
    global i
    if '.' in n1:
        i = float(n1)
    else:    
        i = int(n1)

b1 = Button(window, text="/" , width=5, command= div)
b1.place(x=370 , y=200)

b1 = Button(window, text="0" , width=10, command=lambda :click(0))
b1.place(x=90 , y=260)

b1 = Button(window, text="00" , width=10, command=lambda :click('00'))
b1.place(x=160 , y=260)

b1 = Button(window, text="." , width=10, command=lambda :click('.'))
b1.place(x=230 , y=260)

   


def equal():
    n2 = entry.get()
    entry.delete(0,END)
    
    if '.' in n2:
        b = float(n2)
        entry.insert(0,i+b)
    else:
        b = int(n2)
        
    if math == "addition":
        entry.insert(0, i + b)
    elif math == "subtraction":
        entry.insert(0, i - b)
    elif math == "multiplication":
        entry.insert(0, i * b)
    elif math == "division":
        entry.insert(0, i / b)       
                
   
b1 = Button(window, text="=" , width=12, command= equal)
b1.place(x=320 , y=260)
    
window.mainloop()
