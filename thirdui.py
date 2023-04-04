import tkinter as tk
from tkinter import filedialog


def download_file():
    # Provide the file path to download
    file_path = "C:\Users\Sumit\Desktop\IMEX-2\Attendance.xlsx"

    # Open the file for reading
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Set the HTTP headers to indicate a file download
    root.after(100, lambda: root.attributes("-topmost", True))
    root.after(100, lambda: root.attributes("-topmost", False))
    root.after(100, lambda: root.focus_force())

    root.protocol('WM_DELETE_WINDOW', root.iconify)

    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    root.attributes('-alpha', 0.0)
    root.after(100, lambda: root.attributes('-alpha', 1.0))

    root.protocol('WM_DELETE_WINDOW', root.iconify)

    # Set the HTTP headers to indicate a file download
    root.headers['Content-Disposition'] = f'attachment; filename="{file_path}"'

    # Send the file to the user as a download
    return flask.send_file(file_data, mimetype='application/octet-stream', as_attachment=True)


root = tk.Tk()
root.title("File Downloader")
root.geometry("200x100")

download_button = tk.Button(root, text="Download File", command=download_file)
download_button.pack()

root.mainloop()
