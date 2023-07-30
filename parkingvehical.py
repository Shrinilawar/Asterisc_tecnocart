import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Parking Management System")
window.geometry("700x500")
window.configure(bg="cyan4")

Vehicle_Number = []
Vehicle_Type = []
vehicle_Name = []
Owner_Name = []

login_button = None
close_button = None

def login():
    def verify_login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "shri" and password == "1234":
            entry_window.destroy()
            show_options()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    entry_window = tk.Toplevel(window)
    entry_window.geometry("700x500")
    entry_window.configure(bg="cyan4")

    entry_window.title("Login")

    label_username = tk.Label(entry_window, text="Username:",height="2")
    label_username.place(x=250,y=100)
    entry_username = tk.Entry(entry_window,font=("Areal",17))
    entry_username.place(x=330,y=100)

    label_password = tk.Label(entry_window, text="Password:",height="2")
    label_password.place(x=250,y=150)
    entry_password = tk.Entry(entry_window, show="*",font=("bold",17))
    entry_password.place(x=330,y=150)

    login_button = tk.Button(entry_window, text="Login", command=verify_login,bg="cyan4",height="2",width="12",font=("bold",15))
    login_button.place(x=300,y=230)

def show_options():
    global login_button
    global close_button
    login_button.destroy()
    close_button.destroy()

    add_vehicle_button = tk.Button(window, text="Add Vehicle", font=("bold", 14), command=vehicle_entry,bg="cyan4")
    add_vehicle_button.pack(pady=10)

    display_vehicles_button = tk.Button(window, text="Display Parked Vehicles", font=("bold", 14), command=display_parked_vehicles,bg="cyan4")
    display_vehicles_button.pack(pady=10)

    remove_vehicle_button = tk.Button(window, text="Remove Vehicle", font=("bold", 14), command=remove_vehicle,bg="cyan4")
    remove_vehicle_button.pack(pady=10)

    close_button = tk.Button(window, text="Close", font=("bold", 14), command=window.destroy,bg="cyan4")
    close_button.pack(pady=10)

def vehicle_entry():
    entry_window = tk.Toplevel(window)
    entry_window.title("Vehicle Entry")
    entry_window.geometry("700x500")
    entry_window.configure(bg="cyan4")

    def save_entry():
        vno = entry_vehicle_number.get().upper()
        vtype = entry_vehicle_type.get().lower()
        vname = entry_vehicle_name.get()
        owner_name = entry_owner_name.get()

        if vno == "":
            messagebox.showerror("Error", "Please enter a vehicle number.")
        elif vno in Vehicle_Number:
            messagebox.showerror("Error", "Vehicle number already exists.")
        elif vtype == "":
            messagebox.showerror("Error", "Please enter a vehicle type.")
        elif vname == "":
            messagebox.showerror("Error", "Please enter a vehicle name.")
        elif owner_name == "":
            messagebox.showerror("Error", "Please enter the owner name.")
        else:
            Vehicle_Number.append(vno)
            Vehicle_Type.append(vtype)
            vehicle_Name.append(vname)
            Owner_Name.append(owner_name)

            messagebox.showinfo("Success", "Vehicle entry recorded successfully.")
            entry_window.destroy()

    label_vehicle_number = tk.Label(entry_window, text="Vehicle Number (XXXX-XX-XXXX):",bg="cyan")
    label_vehicle_number.grid(row=0, column=0, padx=10, pady=5)
    entry_vehicle_number = tk.Entry(entry_window,font=("Areal",17))
    entry_vehicle_number.grid(row=0, column=1, padx=10, pady=5)

    label_vehicle_type = tk.Label(entry_window, text="Vehicle Type (Bicycle/Bike/Car):",bg="cyan")
    label_vehicle_type.grid(row=1, column=0, padx=10, pady=5)
    entry_vehicle_type = tk.Entry(entry_window,font=("Areal",17))
    entry_vehicle_type.grid(row=1, column=1, padx=10, pady=5)

    label_vehicle_name = tk.Label(entry_window, text="Vehicle Name:",bg="cyan")
    label_vehicle_name.grid(row=2, column=0, padx=10, pady=5)
    entry_vehicle_name = tk.Entry(entry_window,font=("Areal",17))
    entry_vehicle_name.grid(row=2, column=1, padx=10, pady=5)

    label_owner_name = tk.Label(entry_window, text="Owner Name:",bg="cyan")
    label_owner_name.grid(row=3, column=0, padx=10, pady=5)
    entry_owner_name = tk.Entry(entry_window,font=("Areal",17))
    entry_owner_name.grid(row=3, column=1, padx=10, pady=5)

    save_button = tk.Button(entry_window, text="Save", command=save_entry,bg="cyan4",height="2",width="12")
    save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def display_parked_vehicles():
    display_window = tk.Toplevel(window)
    display_window.geometry("700x500")
    display_window.title("Parked Vehicles")
    display_window.configure(bg="cyan4")

    label_title = tk.Label(display_window, text="List of Parked Vehicles", font=("bold", 14))
    label_title.grid(row=0, column=0, columnspan=4, pady=10)

    label_vehicle_number = tk.Label(display_window, text="Vehicle Number", font=("bold", 12))
    label_vehicle_number.grid(row=1, column=0, padx=10, pady=5)
    label_vehicle_type = tk.Label(display_window, text="Vehicle Type", font=("bold", 12))
    label_vehicle_type.grid(row=1, column=1, padx=10, pady=5)
    label_vehicle_name = tk.Label(display_window, text="Vehicle Name", font=("bold", 12))
    label_vehicle_name.grid(row=1, column=2, padx=10, pady=5)
    label_owner_name = tk.Label(display_window, text="Owner Name", font=("bold", 12))
    label_owner_name.grid(row=1, column=3, padx=10, pady=5)

    row = 2
    for i in range(len(Vehicle_Number)):
        vehicle_number = Vehicle_Number[i]
        vehicle_type = get_vehicle_type(Vehicle_Type[i])
        vehicle_name = vehicle_Name[i]
        owner_name = Owner_Name[i]

        label_vnum = tk.Label(display_window, text=vehicle_number)
        label_vnum.grid(row=row, column=0, padx=10, pady=5)
        label_vtype = tk.Label(display_window, text=vehicle_type)
        label_vtype.grid(row=row, column=1, padx=10, pady=5)
        label_vname = tk.Label(display_window, text=vehicle_name)
        label_vname.grid(row=row, column=2, padx=10, pady=5)
        label_oname = tk.Label(display_window, text=owner_name)
        label_oname.grid(row=row, column=3, padx=10, pady=5)

        row += 1

def get_vehicle_type(vehicle_type):
    if vehicle_type.lower() in ['a', 'bicycle','Bicycle',"BICYCLE"]:
        return "Bicycle"
    elif vehicle_type.lower() in ['b', 'bike','Bike',"BIKE"]:
        return "Bike"
    elif vehicle_type.lower() in ['c', 'car','Car',"CAR"]:
        return "Car"
    else:
        return ""


def remove_vehicle():
    remove_window = tk.Toplevel(window)
    remove_window.geometry("700x500")
    remove_window.title("Remove Vehicle")
    remove_window.configure(bg="cyan4")

    def delete_vehicle():
        vno = remove_vehicle_number.get().upper()

        if vno == "":
            messagebox.showerror("Error", "Please enter a vehicle number.")
        elif vno not in Vehicle_Number:
            messagebox.showerror("Error", "No entry found with the given vehicle number.")
        else:
            index = Vehicle_Number.index(vno)

            Vehicle_Number.pop(index)
            Vehicle_Type.pop(index)
            vehicle_Name.pop(index)
            Owner_Name.pop(index)

            messagebox.showinfo("Success", "Vehicle entry removed successfully.")
            remove_window.destroy()

 
    label_vehicle_number = tk.Label(remove_window, text="Vehicle Number (XXXX-XX-XXXX):")
    label_vehicle_number.pack()
    remove_vehicle_number = tk.Entry(remove_window,font=("Areal",17))
    remove_vehicle_number.pack()

    delete_button = tk.Button(remove_window, text="Remove", command=delete_vehicle,bg="cyan4",height="2",width="12")
    delete_button.pack()

def home():
    global login_button, close_button

    label_title = tk.Label(window, text="Parking Management System", font=("bold", 20))
    label_title.pack(pady=20)

    login_button = tk.Button(window, text="Login", font=("bold", 14), command=login,bg="cyan4")
    login_button.pack(pady=10)

    close_button = tk.Button(window, text="Close", font=("bold", 14), command=window.destroy,bg="cyan4")
    close_button.pack(pady=10)

home()

window.mainloop()