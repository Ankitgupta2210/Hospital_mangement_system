import mysql.connector
mysql = mysql.connector.connect( # mysql is showing the connection to the mysql-server
host="sql12.freemysqlhosting.net",
port='3306',
user="sql12620453",
password = 'pxkWxqJnYA')
mycursor = mysql.cursor()