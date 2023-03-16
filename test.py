from tkinter import *
from tkcalendar import *
from datetime import date

root = Tk()

# create a DateEntry widget
date_entry = DateEntry(root)

# set the maxdate attribute to the current date
date_entry.maxdate = date.today()

def on_submitbuttonclicked():
    datee = date_entry.get()
    print(datee)
# pack the widget
date_entry.pack()

button = Button(root,text='Submit',command=on_submitbuttonclicked)
button.pack()

root.mainloop()
