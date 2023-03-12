import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

root = tk.Tk()
file_path = None

def open_image():
    global file_path
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img = img.resize((400, 400))
    img_tk = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img_tk)
    label.image = img_tk
    print(file_path)
    label.pack()

button = tk.Button(root, text="Select Image", command=open_image)
button.pack()
print(file_path)
root.mainloop()

