import re
import tkinter as tk
from datetime import date
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkcalendar import *
from PIL import ImageTk,Image
from tkvideo import tkvideo
filepath=''
f=1
def firstui():
    # Created a Window for Adding Elements
    root = tk.Tk()
    root.iconbitmap('images/icon.ico')
    root.title('IMEX')

    lblVideo = Label(root)
    lblVideo.pack()

    player = tkvideo("images/test1.mp4",lblVideo,loop=2,size=(700,500))
    player.play()
    lblVideo.after(2000,lblVideo.master.destroy)
    # Added Software Lookup

    root.mainloop()
def openfile(e):
    global filepath
    global f
    if e==0:
        filepath = filedialog.askopenfilename(filetypes=(("PNG", "*.png"), ("JPG", "*.jpg")))
        if filepath != '':
            f=0
        if filepath == '':
            messagebox.showerror("Error","You Have Not Uploaded Anything")
            # messagebox.
        else :
            m = 'The file You Uploaded is ' + filepath
            messagebox.showwarning("File ",m)
    else :
        return filepath
def on_submitbuttonClicked(root):
        if f != 0 :
            messagebox.showerror('Error',"You Have Not Uploaded Anything")
        else:
            x = openfile(1)
            root.destroy()
            thirdui(x)


def Secondui():
    root = tk.Tk()
    root.iconbitmap('images/icon.ico')
    root.title('IMEX')
    root.geometry('900x550')
    root.config(bg='white')



    lab2 = Label(root,text='Upload your file Here',font=("Arial",19),bg="white",fg="gray")
    # lab2.place(x=90,y=400)
    lab2.place(x=45,y=100)
    # Creating a button with built-in options


    edit_button = tk.Button(root, text="Edit Previous Records", bg="#E05959", fg="white", font=("Arial", 12))
    edit_button.config(borderwidth=2, relief="groove")
    edit_button.place(x=400, y=50)

    maxdate = date.today()
    mindate = date(2023,1,1)

    date_entry = DateEntry(root, width=15,font=("Helvetica", 16), background='darkblue',foreground='white', borderwidth=2,maxdate=maxdate,mindate=mindate )
    date_entry.place(x=65,y=450)

    img = Image.open("images/upload1.jpg")
    img = img.resize((250,250))  # resize the image to fit the button
    # Create a PhotoImage object from the image
    photo1 = ImageTk.PhotoImage(img)
    upload_button = Button(root,image=photo1,highlightcolor='#111111',borderwidth=0,command=lambda:openfile(0))
    upload_button.place(x=30,y=150,width=250,height=250)
    x = openfile(1)

    lab1 = Label(root,text='Specify The Date:',bg='white',fg='gray')
    lab1.place(x=65,y=427)
    #logo
    image = Image.open("images/logo1.jpg")
    image= image.resize((150,75))
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo,borderwidth=0)
    label.place(x=80,y=10)

    print(x)
    sub_button = tk.Button(root, text="Submit", bg="#E05959", fg="white",state= 'active' ,font=("Arial", 12),command=lambda:on_submitbuttonClicked(root))
    sub_button.config(borderwidth=2, relief="groove", width=25)
    sub_button.place(x=50, y=485)



    root.mainloop()






def thirdui(x):
    root = Tk()
    print(x)
    label = Label(root, text='heloooo')
    label.place(x=80, y=10)
    root.mainloop()
firstui()
Secondui()

