import mysql.connector
mydb= mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='@!2002bisesh',
    port='3306',
    database='democlass')

mycursor=mydb.cursor()
mycursor.execute('Select * from tbl_employee')
users=mycursor.fetchall()
for fname in users:
    print(fname)
    print('fname:'+fname[1])




