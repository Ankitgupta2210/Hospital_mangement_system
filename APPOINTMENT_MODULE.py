'''                                                       HOSPITAL_MANAGEMENT_SYSTEM                                                                      '''
'''                                                           APPOINTMENT_MODULE                                                                          '''
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
import pandas as pd                                # IMPORTING PANDAS TO RUN SQL QUERIES
from tabulate import tabulate                      # WE IMPORTED TABULATE TO DISPLAY THE QUERY OUTPUT IN A TABULATE FORMAT
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
class connect_APPOINTMENT_TO_MAIN:                 # CONNECTING THROUGH THE SQL_SERVER VIA MAIN_MODULE
    def __init__(self, conn, mycursor):
        self.conn = conn
        self.mycursor = mycursor
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def appointment(self):                         # SHOWING APPOINTMENTS 
        qry = "SELECT * FROM APPOINTMENT WHERE DATE_ON_ARRIVAL = CURDATE();"
        df = pd.read_sql(qry, self.conn)# it executes the SQL query using the pandas library's read_sql() function.
        # It is convenient when you want to directly retrieve the query results as a DataFrame
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        # TABULATE is then used to print the DataFrame in a tabular format using the tabulate function.
        # tablefmt='mysql' :- This parameter sets the table format to "mysql," which mimics the style of tables in MYSQL.
        # Using tablefmt='psql'__ will use the format of PostgreSQL .
        # headers='keys':- This parameter specifies that the column names of the DataFrame should be used as the table headers.
        
        
        x = input("Enter Doctor name: ")
        qry = "SELECT * FROM APPOINTMENT WHERE D_FIRST_NAME = '{}';".format(x)
        self.mycursor.execute(qry)                 # execute(qry) is a method that sends an SQL query to the database for execution.
        r = self.mycursor.fetchone()               # fetchone() is a method that fetches the next row of the result set, returning it as a tuple
        df = pd.read_sql(qry, self.conn)
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        
        self.conn.commit()                         # conn.commit(), it instructs the database to make the changes permanent
        if r:
            # print("Exist")
            t = input("Treatment: ")
            qry = "UPDATE APPOINTMENT SET TREATMENT = '{}' WHERE D_FIRST_NAME = '{}';".format(t, x)
            self.mycursor.execute(qry)             # execute(qry) is a method that sends an SQL query to the database for execution.
            # execute(qry) is a method that sends an SQL query to the database for execution.
            self.conn.commit()                     # conn.commit(), it instructs the database to make the changes permanent
            print("Successfully updated")
        else:
            print("Wrong Doctor Name")
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def appointment_edit(self):                    # EDITING APPOINTMENTS 
        x = input("Enter Doctor First Name: ")
        qry = "SELECT * FROM APPOINTMENT WHERE D_FIRST_NAME = '{}';".format(x)
        self.mycursor.execute(qry)                 # execute(qry) is a method that sends an SQL query to the database for execution.
        # execute(qry) is a method that sends an SQL query to the database for execution.
        r = self.mycursor.fetchone()               # fetchone() is a method that fetches the next row of the result set, returning it as a tuple
        # fetchone() is a method that fetches the next row of the result set, returning it as a tuple 
        if r:
            d = input("Enter treatment: ")
            qry = "UPDATE APPOINTMENT SET TREATMENT = '{}' WHERE D_FIRST_NAME = '{}';".format(d, x)
            self.mycursor.execute(qry)             # execute(qry) is a method that sends an SQL query to the database for execution.
            self.conn.commit()                     # conn.commit(), it instructs the database to make the changes permanent
            print("Successful Update")
        else:
            print("Wrong Doctor Name")
#__________________________________________________________________________________________________________________________________________________________________________________________________ 