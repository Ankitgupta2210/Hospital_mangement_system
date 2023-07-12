'''                                                       HOSPITAL_MANAGEMENT_SYSTEM                                                                      '''
'''                                                              MAIN_MODULE                                                                              '''

import os                                                  # IMPORTING OPERATING SYSTEM PROPERTIES
import mysql.connector                                     # IMPORTING SQL_CONNECTOR LYBRARY THAT WILL HELP US CONNECTING TO DATABASE
from OPD_MODULE import connect_OPD_TO_MAIN                 # IMPORTING OPD_MODULE WITH CLASS(connect_OPD_TO_MAIN) to connect OPD MODULE to the sql database
from DOCTOR_MODULE import connect_DOCTOR_TO_MAIN           # IMPORTING DOCTOR_MODULE WITH CLASS(connect_DOCTOR_TO_MAIN) to connect DOCTOR MODULE to the sql database
from REPORT_MODULE import connect_REPORT_TO_MAIN           #  ---------------------SAME  AS  ABOVE-------------------------
from APPOINTMENT_MODULE import connect_APPOINTMENT_TO_MAIN #  ---------------------SAME  AS  ABOVE-------------------------
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
conn = mysql.connector.connect(                            # CONNECTION TO THE MYSQL DATABASE #
    host="localhost",                                      #----------------------------------#
    port='3306',                                           #----------------------------------#
    user="root",                                           #----------------------------------#
    password = '1234567890',                               #----------------------------------#
    database = 'hospital')                                 #----------------------------------#
conn = conn                                                       
mycursor = conn.cursor()
# connection = conn.connect()
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
while(True):                                               # WHILE LOOP WILL RUN THE CODE AGAIN WHEN ANY ONE OPERATION IS COMPLETED
    print("="*80)
    print("\t\t\t Hospital Management System\n")           # DISPLAYING THE INPUT OPTIONS FOR USER IN TABULER FORMAT
    print("="*80)
    print("\t\t\t\tEnter your choice")
    print("\t\t\t\t1. OPD\n\t\t\t\t2. Doctor Details\n\t\t\t\t3. Appointment\n\t\t\t\t4. Reports\n\t\t\t\t5. Exit\n")
    print("="*80)
    choice = int(input("ENTER YOUR CHOICE : "))
    os.system('cls')                                       # os.system('cls') clears the console screen after each operation.
    if choice == 1: # OPD 
        opd_module = connect_OPD_TO_MAIN(conn, mycursor)           
        # opd_module is calling and establishing connection to the server and the class connect_OPD_TO_MAIN only when the user choose 1
#__________________________________________________________________________________________________________________________________________________________________________________________________                                                                   
        while True:
            os.system('cls')
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. New OPD\n\t\t\t\t2. Edit OPD\n\t\t\t\t3. Delete OPD\n\t\t\t\t4. Search\n\t\t\t\t5. Back to Main Menu")
            # \t is an escape sequence for a horizontal tab. It adds a tabulation to the output, indenting the text.
            choice = int(input("ENTER YOUR CHOICE : "))
#__________________________________________________________________________________________________________________________________________________________________________________________________            
            if choice == 1:
                opd_module.opd_input()                     # CALLING opd_input FROM opd_module
                break
            elif choice == 2:
                opd_module.opd_edit()                      # CALLING opd_edit FROM opd_module
                break
            elif choice == 3:
                opd_module.opd_delete()                    # CALLING opd_delete FROM opd_module
                break
            elif choice == 4:
                opd_module.opd_search()                    # CALLING opd_search FROM opd_module
                break
            elif choice == 5:                              # INPUT 5 WILL TAKE USER BACK TO MAIN MENU
                break
            else:
                print("Invalid input")                     # INPUT GREATER THEN 5 WILL SHOW INVALID INPUT
                break
#__________________________________________________________________________________________________________________________________________________________________________________________________                        
    elif choice == 2: # Doctor Details
        doctor_module = connect_DOCTOR_TO_MAIN(conn, mycursor)     
        # doctor_module is calling and establishing connection to the server and the class connect_DOCTOR_TO_MAIN only when the user choose 2.
        while True:
            os.system('cls')                               # os.system('cls') clears the console screen after each operation.
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. Add New Doctor\n\t\t\t\t2. Edit Doctor Details\n\t\t\t\t3. Delete Doctor Details\n\t\t\t\t4. Search Doctor Details\n\t\t\t\t5. Back to Main Menu")
            # \t is an escape sequence for a horizontal tab. It adds a tabulation to the output, indenting the text.
            choice = int(input("ENTER YOUR CHOICE : "))
            
            if choice == 1:
                doctor_module.doctor_input()               # CALLING doctor_input FROM doctor_module
                break
            elif choice == 2:
                doctor_module.doctor_edit()                # CALLING doctor_edit FROM doctor_module
                break
            elif choice == 3:
                doctor_module.doctor_delete()              # CALLING doctor_delete FROM doctor_module
                break
            elif choice == 4:
                doctor_module.doctor_search()              # CALLING doctor_search FROM doctor_module
                break
            elif choice == 5:                              # INPUT 5 WILL TAKE USER BACK TO MAIN MENU
                break
            else:
                print("Invalid input")                     # INPUT GREATER THEN 5 WILL SHOW INVALID INPUT
                break
#__________________________________________________________________________________________________________________________________________________________________________________________________              
    elif choice == 3: # Appointment
        appointment_module = connect_APPOINTMENT_TO_MAIN(conn, mycursor)
        # appointment_module is calling and establishing connection to the server and the class connect_APPOINTMENT_TO_MAIN only when the user choose 3
        while True:
            os.system('cls')                               # os.system('cls') clears the console screen after each operation.
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. Appointment\n\t\t\t\t2. Appointment Edit\n\t\t\t\t3. Back to Main Menu")
            choice = int(input("Select the Action : "))
            
            if choice == 1:
                appointment_module.appointment()           # CALLING appointment_module FROM appointment
                break
            elif choice == 2:
                appointment_module.appointment_edit()      # CALLING appointment_edit FROM appointment
                break
            elif choice == 3:                              # INPUT 3 WILL TAKE USER BACK TO MAIN MENU
                break
            else:
                print("INVALID INPUT")                     # INPUT GREATER THEN 3 WILL SHOW INVALID INPUT
                break
#__________________________________________________________________________________________________________________________________________________________________________________________________               
    elif choice == 4: # Reports
        report_module = connect_REPORT_TO_MAIN(conn, mycursor)
          # report_module is calling and establishing connection to the server and the class connect_REPORT_TO_MAIN only when the user choose 4
        while True:
            os.system('cls')                               # os.system('cls') clears the console screen after each operation.
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. Display Doctors List\n\t\t\t\t2. Display Patient List\n\t\t\t\t3. Doctor History\n\t\t\t\t4. Patient History\n\t\t\t\t5. OPD Details\n\t\t\t\t6. Max Diagnose (Chart)\n\t\t\t\t7. Back to Main Menu")
            choice = int(input("Select the Action : "))
            
            if choice == 1:
                report_module.doctor_list()                # CALLING doctor_list FROM report_module
                break
            elif choice == 2:
                report_module.patient_list()               # CALLING patient_list FROM report_module
                break
            elif choice == 3:
                report_module.doctor_treatment()           # CALLING doctor_treatment FROM report_module
                break
            elif choice == 4:
                report_module.patient_history()            # CALLING patient_history FROM report_module
                break
            elif choice == 5:
                report_module.opd_list()                   # CALLING opd_list FROM report_module
                break
            elif choice == 6:
                report_module.analysis_chart()             # CALLING analysis_chart FROM report_module
                break
            elif choice == 7:                              # INPUT 7 WILL TAKE USER BACK TO MAIN MENU
                break
            else:
                print("INVALID INPUT")                     # INPUT GREATER THEN 7 WILL SHOW INVALID INPUT
                break
#__________________________________________________________________________________________________________________________________________________________________________________________________ 
    elif choice == 5:                                      # CHOOSING 5 WILL TAKE THE USER BACK TO MAIN MENU 
        break
#__________________________________________________________________________________________________________________________________________________________________________________________________    
    else:
        print("INVALID INPUT")                             # INPUT GREATER THEN 5 WILL SHOW INVALID INPUT
        break
#__________________________________________________________________________________________________________________________________________________________________________________________________









