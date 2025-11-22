import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create window
window = tk.Tk()
window.config(background="red")
window.geometry("500x500")
window.title("mobile price Form")

# Variables
name_var = tk.StringVar()
qua_var = tk.StringVar()
Price_var = tk.StringVar()

# Function for Submit button
def submit(event):
    emp_name = name_var.get()
    emp_qua = int(qua_var.get())
    emp_Price = int(Price_var.get())

    print(f"Price : {emp_Price}, Name: {emp_name}, Quantity: {emp_qua}")

    conn = sqlite3.connect('Quentity.db')
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS EMPLOYEES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(20),
        QUENTITY INT,
        PRICE INT
    )
    """)

    c.execute("INSERT INTO EMPLOYEES (NAME, QUENTITY, PRICE) VALUES (?, ?, ?)",
              (emp_name, emp_qua, emp_Price))

    conn.commit()
    c.close()
    conn.close()

    messagebox.showinfo("Submission Successful", "Data has been submitted successfully!")

    name_var.set("")
    qua_var.set("")
    Price_var.set("")
    window.destroy()

# UI
tk.Label(window, text="Registration Form", font=("Arial", 20), bg="black", fg="white", width=200).pack(pady=5)
tk.Label(window, text="Name:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=50)
tk.Entry(window, textvariable=name_var, font=("Arial", 14)).place(x=150, y=50)

tk.Label(window, text="Quantity:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=100)
tk.Entry(window, textvariable=qua_var, font=("Arial", 14)).place(x=150, y=100)

tk.Label(window, text="Price:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=150)
tk.Entry(window, textvariable=Price_var, font=("Arial", 14)).place(x=150, y=150)

button = tk.Button(window, text="Submit", font=("Arial", 16), bg="black", fg="white")
button.place(x=170, y=200)
button.bind("<Button-1>", submit)  

window.mainloop()
