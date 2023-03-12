
import mysql.connector
import datetime
import pandas as pd
# import openpyxl as pd
def databaseinsertion(date,name):
    current_date = datetime.date.today()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Sumit@1029",
        database="DB2"
    )
    mycursor = mydb.cursor()

    # mycursor.execute("CREATE DATABASE DB2")
    # mycursor.execute("CREATE TABLE attendance (name VARCHAR(20))")
    sqlformula = "INSERT INTO attendance (name) VALUES ('Afzal')"
    mycursor.execute(sqlformula)

    df = pd.read_sql("SELECT * FROM attendance", con=mydb)

    # converting database to Excel
    df.to_excel("output.xlsx", index=False)

databaseinsertion()