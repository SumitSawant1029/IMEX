import tkinter as tk
import sqlite3

import tkinter as tk
import sqlite3

# Connect to database



# Close database connection

conn = sqlite3.connect('IMEX.db')
cursor = conn.cursor()

# Retrieve data from the database
cursor.execute("SELECT * FROM Attendance1")
rows = cursor.fetchall()
print(rows)
L1=[]
for i in range(0,len(rows)):
    L1.append(rows[i][1])
print(L1)
conn.commit()
cursor.close()
conn.close()