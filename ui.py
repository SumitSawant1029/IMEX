import tkinter as tk
from datetime import date
from tkinter import *
from tkinter import filedialog, messagebox
from tkcalendar import *
from PIL import ImageTk,Image
from tkvideo import tkvideo

filepath=''
f=1
y=''
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

def getdate(x):
    global y
    if x != 0:
        y = x.get()
        print(y)
        return y
    else :
        return y
def openfile(e):
    global filepath
    global f

    if e==0:
        filepath = filedialog.askopenfilename(filetypes=(("JPG", "*.jpg"),("PNG", "*.png")))
        if filepath != '':
            f=0
        if filepath == '':
            messagebox.showerror("Error","You Have Not Uploaded Anything")
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
    getdate(date_entry)

    img = Image.open("images/upload1.jpg")
    img = img.resize((250,250))
    photo1 = ImageTk.PhotoImage(img)
    upload_button = Button(root,image=photo1,highlightcolor='#111111',borderwidth=0,command=lambda:openfile(0))
    upload_button.place(x=45,y=150,width=250,height=250)
    x = openfile(1)

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

    sub_button = tk.Button(root, text="Submit", bg="#E05959", fg="white",font=("Arial", 12),command=lambda:on_submitbuttonClicked(root))
    sub_button.config(borderwidth=2, relief="groove", width=25)
    sub_button.place(x=50, y=485)

    root.mainloop()
def thirdui(x):
    root = Tk()
    root.geometry('350x550+500+200')
    root.iconbitmap('images/icon.ico')
    root.title('IMEX')
    root.config(bg='white')
    root.resizable(False, False)
    root.mainloop()
