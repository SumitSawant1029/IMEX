
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

import pandas as pd
from PIL import ImageTk

import main


def moveback():
    main.Secondui()

def EditDatabase():
    root = tk.Tk()
    root.geometry('800x800')
    Back_Button = Button(root, text='BACK', command=moveback)
    treeview = ttk.Treeview(root)
    conn = sqlite3.connect("IMEX.db")
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(Attendance1)")
    columns = [column[1] for column in cur.fetchall()]
    treeview["columns"] = columns
    for column in columns:
        treeview.heading(column, text=column)

    cur.execute("SELECT * FROM Attendance1")
    rows = cur.fetchall()

    for row in rows:
        treeview.insert("", tk.END, values=row)

    scrollbar = tk.Scrollbar(root, orient="horizontal", command=treeview.xview)
    treeview.configure(xscrollcommand=scrollbar.set)

    # Set the repeatdelay and repeatinterval options for the scrollbar

    scrollbar.config(troughcolor='white', bd=0, highlightthickness=0, repeatdelay=100, repeatinterval=50)

    # Configure the scrollbar range based on the number of rows in the Treeview widget

    scrollbar.pack(side="bottom", fill="x")
    treeview.pack()
    root.mainloop()


def ConvertDatabasetoExcel():
    conn = sqlite3.connect('IMEX.db')

    # Read data from the database using a SQL query
    data = pd.read_sql_query("SELECT * FROM Attendance1", conn)

    # Convert the data to an Excel file
    data.to_excel('Attendance.xlsx', index=False)

    # Close the database connection
    conn.close()
def thirdui1():
    ConvertDatabasetoExcel()
    def Openfile():
        time.sleep(3)
        os.startfile("Attendance.xlsx")
    def DownloadFile():
        pass
    root = tk.Tk()
    root.geometry('350x550+500+200')
    root.iconbitmap('images/icon.ico')
    root.title('IMEX')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 350
    height = 550
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.config(bg='white')
    root.resizable(False, False)

    lab2 = Label(root, text='Download your file Here', font=("Arial", 19), bg="white", fg="gray")
    lab2.place(x=45, y=100)

    img = Image.open("images/Downloadfile.png")
    img = img.resize((300, 250))
    photo1 = ImageTk.PhotoImage(img)

    download_button = Button(root, image=photo1, highlightcolor='#111111', borderwidth=0)
    download_button.place(x=30, y=150, width=300, height=250)

    edit1 = Image.open("images/edit.jpg")
    edit1 = edit1.resize((30, 30))
    edit11 = ImageTk.PhotoImage(edit1)
    edit_button1 = Button(root, image=edit11, highlightcolor='#111111', borderwidth=0 ,command=EditDatabase)
    edit_button1.place(x=300, y=20, width=30, height=30)

    image = Image.open("images/logo1.jpg")
    image = image.resize((150, 75))
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo, borderwidth=0)
    label.place(x=80, y=10)

    img2 = Image.open("images/Adddata.jpg")
    img2 = img2.resize((30, 30))
    photo2 = ImageTk.PhotoImage(img2)
    upload_button1 = Button(root, image=photo2, highlightcolor='#111111', borderwidth=0)
    upload_button1.place(x=300, y=60, width=30, height=30)

    image1 = Image.open("images/Openbutton.png")
    image1 = image1.resize((200, 100))
    photo3 = ImageTk.PhotoImage(image1)
    Open_button = tk.Button(root, image=photo3, borderwidth=0, bg='white',command=Openfile)
    Open_button.config(borderwidth=2, relief="groove")
    Open_button.place(x=65, y=420)
    root.mainloop()
