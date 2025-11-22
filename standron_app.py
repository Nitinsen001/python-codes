# import tkinter as tk
# window = tk.Tk()
# window.config(background="red")# koisa  bhi color pass ker sakta hhu
# window.geometry("500x500")# window ka size
# window.title("My first GUI")# window ka title


# def new():
#     print("Button Clicked")
#     root= tk.Tk()
#     root.mainloop()
    

# # command me new function call hoga jab button click hoga
# button = tk.Button(text="Click Me",foreground="white",background="black",font=("Bolt",30),command=new)# foreground is text color and background is background color

# button.place(x=100,y=100)# it is use to show the button in window at x and y position



# image = tk.PhotoImage(file="nitin.png")# it is use to show the image in window
# background_label = tk.Label(image=image)
# background_label.place(x=0,y=0,relwidth=1,relheight=1)# it is use to show the image in window at x and y position and relwidth and relheight is use to set the image size
# window.mainloop()# meri instructtion milne tak winndow ruki rahegi



'''
# label = tk.Label(text="Hello World",foreground="white",background="black",font=("Arial",30))# foreground is text color and background is background color


# label.pack()# it is use to show the label in window


window.mainloop()# meri instructtion milne tak winndow ruki rahegi

image = tk.PhotoImage(file="nitin.png")# it is use to show the image in window
background_label = tk.Label(image=image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)# it is use to show the image in window at x and y position and relwidth and relheight is use to set the image size'''




# import tkinter as tk
# from PIL import Image, ImageTk
# window = tk.Tk()
# window.config(background="red")# koisa  bhi color pass ker sakta hhu
# window.geometry("500x500")# window ka size
# # label = tk.Label(window,text="nitin sen is good in python",font=("BOLD",30),fg="blue") #fg ka use text me color kerne ke lliye kerte h# foreground is text color and background is background color

# bg = ImageTk.PhotoImage(Image.open("nitin.png"))
# label = tk.Label(window,image=bg)
# label.place(x=20,y=20,relwidth=1,relheight=1)
# window.mainloop()

# ========================================================================================================



# import tkinter as tk
# from PIL import Image, ImageTk
# window = tk.Tk()
# window.config(background="red")# koisa  bhi color pass ker sakta hhu
# window.geometry("500x500")# window ka size
# window.title("My first GUI")# window ka title

# def display():
#     print(var.get())
#     if var.get()==True:
#         label = tk.Label(window,text="You selected Option 1",font=("Arial",20))
#         label.pack()
#     else:
#         label = tk.Label(window,text="You selected Option 2",font=("Arial",20))
#         label.pack()
# var = tk.BooleanVar()

# # radio1 = tk.Radiobutton(window,text="Option 1",variable=var,font=("Arial",20),value=True,command=display)
# # radio1.pack()
# # radio2 = tk.Radiobutton(window,text="Option 2",variable=var,font=("Arial",20),value=False,command=display)
# # radio2.pack()


# # now add a checkbox for multiple options
# # ek sath multi opption kko click ker sakte h
# option1 = tk.BooleanVar()
# option2 = tk.BooleanVar()
# option3 = tk.BooleanVar()
# # ham upper boolian ki jaga innt or strin var bhi use ker sakte h

# chckebox1 = tk.Checkbutton(window,text="Option 1",variable=var,font=("Arial",20),command=display)
# chckebox2 = tk.Checkbutton(window,text="Option 2",variable=var,font=("Arial",20),command=display)
# chckebox3 = tk.Checkbutton(window,text="Option 3",variable=var,font=("Arial",20),command=display)
# chckebox1.pack()
# chckebox2.pack()
# chckebox3.pack()

# window.mainloop()


# database
# import sqlite3
# # connected
# conn = sqlite3.connect('mydatabase.db')

# # add cursor
# c = conn.cursor()

# create a table

# c.execute(" CREATE TABLE IF NOT EXISTS EMPLOYEES (ID INT,NAME VARCHAR(20),SALARY INT)")
# c.execute("INSERT INTO EMPLOYEES VALUES(1,'NITIN SEN',50000)")
# c.execute("INSERT INTO EMPLOYEES VALUES(2,'CHINU JOSHI',60000),(3,'RAVI KUMAR',70000)")

#  UPDATE AND DELETE COMMAND

# c.execute("UPDATE EMPLOYEES SET SALARY=100000 WHERE ID=1")
# c.execute("DELETE FROM EMPLOYEES WHERE ID=2")

#  HOW CAN INSERT THE DATA USING VARIABLE
# ID=int(input("Enter ID: "))
# NAME=input("Enter Name: ")
# SALARY=int(input("Enter Salary: "))
# c.execute("INSERT INTO EMPLOYEES VALUES(?,?,?)",(ID,NAME,SALARY))

# # commit the changes
# conn.commit()
# c.close()
# # close the connection

# conn.close()



# import tkinter as tk
# from PIL import Image, ImageTk
# window = tk.Tk()
# window.config(background="green")# koisa  bhi color pass ker sakta hhu
# window.geometry("500x500")# window ka size
# window.title("form")# window ka title
# def submit():
    
#     id = int(input)
#     name = name.get()
#     salary = sal.get()
#     print(f"ID: {id}, Name: {name}, Salary: {salary}")

# id = tk.IntVar()   
# name = tk.StringVar
# sal = tk.IntVar()


# id = tk.Radiobutton(window,text="id",variable=id,font=("Arial",20),value=int(input()),command=submit)
# id.pack()

# name = tk.Radiobutton(window,text="name",variable=name,font=("Arial",20),value=input(""),command=submit)
# name.pack()

# salary = tk.Radiobutton(window,text="sal",variable=sal,font=("Arial",20),value=int(input()),command=submit)
# salary.pack()

# window.mainloop()




# import tkinter as tk
# from PIL import Image, ImageTk

# # Create window
# window = tk.Tk()
# window.config(background="green")
# window.geometry("500x500")
# window.title("Employee Form")

# # Variables
# id_var = tk.StringVar()
# name_var = tk.StringVar()
# sal_var = tk.StringVar()

# # Function for Submit button
# def submit():
#     emp_id = id_var.get()
#     emp_name = name_var.get()
#     emp_sal = sal_var.get()
    
#     print(f"ID: {emp_id}, Name: {emp_name}, Salary: {emp_sal}")
    

#     import sqlite3
#     # connected
#     conn = sqlite3.connect('mynew.db')
#     # add cursor
#     c = conn.cursor()
#     # create a table
#     c.execute(" CREATE TABLE IF NOT EXISTS EMPLOYEES (ID INT,NAME VARCHAR(20),SALARY INT)")
#     c.execute("INSERT INTO EMPLOYEES VALUES(?,?,?)",(emp_id,emp_name,emp_sal))
#     # commit the changes
#     conn.commit()   
#     c.close()\
#     # close the connection
#     conn.close()

    
#     # Optional: Show in GUI too
#     result_label.config(text=f"ID: {emp_id}\nName: {emp_name}\nSalary: {emp_sal}")

# # Labels and Entry fields
# tk.Label(window, text="Registration Form", font=("Arial", 20), bg="green", fg="white").pack(pady=5)
# tk.Label(window, text="Employee ID:", font=("Arial", 16), bg="green", fg="white").pack(pady=5)
# tk.Entry(window, textvariable=id_var, font=("Arial", 14)).pack(pady=5)

# tk.Label(window, text="Employee Name:", font=("Arial", 16), bg="green", fg="white").pack(pady=5)
# tk.Entry(window, textvariable=name_var, font=("Arial", 14)).pack(pady=5)

# tk.Label(window, text="Salary:", font=("Arial", 16), bg="green", fg="white").pack(pady=5)
# tk.Entry(window, textvariable=sal_var, font=("Arial", 14)).pack(pady=5)

# # Submit button
# tk.Button(window, text="Submit", font=("Arial", 16), bg="blue", fg="white", command=submit).pack(pady=10)

# # Result label
# result_label = tk.Label(window, text="", font=("Arial", 14), bg="green", fg="yellow")
# result_label.pack(pady=20)

# # Run the window
# window.mainloop()



# [----------------------------------Quentity-------------------------------------]

# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import sqlite3

# # Create window
# window = tk.Tk()
# window.config(background="red")
# window.geometry("500x500")
# window.title("mobile price Form")

# # Variables
# name_var = tk.StringVar()
# qua_var = tk.StringVar()
# Price_var = tk.StringVar()

# # Function for Submit button
# def submit():
#     emp_name = name_var.get()
#     emp_qua = int(qua_var.get())
#     emp_Price = int(Price_var.get())

#     print(f"Price : {emp_Price}, Name: {emp_name}, Quantity: {emp_qua}")

#     # Connect to database
#     conn = sqlite3.connect('Quentity.db')
#     c = conn.cursor()

#     # Create table (with ID column)
#     c.execute("""
#     CREATE TABLE IF NOT EXISTS EMPLOYEES (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NAME VARCHAR(20),
#         QUENTITY INT,
#         PRICE INT
#     )
#     """)

#     # Insert data
#     c.execute("INSERT INTO EMPLOYEES (NAME, QUENTITY, PRICE) VALUES (?, ?, ?)",
#               (emp_name, emp_qua, emp_Price))

#     conn.commit()
#     c.close()
#     conn.close()

#     # Show success message
#     messagebox.showinfo("Submission Successful", "Data has been submitted successfully!")

#     # Clear fields
#     name_var.set("")
#     qua_var.set("")
#     Price_var.set("")
#     window.destroy()

# # UI
# tk.Label(window, text="Registration Form", font=("Arial", 20), bg="black", fg="white", width=200).pack(pady=5)
# tk.Label(window, text="Name:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=50)
# tk.Entry(window, textvariable=name_var, font=("Arial", 14)).place(x=150, y=50)

# tk.Label(window, text="Quantity:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=100)
# tk.Entry(window, textvariable=qua_var, font=("Arial", 14)).place(x=150, y=100)

# tk.Label(window, text="Price:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=150)
# tk.Entry(window, textvariable=Price_var, font=("Arial", 14)).place(x=150, y=150)

# tk.Button(window, text="Submit", font=("Arial", 16), bg="black", fg="white", command=submit).place(x=170, y=200)

# window.mainloop()





# --------------------------------------------------new real form ---------------------------------------------------------

# import tkinter as tk
# from tkinter import messagebox
# import sqlite3

# # ------------ WINDOW SETUP ------------
# window = tk.Tk()
# window.title("Mobile Price Form")
# window.geometry("600x500")
# window.config(bg="#ECECEC")

# # Center Frame (Form Box)
# form_frame = tk.Frame(window, bg="white", bd=2, relief="groove")
# form_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=400)

# # ------------ VARIABLES ------------
# name_var = tk.StringVar()
# qua_var = tk.StringVar()
# price_var = tk.StringVar()


# # ------------ DATABASE FUNCTION ------------
# def submit():
#     emp_name = name_var.get()
#     emp_qua = qua_var.get()
#     emp_price = price_var.get()

#     if emp_name == "" or emp_qua == "" or emp_price == "":
#         messagebox.showwarning("Missing Fields", "Please fill all the fields!")
#         return

#     try:
#         emp_qua = int(emp_qua)
#         emp_price = int(emp_price)
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Quantity and Price must be numbers!")
#         return

#     conn = sqlite3.connect('Quentity.db')
#     c = conn.cursor()

#     c.execute("""
#     CREATE TABLE IF NOT EXISTS EMPLOYEES (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NAME TEXT,
#         QUANTITY INT,
#         PRICE INT
#     )
#     """)

#     c.execute("INSERT INTO EMPLOYEES (NAME, QUANTITY, PRICE) VALUES (?, ?, ?)",
#               (emp_name, emp_qua, emp_price))

#     conn.commit()
#     c.close()
#     conn.close()

#     messagebox.showinfo("Success", "Data submitted successfully!")
#     name_var.set("")
#     qua_var.set("")
#     price_var.set("")


# # ------------ HEADING ------------
# title_label = tk.Label(
#     form_frame,
#     text="📱 Mobile Price Registration",
#     font=("Arial", 20, "bold"),
#     fg="#222",
#     bg="white"
# )
# title_label.pack(pady=(25, 20))

# separator = tk.Frame(form_frame, bg="#444", height=2, width=300)
# separator.pack(pady=(0, 10))

# # ------------ FORM FIELDS ------------
# def create_label(text, y):
#     return tk.Label(form_frame, text=text, font=("Arial", 14, "bold"), fg="#333", bg="white").place(x=70, y=y)

# def create_entry(var, y):
#     return tk.Entry(form_frame, textvariable=var, font=("Arial", 13), bd=2, relief="groove", width=25).place(x=180, y=y)

# create_label("Name:", 120)
# create_entry(name_var, 120)

# create_label("Quantity:", 170)
# create_entry(qua_var, 170)

# create_label("Price (₹):", 220)
# create_entry(price_var, 220)


# # ------------ SUBMIT BUTTON (with hover effect) ------------
# def on_enter(e):
#     submit_btn.config(bg="#222", fg="white", relief="sunken")

# def on_leave(e):
#     submit_btn.config(bg="#444", fg="white", relief="raised")

# submit_btn = tk.Button(
#     form_frame,
#     text="Submit",
#     font=("Arial", 14, "bold"),
#     bg="#444",
#     fg="white",
#     activebackground="#222",
#     activeforeground="white",
#     padx=20,
#     pady=5,
#     command=submit
# )
# submit_btn.place(relx=0.5, rely=0.8, anchor="center")
# submit_btn.bind("<Enter>", on_enter)
# submit_btn.bind("<Leave>", on_leave)


# # ------------ FOOTER ------------
# footer = tk.Label(
#     window,
#     text="© 2025 Nitin's Form Interface",
#     font=("Arial", 10, "italic"),
#     bg="#ECECEC",
#     fg="#555"
# )
# footer.pack(side="bottom", pady=10)


# window.mainloop()



# --------------------------------------------new real form 2--------------------------------------------------------------------

# import tkinter as tk
# from tkinter import messagebox
# import sqlite3

# # ---------------- WINDOW ----------------
# window = tk.Tk()
# window.title("📱 Mobile Price Entry Form")
# window.geometry("700x550")
# window.resizable(False, False)

# # Create gradient background using Canvas
# canvas = tk.Canvas(window, width=700, height=550)
# canvas.pack(fill="both", expand=True)

# # Gradient effect
# for i in range(0, 550):
#     color = "#%02x%02x%02x" % (80 + i//10, 20 + i//5, 120 + i//8)
#     canvas.create_line(0, i, 700, i, fill=color)

# # ---------------- FORM FRAME ----------------
# form_frame = tk.Frame(window, bg="#ffffff", bd=0, relief="flat")
# form_frame.place(relx=0.5, rely=0.5, anchor="center", width=460, height=400)

# # Rounded-corner effect (illusion)
# round_bg = tk.Frame(form_frame, bg="#E8E8E8")
# round_bg.place(x=10, y=10, width=440, height=380)

# inner_frame = tk.Frame(form_frame, bg="#ffffff")
# inner_frame.place(x=15, y=15, width=430, height=370)

# # ---------------- VARIABLES ----------------
# name_var = tk.StringVar()
# qua_var = tk.StringVar()
# price_var = tk.StringVar()

# # ---------------- DATABASE FUNCTION ----------------
# def submit():
#     emp_name = name_var.get()
#     emp_qua = qua_var.get()
#     emp_price = price_var.get()

#     if emp_name == "" or emp_qua == "" or emp_price == "":
#         messagebox.showwarning("⚠️ Missing Fields", "Please fill all fields before submitting.")
#         return

#     try:
#         emp_qua = int(emp_qua)
#         emp_price = int(emp_price)
#     except ValueError:
#         messagebox.showerror("❌ Invalid Input", "Quantity and Price must be numbers!")
#         return

#     conn = sqlite3.connect("Quentity.db")
#     c = conn.cursor()

#     c.execute("""
#     CREATE TABLE IF NOT EXISTS EMPLOYEES (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NAME TEXT,
#         QUANTITY INT,
#         PRICE INT
#     )
#     """)

#     c.execute("INSERT INTO EMPLOYEES (NAME, QUANTITY, PRICE) VALUES (?, ?, ?)",
#               (emp_name, emp_qua, emp_price))
#     conn.commit()
#     c.close()
#     conn.close()

#     messagebox.showinfo("✅ Success", "Data submitted successfully!")
#     name_var.set("")
#     qua_var.set("")
#     price_var.set("")

# # ---------------- FORM CONTENT ----------------
# heading = tk.Label(
#     inner_frame,
#     text="📋 Mobile Price Registration",
#     font=("Poppins", 20, "bold"),
#     bg="white",
#     fg="#4B0082"
# )
# heading.pack(pady=(20, 10))

# underline = tk.Frame(inner_frame, bg="#4B0082", height=2, width=300)
# underline.pack(pady=(0, 20))

# # Labels & Entries
# def create_label(text, y):
#     tk.Label(inner_frame, text=text, font=("Arial", 13, "bold"), bg="white", fg="#333").place(x=60, y=y)

# def create_entry(var, y):
#     tk.Entry(inner_frame, textvariable=var, font=("Arial", 13), bg="#F5F5F5", bd=0, relief="flat", width=25).place(x=180, y=y)

# create_label("Mobile Name:", 100)
# create_entry(name_var, 100)

# create_label("Quantity:", 150)
# create_entry(qua_var, 150)

# create_label("Price (₹):", 200)
# create_entry(price_var, 200)

# # ---------------- SUBMIT BUTTON (Glow effect) ----------------
# def on_enter(e):
#     submit_btn.config(bg="#6A0DAD", fg="white", font=("Arial", 13, "bold"))

# def on_leave(e):
#     submit_btn.config(bg="#4B0082", fg="white", font=("Arial", 13))

# submit_btn = tk.Button(
#     inner_frame,
#     text="Submit",
#     font=("Arial", 13),
#     bg="#4B0082",
#     fg="white",
#     activebackground="#6A0DAD",
#     activeforeground="white",
#     bd=0,
#     padx=25,
#     pady=8,
#     relief="flat",
#     cursor="hand2",
#     command=submit
# )
# submit_btn.place(relx=0.5, rely=0.8, anchor="center")
# submit_btn.bind("<Enter>", on_enter)
# submit_btn.bind("<Leave>", on_leave)

# # ---------------- FOOTER ----------------
# footer = tk.Label(
#     window,
#     text="© 2025 | Designed by Nitin | AIML Dept.",
#     font=("Arial", 10, "italic"),
#     bg="#4B0082",
#     fg="white",
#     padx=10,
#     pady=5
# )
# footer.pack(side="bottom", fill="x")

# window.mainloop()





# -------------------------------------------------Drop down------------------------------------------------------------------




# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import sqlite3

# # Create window
# window = tk.Tk()
# window.config(background="red")
# window.geometry("500x500")
# window.title("mobile price Form")

# # Variables
# name_var = tk.StringVar()
# qua_var = tk.StringVar()
# Price_var = tk.StringVar()









# # Function for Submit button
# def submit():
#     emp_name = name_var.get()
#     emp_qua = int(qua_var.get())
#     emp_Price = int(Price_var.get())

#     print(f"Price : {emp_Price}, Name: {emp_name}, Quantity: {emp_qua}")

#     # Connect to database
#     conn = sqlite3.connect('Quentity.db')
#     c = conn.cursor()

#     # Create table (with ID column)
#     c.execute("""
#     CREATE TABLE IF NOT EXISTS EMPLOYEES (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NAME VARCHAR(20),
#         QUENTITY INT,
#         PRICE INT
#     )
#     """)

#     # Insert data
#     c.execute("INSERT INTO EMPLOYEES (NAME, QUENTITY, PRICE) VALUES (?, ?, ?)",
#               (emp_name, emp_qua, emp_Price))

#     conn.commit()
#     c.close()
#     conn.close()

#     # Show success message
#     messagebox.showinfo("Submission Successful", "Data has been submitted successfully!")

#     # Clear fields
#     name_var.set("")
#     qua_var.set("")
#     Price_var.set("")
#     window.destroy()

# # UI
# tk.Label(window, text="Registration Form", font=("Arial", 20), bg="black", fg="white", width=200).pack(pady=5)
# tk.Label(window, text="Name:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=50)
# tk.Entry(window, textvariable=name_var, font=("Arial", 14)).place(x=150, y=50)

# tk.Label(window, text="Quantity:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=100)
# tk.Entry(window, textvariable=qua_var, font=("Arial", 14)).place(x=150, y=100)

# tk.Label(window, text="Price:", font=("Arial", 16), bg="black", fg="white").place(x=50, y=150)
# tk.Entry(window, textvariable=Price_var, font=("Arial", 14)).place(x=150, y=150)

# tk.Button(window, text="Submit", font=("Arial", 16), bg="black", fg="white", command=submit).place(x=170, y=200)

# window.mainloop()




# =-----------------------------------------------------motion graphics---------------------------------------------------------

# jab mouse ko move kerenge to distance show hogi 
# import tkinter as tk
 
# root = tk.Tk()
# root.title("Moving Image")
# def display(event):
#     x, y = event.x, event.y
#     # label.place(x=x, y=y)
#     print(f"Mouse moved to ({x}, {y})")
# root.bind("<Motion>",display)
# root.mainloop()



# jab mouse ki button press ho to hi move hoga tab show hoga distance

# import tkinter as tk
 
# root = tk.Tk()
# root.title("Moving Image")
# def display(event):
#     x, y = event.x, event.y
#     # label.place(x=x, y=y)
#     print(f"Mouse moved to ({x}, {y})")
# root.bind("<B1-Motion>",display)
# root.mainloop()





