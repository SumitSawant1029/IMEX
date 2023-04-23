import time
import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import *
from tkinter import filedialog, messagebox
import os
from tkcalendar import *
from PIL import ImageTk,Image
from tkvideo import tkvideo
import sqlite3
import cv2    #openv cv
import pytesseract
import pandas as pd
filepath=''
# To Add New Students As A Dataset In Database And Comparision With Detected Names
def Addstudent(x):
    x.destroy()
    def AddNameStudent(x,y):
        import sqlite3

        # Connect to database
        conn = sqlite3.connect('IMEX.db')
        cursor = conn.cursor()

        # Retrieve data from the database
        cursor.execute("SELECT * FROM Attendance1")
        rows = cursor.fetchall()

        L1 = []
        for i in range(0, len(rows)):
            L1.append(rows[i][0])

        conn.commit()
        cursor.close()
        conn.close()
        g=1
        for i in range(0,len(rows)):
            if y.get()==L1[i]:
                g = 0
        #_____________________________________________________________________________________________________
        if g == 1:
            conn = sqlite3.connect('IMEX.db')
            cursor = conn.cursor()

            # Retrieve data from the database
            cursor.execute("INSERT INTO Attendance1 (RollNo,Name) VALUES ('{}','{}')".format(y.get(),x.get()))
            conn.commit()
            # Close the database connection
            cursor.close()
            conn.close()
            message = x.get() + " Added Successfully"
            messagebox.showinfo("Success", message)
            x.delete(0,"end")
            y.delete(0, "end")
        else :
            message = x.get() + " Already Exist "
            messagebox.showerror("Error",message)
            x.delete(0, "end")
            y.delete(0, "end")


    root = tk.Tk()
    root.geometry('350x550+500+200')
    root.iconbitmap('images/icon.ico')
    root.title('IMEX')


    root.geometry("500x600")
    root.config(bg='#2b2929')
    root.resizable(False, False)
    labelx = Label(root,text= "Student Details",bg="#2b2929",fg="white", font=('Arial',20))
    labelx.place(x=150,y=15)

    label1 = Label(root,text= "Name Of Student",bg="#2b2929",fg="white", font=('Arial',12))
    label1.place(x=50,y=400)

    entry = Entry(root,width=25, font=('Arial',12))
    entry.place(x=200,y=400)

    label12 = Label(root, text="Roll No",bg="#2b2929",fg="white", font=('Arial',12))
    label12.place(x=50,y=450)

    entry_rollNo = Entry(root, width=25, font=('Arial',12))
    entry_rollNo.place(x=200,y=450)

    button = Button(root,text="Add", font=('Arial',12),width=10,fg="light green",bg="#2b2929",command=lambda : AddNameStudent(entry,entry_rollNo))
    button.place(x=200,y=500)

    button1 = Button(root, text="Back", font=('Arial',12),width=10,fg="red",bg="#2b2929",command=lambda: moveback(root))
    button1.place(x=325,y=500)

    image = Image.open("images/Addstud.png")

    photo = ImageTk.PhotoImage(image)
    label9 = tk.Label(root, image=photo, bg="#2b2929", width=0)
    label9.place(x=80, y=50)
    # ___________________________
    root.mainloop()
# To Modify If Any Error Occur We can Modify The Output
def ModifyDatabase(name,date,status,x):
    try:
        conn = sqlite3.connect('IMEX.db')
        cursor = conn.cursor()

        # Retrieve data from the database
        cursor.execute("UPDATE Attendance1 SET '{}' = '{}' WHERE Name = '{}';".format(date.get(),status.get(),name.get()))
        conn.commit()
        cursor.close()
        conn.close()
        EditDatabase(x)
    except:
        messagebox.showerror("Wrong Crediantials","Please Enter Valid Inputs")
# Just To Move To The Previous UI
def moveback(x):
    x.destroy()
    filepath=''
    Secondui()
#TO Delete A Column Of Attendance
def DeleteColumnDatabase(date,x):
    try:
        conn = sqlite3.connect('IMEX.db')
        cursor = conn.cursor()

        # Retrieve data from the database
        cursor.execute("ALTER TABLE Attendance1 DROP COLUMN '{}';".format(date.get()))
        cursor.execute("DELETE FROM Date WHERE dates = '{}';".format(date.get()))
        conn.commit()
        cursor.close()
        conn.close()
        EditDatabase(x)
    except:
        messagebox.showerror("Wrong Crediantials","Please Enter Valid Inputs")
def EditDatabase(x):
    x.destroy()
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.title("Edit Data")
    # Set the geometry of the main window to the screen size
    root.geometry("%dx%d+0+0" % (screen_width, screen_height))

    root.config(bg="white")


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
    treeview.tag_configure('mytag', font=('Arial',12))
    for row in rows:
        treeview.insert("", tk.END, values=row, tags=('mytag',))

    scrollbar = tk.Scrollbar(root, orient="horizontal", command=treeview.xview)
    treeview.configure(xscrollcommand=scrollbar.set)


    # Set the repeatdelay and repeatinterval options for the scrollbar

    scrollbar.config(troughcolor='white', bd=0, highlightthickness=0, repeatdelay=100, repeatinterval=50)

    # Configure the scrollbar range based on the number of rows in the Treeview widget

    scrollbar.pack(side="top", fill="x")
    treeview.pack()

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Connect to the database
    conn = sqlite3.connect('IMEX.db')
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute('SELECT * FROM Attendance1')
    rows = cursor.fetchall()

    # Create a Tkinter window

    root.title("Choice Entry Field Example")

    # Create a label
    label = tk.Label(root, text="Select a name:",bg="white",font=('Arial',10))

    # Create a choice entry field
    choices = [row[1] for row in rows]
    var = tk.StringVar(value=choices[0])
    entry = tk.OptionMenu(root, var, *choices)
    entry.config(width=20)
    # Pack the label and choice entry field
    label.place(x=300,y=400)
    entry.place(x=400,y=400)

    # Close the database connection
    cursor.close()
    conn.close()
#__________________________________________________________________________
    conn = sqlite3.connect('IMEX.db')
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute('SELECT * FROM Date')
    rows = cursor.fetchall()

    # Create a Tkinter window

    root.title("Choice Entry Field Example")

    # Create a label
    label1 = tk.Label(root, text="Select a date:",bg="white",font=('Arial',10))

    # Create a choice entry field
    choices1 = [row[0] for row in rows]
    var1 = tk.StringVar(value=choices1[0])
    entry1 = tk.OptionMenu(root, var1, *choices1)
    entry1.config(width=20)
    # Pack the label and choice entry field
    label1.place(x=300, y=450)
    entry1.place(x=400, y=450)

    # Close the database connection
    cursor.close()
    conn.close()

#________________________________________________________________________________________________________________________________________
    label = tk.Label(root, text="Attendance:",bg="white",font=('Arial',10))

# Pack label and radio button group into window
    options = ["PRESENT", "ABSENT"]

    # Set the default option
    default = tk.StringVar(root)
    default.set(options[0])

    # Create the dropdown menu
    dropdown1 = tk.OptionMenu(root, default, *options)
    dropdown1.config(width=20)

    dropdown1.place(x=400,y=500)
    label.place(x=300,y=500)
#________________________________________________________________________________________________________________________________________
    Modify_Button=Button(root,text='Modify',width=10,bg="#5ACCD0",fg="white",font=('Arial', 10),command=lambda :ModifyDatabase(var,var1,default,root))
    Modify_Button.place(x=300,y=575)

    DeleteColumn_Button = Button(root, text='Delete Column', width=20,font=('Arial', 10), bg="#FF4040",command=lambda: DeleteColumnDatabase(var1,root))
    DeleteColumn_Button.place(x=400, y=575)

    img = Image.open("images/Back.png")
    img = img.resize((50,50))
    photo1 = ImageTk.PhotoImage(img)

    Back_button = Button(root, image=photo1, highlightcolor='#111111', bg="white", borderwidth=0,command=lambda: moveback(root))
    Back_button.place(x=225, y=320, width=50, height=50)

    label3 = Label(root, text="Specify the Details",bg="white", fg="gray",font=('Arial', 25))
    label3.place(x=300, y=325)

    label32 = Label(root, text="Table View", bg="white", fg="gray", font=('Arial', 15))
    label32.pack()



    image = Image.open("images/Editdata.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo,bg="white",width=0)
    label.place(x=900,y=325)
#_______________________________________________________________________________________________________________________________________
    root.mainloop()
# To Convert Database to Excel
def ConvertDatabasetoExcel():
    conn = sqlite3.connect('IMEX.db')

    # Read data from the database using a SQL query
    data = pd.read_sql_query("SELECT * FROM Attendance1", conn)

    # Convert the data to an Excel file
    data.to_excel('Attendance.xlsx', index=False)

    # Close the database connection
    conn.close()
# FrontEnd With Some Backend
def thirdui():
    if filepath != '':
        ## Python-tesseract is an optical character recognition (OCR) tool for python ##
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

        ## Fetch the image from respective Directory ##
        image = cv2.imread(filepath)

        ## Convert image into RGB values from BGR ##
        ## pytesseract works good so ##
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(pytesseract.image_to_string(image))

        ## Detecting Digits ##
        heightImage, weightImage, _ = image.shape
        ## Configuration to detect digits from images ##
        cong = r"--oem 3 --psm 6 outputbase digits"
        boxes = pytesseract.image_to_boxes(image, config=cong)

        ## Create an empty list to store detected digits
        detected_digits = []

        ## Forming bounding box around digits and storing the detected digits in a list
        for b in boxes.splitlines():
            b = b.split(" ")

            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(image, (x, heightImage - y), (w, heightImage - h), (0, 0, 255), 3)
            detected_digit = b[0]
            detected_digits.append(detected_digit)
            cv2.putText(image, detected_digit, (x, heightImage - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (20, 30, 255), 2)

        ## Print the list of detected digits
        print(detected_digits)

        cv2.imshow("Detecting Digits", image)
        cv2.waitKey(0)


#____________Added Dataset Of Students through Databaseiy

    def AddDataToDatabase(date1, Rollno):
        try:
            # Connect to the database
            conn = sqlite3.connect('IMEX.db')

            # Get a cursor object
            cursor = conn.cursor()

            # Execute the ALTER TABLE statement to add the new column
            cursor.execute("ALTER TABLE Attendance1 ADD COLUMN '{}' TEXT  DEFAULT 'ABSENT' ".format(date1))
            cursor.execute("INSERT INTO Date VALUES ('{}');".format(date1))

            # Commit the changes to the database
            conn.commit()

            # Close the database connection
            conn.close()
        except:
            print("Column Already Exist")

        conn = sqlite3.connect('IMEX.db')

        # Get a cursor object
        cursor = conn.cursor()
        for i in range(0, len(Rollno)):

            # Execute the ALTER TABLE statement to add the new column
            cursor.execute("UPDATE Attendance1 SET '{}' = 'PRESENT' WHERE RollNo = '{}'".format(date1, Rollno[i]))

        # Commit the changes to the database
        conn.commit()

        # Close the database connection
        conn.close()

    new_list = []

    for elem in detected_digits:
        if elem.isdigit() or (elem.startswith('-') and elem[1:].isdigit()):
            new_list.append(int(elem))

    print(new_list)
    AddDataToDatabase(date1, new_list)
    #--------------------------------------------------------------------------------------------------------------------
    ConvertDatabasetoExcel()

    def Openfile():
        time.sleep(1)
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
    messagebox.showwarning("", "Your Data Is Successfully Added")
    lab2 = Label(root, text='Download your file Here', font=("Arial", 19), bg="white", fg="gray")
    lab2.place(x=45, y=100)

    img = Image.open("images/Download.jpg")
    img = img.resize((300, 250))
    photo1 = ImageTk.PhotoImage(img)

    download_button = Button(root, image=photo1, highlightcolor='#111111', borderwidth=0)
    download_button.place(x=30, y=150, width=300, height=250)

    edit1 = Image.open("images/edit.jpg")
    edit1 = edit1.resize((30, 30))
    edit11 = ImageTk.PhotoImage(edit1)

    edit_button1 = Button(root, image=edit11, highlightcolor='#111111', borderwidth=0 ,command= lambda:EditDatabase(root))
    edit_button1.place(x=300, y=20, width=30, height=30)

    image = Image.open("images/logo1.jpg")
    image = image.resize((150, 75))
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo, borderwidth=0)
    label.place(x=80, y=10)

    img2 = Image.open("images/Adddata.jpg")
    img2 = img2.resize((30, 30))
    photo2 = ImageTk.PhotoImage(img2)

    upload_button1 = Button(root, image=photo2, highlightcolor='#111111', borderwidth=0,command=lambda :Addstudent(root))
    upload_button1.place(x=300, y=60, width=30, height=30)


    Open_button = tk.Button(root,text="Open", borderwidth=0,highlightcolor='#111111',width=20,height=1,bg="#FF5733",fg="white",font=("Arial", 15),command=Openfile)
    Open_button.config(borderwidth=1, relief="groove")
    Open_button.place(x=70, y=420)

    img = Image.open("images/Back.png")
    img = img.resize((50, 50))
    photox = ImageTk.PhotoImage(img)

    Back_button = Button(root, image=photox, highlightcolor='#111111', bg="white", borderwidth=0,command=lambda: moveback(root))
    Back_button.place(x=15, y=30, width=50, height=50)


    root.mainloop()
def firstui():
    root = tk.Tk()
    root.geometry('700x500+500+200')
    root.iconbitmap('images/icon.ico')
    width = 700
    height = 500

    root.resizable(False, False)
    root.title('IMEX')


    lblVideo = Label(root)
    lblVideo.pack()
    player = tkvideo("images/test1.mp4",lblVideo,loop=2,size=(700,500))
    player.play()
    lblVideo.after(2000,lblVideo.master.destroy)

    root.mainloop()
def Secondui():

    def openfile(e):
        global filepath

        if e == 0:
            filepath = filedialog.askopenfilename(filetypes=(("JPG", "*.jpg"), ("PNG", "*.png")))
            if filepath == '':
                messagebox.showerror("Error", "You Have Not Uploaded Anything")
            else:
                m = 'The file You Uploaded is ' + filepath
                messagebox.showwarning("File ", m)
    def on_submitbuttonClicked(x):
        if filepath == '':
            messagebox.showerror('Error', "You Have Not Uploaded Anything")
        else:
            message = "The File You Submitted is " + filepath
            messagebox.showwarning('Something',message)
            global date1
            date1 = x.get()
            x = openfile(1)
            root.destroy()
            thirdui()

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

    lab2 = Label(root,text='Upload your file Here',font=("Arial",19),bg="white",fg="gray")
    lab2.place(x=50,y=175)

    maxdate = date.today()
    mindate = date(2023,1,1)

    date_entry = DateEntry(root, width=15,font=("Helvetica", 16), background='darkblue',foreground='white', borderwidth=2,maxdate=maxdate,mindate=mindate )
    date_entry.place(x=65,y=125)

    img = Image.open("images/upload1.jpg")
    img = img.resize((250,250))
    photo1 = ImageTk.PhotoImage(img)

    upload_button = Button(root,image=photo1,highlightcolor='#111111',borderwidth=0,command=lambda:openfile(0))
    upload_button.place(x=45,y=225,width=250,height=250)

    edit1 = Image.open("images/edit.jpg")
    edit1 = edit1.resize((30,30))
    edit11 = ImageTk.PhotoImage(edit1)
    edit_button1 = Button(root, image=edit11, highlightcolor='#111111', borderwidth=0,command=lambda:EditDatabase(root))
    edit_button1.place(x=300, y=20, width=30, height=30)

    datelab1 = Label(root,text='Specify The Date:',bg='white',fg='gray')
    datelab1.place(x=65,y=100)

    image = Image.open("images/logo1.jpg")
    image= image.resize((150,75))
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo,borderwidth=0)
    label.place(x=80,y=10)

    img2 = Image.open("images/Adddata.jpg")
    img2 = img2.resize((30, 30))
    photo2 = ImageTk.PhotoImage(img2)
    upload_button1 = Button(root, image=photo2, highlightcolor='#111111', borderwidth=0,command=lambda :Addstudent(root))
    upload_button1.place(x=300, y=60, width=30, height=30)

    sub_button = tk.Button(root, text="Submit", bg="#E05959", fg="white",font=("Arial", 12),command=lambda :on_submitbuttonClicked(date_entry))
    sub_button.config(borderwidth=2, relief="groove", width=25)
    sub_button.place(x=50, y=485)

    root.mainloop()
firstui()
Secondui()
