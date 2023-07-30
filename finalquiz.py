from tkinter import *
from tkinter import messagebox as mb

def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        mb.showinfo("", "Blank Not Allowed")

    elif (username=="shri" and password=="1234"):
        mb.showinfo("", "login success")
        top.destroy()

        from Quiz import Quiz
        Quiz()
        
    else:
        mb.showinfo("", "incorrect username and password")

top=Tk()
top.geometry("300x200")
top.configure(bg="cyan4")
top.state("zoomed")

global entry1

global entry2

label1=Label(top,text="Login Page",bg="cyan4",fg="cyan",font=("Areal",20))
label1.place(x=600,y=20)

label2=Label(top,text="Username :",bg="cyan4",fg="white",font=("Areal",20))
label2.place(x=500,y=300)

label3=Label(top,text="Password :",bg="cyan4",fg="white",font=("Areal",20))
label3.place(x=500,y=400)

entry1=Entry(top, font=("Areal,",15)) 
entry1.place(x= 650,y=300)

entry2=Entry(top, font=("Areal",15),show="*")

entry2.place(x=650,y=400)

button=Button(top, text="Login", command=login,height=1, width=7,bg="cyan3",font=("Areal",20))
button.place(x=650,y=470)

top.mainloop()

