import mysql.connector


mydb = mysql.connector.connect( 
    host = 'localhost',
    database = 'mysql', 
    user = 'root', 
    password = 'admin'
    )

mycursor = mydb.cursor()

'''
mycursor.execute("CREATE DATABASE testdb")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

'''
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)