'''                                                       HOSPITAL_MANAGEMENT_SYSTEM                                                                      '''
'''                                                               OPD_MODULE                                                                              '''
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
import pandas as pd                                        # IMPORTING PANDAS TO RUN SQL QUERIES
import random                                              # random ISIMPORTED TO GENERATE RANDOM FEES
from tabulate import tabulate                              # WE IMPORTED TABULATE TO DISPLAY THE QUERY OUTPUT IN A TABULATE FORMAT
#__________________________________________________________________________________________________________________________________________________________________________________________________
class connect_OPD_TO_MAIN:                                 # CONNECTING THROUGH THE SQL_SERVER VIA MAIN_MODULE
    def __init__(self, conn, mycursor):
        self.conn = conn
        self.mycursor = mycursor
#__________________________________________________________________________________________________________________________________________________________________________________________________       
    def opd_input(self):                                   # PATIENT INPUT IN OPD(OUT PATIENT DEPARTMENT)
        qry1 = "select max(OPD_NO) from OPD;"
        self.mycursor.execute(qry1)                        # execute(qry) is a method that sends an SQL query to the database for execution.
        t = self.mycursor.fetchone()                       # fetchone() is a method that fetches the next row of the result set, returning it as a tuple 
        if not t[0]:
            OPD_NO = 1
        else:
            OPD_NO = t[0] + 1                              # IT takes the maximum of OPD_NO and AUTO INCREMENT it 
        print("OPD NO IS : " ,OPD_NO)
        
        DATE_OF_ARIVAL = input("Enter Date of Appointment / Today's DATE : ")
        P_FIRST_NAME = input("Enter Patient First Name : ")
        P_LAST_NAME = input("Enter Patient Last Name : ")
        P_MOBILE = input("Enter Patient Mobile : ")
        
        qry = "select * from DOCTOR;"
        df = pd.read_sql(qry, self.conn) # it executes the SQL query using the pandas library's read_sql() function.
        # It is convenient when you want to directly retrieve the query results as a DataFrame
        print(tabulate(df, headers='keys', tablefmt='mysql', showindex=False))
        # TABULATE is then used to print the DataFrame in a tabular format using the tabulate function.
        # tablefmt='mysql' :- This parameter sets the table format to "mysql," which mimics the style of tables in MYSQL.
        # Using tablefmt='psql'__ will use the format of PostgreSQL .
        # headers='keys':- This parameter specifies that the column names of the DataFrame should be used as the table headers.
        
        D_FIRST_NAME = input("ENTER DOCTORS FIRST NAME : ")
        D_LAST_NAME = input("ENTER DOCTORS LAST NAME : ")
        SYMPTOM = input("SYMPTOM : ")
        FEE = random.randint(200, 800)

        qry = "insert into OPD values('{}' , '{}' , '{}' , '{}' , '{}' , '{}')".format(OPD_NO, P_FIRST_NAME,P_LAST_NAME,D_FIRST_NAME,D_LAST_NAME,FEE)
        # .formart() will place the data entered by user in the respective {} 
        self.mycursor.execute(qry)                         # execute(qry) is a method that sends an SQL query to the database for execution.
        # self.mycursor.fetchall()
        self.conn.commit()                                 # conn.commit(), it instructs the database to make the changes permanent

        qry = "insert into appiontment values('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(OPD_NO, DATE_OF_ARIVAL, P_FIRST_NAME,P_LAST_NAME,D_FIRST_NAME,D_LAST_NAME,SYMPTOM,"")
        # .formart() will place the data entered by user in the respective {} 
        self.mycursor.execute(qry)
        # self.mycursor.fetchall()
        self.conn.commit()                                 # conn.commit(), it instructs the database to make the changes permanent

        qry1 = "select max(P_ID) from PATIENT;"
        self.mycursor.execute(qry1)                        # execute(qry) is a method that sends an SQL query to the database for execution.
        #self.mycursor.fetchall()
        # self.conn.commit()
        t = self.mycursor.fetchone()                       # fetchone() is a method that fetches the next row of the result set, returning it as a tuple 
        # self.conn.commit()
        if not t[0]:
            P_ID = 1
        else:
            P_ID = t[0] + 1
        P_ADDRESS= input("Enter Patient Address : ")
        CITY = input("Enter Patient CITY : ")
        qry2 = "insert into PATIENT values('{}','{}','{}', '{}', '{}', '{}')".format(P_ID,P_FIRST_NAME,P_LAST_NAME,P_ADDRESS,P_MOBILE,CITY)
        self.mycursor.execute(qry2)
        self.conn.commit()                                 # conn.commit(), it instructs the database to make the changes permanent

        print("Successfully Added")
#__________________________________________________________________________________________________________________________________________________________________________________________________
    def opd_edit(self):                                    # Editing OPD
        x = int(input("Enter OPD_No: "))
        qry = "select * from OPD where OPD_NO = {};".format(x)
        self.mycursor.execute(qry)
        r = self.mycursor.fetchone()
        if r:
            FEE = int(input("Enter New Fee: "))
            qry = "update OPD set FEE = {} where OPD_NO = {};".format(FEE, x)
            self.mycursor.execute(qry)
            self.conn.commit()                             # conn.commit(), it instructs the database to make the changes permanent
            print("Updated")
        else:
            print("Wrong OPD No")
#__________________________________________________________________________________________________________________________________________________________________________________________________
    def opd_delete(self):                                  # Deleting OPD Data
        x = int(input("Enter OPD No: "))
        qry = "select * from OPD where OPD_NO = {};".format(x)
        self.mycursor.execute(qry)
        # execute(qry) is a method that sends an SQL query to the database for execution.
        r = self.mycursor.fetchone()
        # fetchone() is a method that fetches the next row of the result set, returning it as a tuple 
        # self.conn.commit()

        if r:
            dl = input("Are you sure you want to delete? (y/n): ")
            if dl == 'y':
                qry = "delete from OPD where OPD_NO = {};".format(x)
                self.mycursor.execute(qry)
                # execute(qry) is a method that sends an SQL query to the database for execution.
                self.conn.commit()                         # conn.commit(), it instructs the database to make the changes permanent
                # conn.commit() method is used to commit the changes made to a database within a transaction.
                print("Successfully Deleted")
            else:
                print("Deletion Canceled")
        else:
            print("Wrong OPD No")
#__________________________________________________________________________________________________________________________________________________________________________________________________
    # def opd_search(self):                                  # SEARCH OPD 
    #    # try:
    #         x = int(input("Enter OPD No: "))
    #         qry = "select * from OPD where OPD_NO = {};".format(x)
    #         df = pd.read_sql(qry, self.conn)
    #         print(tabulate(df, headers='keys', tablefmt='mysql', showindex=False))
                                       
    #         #  fetchall() is a method that retrieves all the remaining rows from the last executed SQL statement as a list of tuples
    #    # except:
    #         #print("Error...Please check OPD No")
#__________________________________________________________________________________________________________________________________________________________________________________________________   
    
    def opd_search(self):
        try:
            x = int(input("Enter OPD No: "))
            qry = "SELECT * FROM OPD WHERE OPD_NO = {};".format(x)
            self.mycursor.execute(qry)
            rows = self.mycursor.fetchall()
            print("printing OPD ROWS",rows)
            if rows:
                headers = [desc[0] for desc in self.mycursor.description]
                print(tabulate(rows, headers=headers, tablefmt='psql', showindex=False))
            else:
                print("No results found for OPD No: ", x)
        except:
            print("Error...Please check OPD No")






