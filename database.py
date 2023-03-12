
import mysql.connector

def databaseinsertion():
    current_date = datetime.date.today()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="DB2"
    )
    mycursor = mydb.cursor()

    # mycursor.execute("CREATE DATABASE DB2")
    # mycursor.execute("CREATE TABLE attendance (name VARCHAR(20))")
    # sqlformula = "INSERT INTO attendance (name) VALUES ('Sumit')"


    df = pd.read_sql("SELECT * FROM attendance", con=mydb)
    df.to_excel("output.xlsx", index=False)
    # mycursor.execute(sqlformula)
