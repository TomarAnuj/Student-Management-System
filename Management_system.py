import tkinter as tk
from tkinter import Entry,messagebox
import Management_Class
from tkinter import ttk

root = tk.Tk()

root.title("Management System")

appLabel = tk.Label(root, text="Management System", width = 20)
appLabel.config(font=("Sylfaen",30))
appLabel.pack(padx=(20,20),pady=(30,10))

nameLabel = tk.Label(root, text="Enter your name")
nameLabel.config(font=("Sylfaen",30))
nameLabel.pack()

nameEntry = Entry(root, width=30)
nameEntry.pack(pady = (0, 20))

addressLabel = tk.Label(root, text="Enter your address")
addressLabel.config(font=("Sylfaen",30))
addressLabel.pack()

addressEntry = Entry(root, width=30)
addressEntry.pack(pady =(0, 20))

phoneLabel = tk.Label(root, text="Enter your phone")
phoneLabel.config(font=("Sylfaen",30))
phoneLabel.pack()

phoneEntry = Entry(root, width=30)
phoneEntry.pack(pady=(0, 20))


def save_details():
    name = nameEntry.get()
    address = addressEntry.get()
    phone = phoneEntry.get()
    if (len(name)>0 and len(address)>0 and len(phone)>0):
        obj = Management_Class.Management()
        obj.add_data(name,address,phone)
        obj.display_data()
        obj.save_details()
        messagebox.showinfo("Success", "your details have been saved successfully")

    else:
        messagebox.showerror("Error","Enter all the details to save data.")


def display_records():
    second = tk.Tk()
    second.title('Displaying data')

    obj = Management_Class.Management('name','address','phone')
    details = obj.display_details()
    print('details')

    tree = ttk.Treeview(second)
    tree["columns"] = ("one","two","three")
    tree.heading("one", text = "Student Name")
    tree.heading("two", text="Address")
    tree.heading("three", text="phone number")

    i = 0

    for row in details:
        tree.insert('', i, text = "Student " + str(row[0]),
                    values = (row[1], row[2], row[3]))
        i = i+1

    tree.pack()

    second.mainloop()


button = tk.Button(root, text="Save Detail", command=lambda: save_details())
button.pack()

display_button = tk.Button(root, text="Display Record", command=lambda: display_records())
display_button.pack()

root.mainloop()