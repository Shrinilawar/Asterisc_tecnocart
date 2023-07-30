from tkinter import *


root=Tk()
root.state("zoomed")
root.title("bill management")


def Reset():
    entry_Pasta.delete(0,END)

    entry_cookies.delete(0, END) 
    entry_Tea.delete(0, END)

    entry_cofee.delete(0, END)

    entry_Pizza.delete(0,END)

    entry_Burger.delete(0,END)

    entry_Fries.delete(0,END)

def Total():
    try:a1=int (Pasta.get()) 
    except: a1=0

    try:a2=int(cookies.get()) 
    except: a2=0

    try:a3=int(Tea.get()) 
    except: a3=0

    try:a4=int(cofee.get()) 
    except: a4=0

    try:a5=int( Pizza.get()) 
    except: a5=0

    try: a6=int(Burger.get())
    except: a6=0
    try:a7=int(Fries.get())
    except: a7=0

    #define cost of each item per quantity

    c1=100*a1

    c2=30*a2

    c3=20* a3

    c4=20 *a4

    c5=120 *a5
    c6=65*a6

    c7=50*a7

    lbl_total=Label (f2, font=("aria", 20, 'bold'), text="Total", width=16, fg="lightyellow", bg="black")

    lbl_total.place(x=80,y=100)

    entry_total=Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6,width=15, bg="cyan4")
    entry_total.place(x=100,y=160)

    totalcost=c1+c2+c3+c4+c5+c6+c7

    string_bill="Rs.", str("%.2f" %totalcost) 
    Total_bill.set(string_bill)







Label(text="Bill Application", bg="black",fg="white",font=("Areal",40),width="200",height="2").pack()


#Menu Card

f=Frame(root, bg="cyan4", highlightbackground="black", highlightthickness= 1, width=430,height=550)
f.place(x=10,y=130)

Label(f, text="Menu", font=("Gabriola", 48, "bold"), fg="black", bg="cyan4").place(x=80,y=0)

Label(f, font=("Gabriola", 25, 'bold'), text="Pasta.......Rs.100",fg="black", bg="cyan4").place(x=10,y=100)

Label(f, font =("Gabriola", 25, 'bold'), text="Cookies....Rs. 30",fg="black", bg="cyan4").place(x=10,y=160)

Label(f, font= ("Gabriola", 25, 'bold'), text="Tea.......Rs.20", fg ="black", bg="cyan4").place(x=10,y=220)

Label(f, font= ("Gabriola", 25, 'bold'), text="Coffee.....Rs.20", fg="black",bg="cyan4").place(x=10,y=280)

Label(f, font =("Gabriola", 25, 'bold'), text="pizza......Rs.120", fg="black", bg="cyan4").place(x=10,y=340)

Label(f, font=("Gabriola", 25, 'bold'), text= "Burger...Rs.65", fg="black", bg="cyan4").place(x=10,y=400)

Label(f, font= ("Gabriola", 25, 'bold'), text="Fries.....Rs.50",fg="black",bg="cyan4").place(x=10,y=460)

#Bill
f2=Frame(root, bg="cyan4", highlightbackground="black", highlightthickness=1,width=450,height=550)
f2.place(x=900,y=130)

Bill=Label(f2, text= "Bill", font =("calibri", 20), bg="cyan4") 
Bill.place(x=200,y=10)



#ENTRY WORK

f1=Frame(root, height=600, width=600,relief=RAISED,highlightbackground="black") 
f1.place(x=450,y=150)
Pasta=StringVar()
cookies= StringVar()
Tea=StringVar()
cofee=StringVar()
Pizza=StringVar()
Burger =StringVar()
Fries= StringVar()
Total_bill=StringVar()




#Label

lbl_Pasta=Label(f1, font =("aria", 20, 'bold'), text="Pasta", width=12, fg="blue") 
lbl_cookies=Label(f1, font =("aria", 20, "bold"), text="Cookies", width=12, fg="blue")
lbl_Tea=Label(f1, font=("aria", 20, 'bold'), text="Tea",width=12, fg="blue")
lbl_cofee=Label(f1, font =("aria", 20, "bold"), text="Coffee",width=12, fg="blue")
lbl_Pizza=Label(f1, font=("aria", 20, 'bold'), text="Pizza",width=12, fg="blue") 
lbl_Burger=Label(f1, font=("aria", 20, 'bold'), text="Burger", width=12, fg="blue")
lbl_Fries =Label(f1, font=("aria", 20, 'bold'), text="Fries",width=12, fg="blue")
lbl_Pasta.grid(row=1, column=0)
lbl_cookies.grid(row=2, column=0)
lbl_Tea.grid(row=3, column=0) 
lbl_cofee.grid(row=4, column=0)
lbl_Pizza.grid(row=5,column=0)
lbl_Burger.grid(row=6, column=0)
lbl_Fries.grid(row=7, column=0)





# Entry

entry_Pasta=Entry(f1, font= ("aria", 20, 'bold'), textvariable=Pasta, bd=6,width=8, bg="lightblue") 
entry_cookies=Entry(f1, font=("aria", 20, 'bold'), textvariable=cookies, bd=6, width=8, bg="lightblue")
entry_Tea=Entry(f1, font=("aria", 20,'bold'), textvariable=Tea,bd=6,width=8, bg="lightblue")
entry_cofee=Entry(f1, font= ("aria", 20, 'bold'), textvariable=cofee, bd=6,width=8, bg="lightblue")
entry_Pizza=Entry(f1, font=("aria", 20, 'bold'), textvariable= Pizza, bd=6, width=8, bg="lightblue")
entry_Burger=Entry(f1, font =("aria",20,"bold"), textvariable=Burger, bd=6,width=8, bg="lightblue")
entry_Fries=Entry(f1, font=("aria", 20, "bold"), textvariable=Fries, bd=6,width=8, bg="lightblue")
entry_Pasta.grid(row=1, column=1)
entry_cookies.grid(row=2, column=1)
entry_Tea.grid(row=3, column=1)
entry_cofee.grid(row=4, column=1)
entry_Pizza.grid(row=5, column=1)
entry_Burger.grid(row=6, column=1)
entry_Fries.grid(row=7,column=1)



#buttons
btn_reset=Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'),width=10, text="Reset", command=Reset) 
btn_reset.grid(row=9, column=0)
btn_total=Button(f1,bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Total", command=Total)
btn_total.grid(row=9, column=1)


root.mainloop()