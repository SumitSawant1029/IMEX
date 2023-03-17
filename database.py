
import mysql.connector
import datetime
import pandas as pd
# import openpyxl as pd

# def addDates(x):
#     def addcolumns(dates):
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Sumit@1029",
#             database="db2"
#         )
#
#         mycursor = mydb.cursor()
#
#         # Generate the SQL query to add a new column for each date
#         for date in dates:
#             sql = "ALTER TABLE attendance ADD COLUMN `{}` VARCHAR(10)".format(date)
#
#             # Execute the SQL query
#             mycursor.execute(sql)
#
#         # Commit the changes to the database
#         mydb.commit()
#
#         # Close the cursor and the database connection
#         mycursor.close()
#         mydb.close()
#
#     # Example usage
#     dates = []
#     dates.append(x)
#     addcolumns(dates)
#
# addDates('12-12-2019')

def addpresenty():
    def present(dates):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sumit@1029",
            database="db2"
        )

        mycursor = mydb.cursor()

        # Generate the SQL query to add a new column for each date
        for date in dates:
            sql = "UPDATE attendance SET 12-12-2019 = P WHERE name = `{}`".format(date)
            # Execute the SQL query
            mycursor.execute(sql)
        # Commit the changes to the database
        mydb.commit()
        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

    dates = ['Afzal']

    present(dates)
addpresenty()