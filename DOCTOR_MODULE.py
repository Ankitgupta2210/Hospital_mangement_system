'''                                                       HOSPITAL_MANAGEMENT_SYSTEM                                                                       '''
'''                                                             DOCTOR_MODULE                                                                              '''
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
import pandas as pd                                  # IMPORTING PANDAS TO RUN SQL QUERIES
from tabulate import tabulate                        # WE IMPORTED TABULATE TO DISPLAY THE QUERY OUTPUT IN A TABULATE FORMAT
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
class connect_DOCTOR_TO_MAIN:                        # CONNECTING THROUGH THE SQL_SERVER VIA MAIN_MODULE
    def __init__(self, conn, mycursor):
        self.conn = conn
        self.mycursor = mycursor
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def doctor_input(self):                          # USER WILL INSERT DOCTOR DETAILS
        qry1 = "select max(D_ID) from DOCTOR;"
        self.mycursor.execute(qry1)                  # execute(qry) is a method that sends an SQL query to the database for execution.
        t = self.mycursor.fetchone()                 # fetchone() is a method that fetches the next row of the result set, returning it as a tuple
        if not t[0]:
            D_ID = 1
        else:
            D_ID =t[0] + 1 
        print("Doctor's ID NO IS : ",D_ID)
        
        #D_ID = int(input("ENTER DOCTOR ID"))
        D_FIRST_NAME = input("ENTER DOCTOR's FIRST NAME : ")
        D_LAST_NAME = input("ENTER DOCTOR's LAST NAME : ")
        DEPARTMENT = input("ENTER DEPARTMENT : ")
        qry = "insert into doctor values('{}','{}','{}','{}')".format(D_ID , D_FIRST_NAME , D_LAST_NAME , DEPARTMENT)
        # .formart() will place the data entered by user in the respective {} 
        print("Successfully Added")
        self.mycursor.execute(qry)                   # execute(qry) is a method that sends an SQL query to the database for execution.
        self.conn.commit()                           # conn.commit(), it instructs the database to make the changes permanent
        self.mycursor.close()                        # close() method is used to close the cursor, releasing any resources associated with it
#__________________________________________________________________________________________________________________________________________________________________________________________________        
    def doctor_edit(self):                           # USER CAN EDIT DOCTOR DETAILS
        x = int(input("Enter Doctor ID : "))
        qry = "select * from  DOCTOR where D_ID = {};".format(x)
        self.mycursor.execute(qry)                   # execute(qry) is a method that sends an SQL query to the database for execution.
        r = self.mycursor.fetchone()                 # fetchone() is a method that fetches the next row of the result set, returning it as a tuple
        #con.commit()
        if r : 
            #print("EXIST")
            d = input("Enter New Department : ")
            qry = "update DOCTOR set DEPARTMENT = '{}' where D_ID ={};".format(d,x)
            self.mycursor.execute(qry)               # execute(qry) is a method that sends an SQL query to the database for execution.
            self.conn.commit()                       # conn.commit(), it instructs the database to make the changes permanent
            print("Successfull Updated")
        else : 
            print("Wrong DoctorID")
        #cursor.close()
#__________________________________________________________________________________________________________________________________________________________________________________________________        
    def doctor_delete(self) :                        # USER CAN DELETE DOCTOR DETAILS           
        x = int(input("Enter DoctorID : "))
        qry = "select * from DOCTOR where D_ID ={};".format(x)
        self.mycursor.execute(qry)                   # execute(qry) is a method that sends an SQL query to the database for execution.
        r = self.mycursor.fetchone()                 # fetchone() is a method that fetches the next row of the result set, returning it as a tuple
        #con.commit()
        if r :
            #print("EXIST")
            ch = input("Are you sure you want to delete y/n : ")
            if ch =='y':
                qry = "delete from DOCTOR where D_ID = {};".format(x)
                self.mycursor.execute(qry)           # execute(qry) is a method that sends an SQL query to the database for execution.
                self.conn.commit()                   # conn.commit(), it instructs the database to make the changes permanent
                print("Successfully Deleted")
        else :
            print("Wrong Doctor ID")
            self.mycursor.close()                    # close() method is used to close the cursor, releasing any resources associated with it
#__________________________________________________________________________________________________________________________________________________________________________________________________        
    def doctor_search(self) :                        # USER CAN SEARCH DOCTOR DETAILS
        x = int(input("Enter Doctor ID : "))
        qry = "select * from DOCTOR where D_ID = {};".format(x)
        df = pd.read_sql(qry,self.conn)
        # print(df,"\n")
        print(tabulate(df , headers = 'keys' , tablefmt = 'psql' , showindex = False))
        self.mycursor.execute(qry)                   # execute(qry) is a method that sends an SQL query to the database for execution.
        self.mycursor.fetchall()                     #  fetchall() is a method that retrieves all the remaining rows from the last executed SQL statement as a list of tuples
        self.conn.commit()                           # conn.commit(), it instructs the database to make the changes permanent
        #self.mycursor.close()
#__________________________________________________________________________________________________________________________________________________________________________________________________        
    
              
            
    
    
         
    
    