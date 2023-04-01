import tkinter as tk
from datetime import date
from tkinter import *
from tkinter import filedialog, messagebox
from tkcalendar import *
from PIL import ImageTk,Image
from tkvideo import tkvideo
import sqlite3
filepath=''
import cv2
import pytesseract
def thirdui(x):
    root = Tk()
    root.geometry('350x550+500+200')
    root.iconbitmap('images/icon.ico')
    root.title('IMEX')
    root.config(bg='white')
    root.resizable(False, False)
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

firstui()

def Secondui():
    def openfile(e):
        global filepath
        global f

        if e == 0:
            filepath = filedialog.askopenfilename(filetypes=(("JPG", "*.jpg"), ("PNG", "*.png")))
            if filepath != '':
                f = 0
            if filepath == '':
                messagebox.showerror("Error", "You Have Not Uploaded Anything")
            else:
                m = 'The file You Uploaded is ' + filepath
                messagebox.showwarning("File ", m)

    def on_submitbuttonClicked(x):
        if f != 0:
            messagebox.showerror('Error', "You Have Not Uploaded Anything")
        else:
            global date1
            date1 = x.get()
            x = openfile(1)
            root.destroy()
            thirdui(x)
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
    lab2.place(x=45,y=100)

    maxdate = date.today()
    mindate = date(2023,1,1)

    date_entry = DateEntry(root, width=15,font=("Helvetica", 16), background='darkblue',foreground='white', borderwidth=2,maxdate=maxdate,mindate=mindate )
    date_entry.place(x=65,y=450)

    img = Image.open("images/upload1.jpg")
    img = img.resize((250,250))
    photo1 = ImageTk.PhotoImage(img)

    upload_button = Button(root,image=photo1,highlightcolor='#111111',borderwidth=0,command=lambda:openfile(0))
    upload_button.place(x=45,y=150,width=250,height=250)

    edit1 = Image.open("images/edit.jpg")
    edit1 = edit1.resize((30,30))
    edit11 = ImageTk.PhotoImage(edit1)
    edit_button1 = Button(root, image=edit11, highlightcolor='#111111', borderwidth=0)
    edit_button1.place(x=300, y=20, width=30, height=30)

    datelab1 = Label(root,text='Specify The Date:',bg='white',fg='gray')
    datelab1.place(x=65,y=427)

    image = Image.open("images/logo1.jpg")
    image= image.resize((150,75))
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo,borderwidth=0)
    label.place(x=80,y=10)

    img2 = Image.open("images/Adddata.jpg")
    img2 = img2.resize((30, 30))
    photo2 = ImageTk.PhotoImage(img2)
    upload_button1 = Button(root, image=photo2, highlightcolor='#111111', borderwidth=0)
    upload_button1.place(x=300, y=60, width=30, height=30)

    sub_button = tk.Button(root, text="Submit", bg="#E05959", fg="white",font=("Arial", 12),command=lambda :on_submitbuttonClicked(date_entry))
    sub_button.config(borderwidth=2, relief="groove", width=25)
    sub_button.place(x=50, y=485)

    root.mainloop()
Secondui()
# print(filepath)
# print(date1)

if filepath != '':
    image = cv2.imread(filepath)
    image = cv2.resize(image, (500, 500))
    #Convert image into RGB values from BGR
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    l1 = pytesseract.image_to_string(image)

    ## Detecting Words ##
    heightImage, weightImage, _ = image.shape
    boxes = pytesseract.image_to_data(image)

    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(image, (x, y), (w + x, h + y), (0, 0, 255), 3)
                cv2.putText(image, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (20, 30, 255), 2)

    cv2.waitKey(0)

    words = l1.split('\n')
    print(words)


    def Predict_the_Name_of_Student(test_value, dataset):
        scores = []

        for element in dataset:
            score = sum([1 for i, j in zip(test_value, element) if i == j])
            scores.append(score)

        max_val = scores[0]  # initialize max_val to the first element of the list
        max_idx = 0  # initialize max_idx to 0
        for i in range(1, len(scores)):
            if scores[i] > max_val:
                max_val = scores[i]
                max_idx = i
        return max_idx


    l2 = []
    dataset = ['XXXXXX', 'Afzal', 'Sumit', 'Nigel', 'Abhay', 'Cyril','Prakhar']
    for i in range(len(words)):
        max1 = Predict_the_Name_of_Student(words[i], dataset)
        if dataset[max1] != 'XXXXXX':
            l2.append(dataset[max1])

    new_list = []

    for item in l2:
        if item not in new_list:
            new_list.append(item)

    print(new_list)

def AddDataToDatabase(date1,StudentList):

    try:
        # Connect to the database
        conn = sqlite3.connect('database_name.db')

        # Get a cursor object
        cursor = conn.cursor()

        # Execute the ALTER TABLE statement to add the new column
        cursor.execute("ALTER TABLE Attendance1 ADD COLUMN '{}' TEXT".format(date1))

        # Commit the changes to the database
        conn.commit()

        # Close the database connection
        conn.close()
    except :
        print("Column Already Exist")

    for i in range(0,len(StudentList)):

        conn = sqlite3.connect('database_name.db')

        # Get a cursor object
        cursor = conn.cursor()

        # Execute the ALTER TABLE statement to add the new column
        cursor.execute("UPDATE Attendance1 SET '{}' = 'Present' WHERE Name = '{}'".format(date1,StudentList[i]))

        # Commit the changes to the database
        conn.commit()

         # Close the database connection
        conn.close()

AddDataToDatabase(date1,new_list)














