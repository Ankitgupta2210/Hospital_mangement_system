'''                                                       HOSPITAL_MANAGEMENT_SYSTEM                                                                      '''
'''                                                             REPORT_MODULE                                                                             '''
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
import pandas as pd                                  # IMPORTING PANDAS TO RUN SQL QUERIES
import matplotlib.pyplot as plt                      # WE IMPORTED MATPLOTLIB TO CREATE GRAPH OF THE "Total Cases by Disease Symptoms"
from tabulate import tabulate                        # WE IMPORTED TABULATE TO DISPLAY THE QUERY OUTPUT IN A TABULATE FORMAT
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
class connect_REPORT_TO_MAIN:                        # CONNECTING THROUGH THE SQL_SERVER VIA MAIN_MODULE
    def __init__(self, conn, mycursor):
        self.conn = conn
        self.mycursor = mycursor
#__________________________________________________________________________________________________________________________________________________________________________________________________        
    def doctor_list(self):                           # DISPLAYING THE DOCTOR LIST
        qry = "SELECT * FROM DOCTOR;"
        df = pd.read_sql(qry, self.conn) # it executes the SQL query using the pandas library's read_sql() function.
        # It is convenient when you want to directly retrieve the query results as a DataFrame
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        # TABULATE is then used to print the DataFrame in a tabular format using the tabulate function.
        # tablefmt='mysql' :- This parameter sets the table format to "mysql," which mimics the style of tables in MYSQL.
        # Using tablefmt='psql'__ will use the format of PostgreSQL .
        # headers='keys':- This parameter specifies that the column names of the DataFrame should be used as the table headers.
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def patient_list(self):                          # DISPLAYING THE PATIENT LIST
        qry = "SELECT * FROM PATIENT;"
        df = pd.read_sql(qry, self.conn)
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def doctor_treatment(self):                      # DISPLAYING THE TREATMENTS DOCTORS HAS PERFORMED
        x = input("Enter DOCTOR's First Name: ")
        qry = "SELECT * FROM appointment WHERE D_FIRST_NAME = '{}';".format(x)
        df = pd.read_sql(qry, self.conn)
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def opd_list(self):                              # DISPLAYING OPD LIST
        B_DATE = input("Enter Beginning Date: ")
        END_DATE = input("Enter End date: ")
        qry = "SELECT APPOINTMENT.OPD_NO, APPOINTMENT.DATE_ON_ARRIVAL, APPOINTMENT.P_FIRST_NAME, APPOINTMENT.P_LAST_NAME, APPOINTMENT.D_FIRST_NAME, APPOINTMENT.D_LAST_NAME, APPOINTMENT.SYMPTOM, APPOINTMENT.TREATMENT, OPD.FEE FROM APPOINTMENT JOIN OPD ON APPOINTMENT.OPD_NO = OPD.OPD_NO WHERE APPOINTMENT.DATE_ON_ARRIVAL BETWEEN '{}' AND '{}';".format(B_DATE, END_DATE)
        df = pd.read_sql(qry, self.conn)
        print(tabulate(df, headers='keys', tablefmt='mysql', showindex=False)) 
        
        
      
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def patient_history(self):                       # DISPLAYING PATIENT HISTORY
        qry = "SELECT * FROM APPOINTMENT, OPD WHERE OPD.OPD_NO = APPOINTMENT.OPD_NO;"
        df = pd.read_sql(qry, self.conn)
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    def analysis_chart(self):                        # CREATING CHART THAT    
        qry = "SELECT SYMPTOM, COUNT(SYMPTOM) AS total_cases FROM APPOINTMENT GROUP BY SYMPTOM;"
        df = pd.read_sql(qry, self.conn)
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))  
                                                     # Print the DataFrame in a tabular format using tabulate
        
        plt.bar(df.SYMPTOM, df.total_cases)          # Create a bar chart using the symptom and total_cases columns from the DataFrame
        plt.title("Total Cases by Disease Symptoms") # Set the title for the chart
        plt.xlabel("Symptoms")                       # Set the x-label for the chart
        plt.ylabel("Total Cases")                    # Set the y-label for the chart
        plt.xticks(rotation=90)                      # Rotate the x-axis labels for better readability if needed
        plt.show()                                   # Display the chart
#__________________________________________________________________________________________________________________________________________________________________________________________________ 











