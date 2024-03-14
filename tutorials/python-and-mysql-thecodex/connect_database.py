import mysql.connector

mydb = mysql.connector.connect(

    host='localhost',
    user = 'root', 
    password = 'admin',
    database = 'mysql'
    )

# object that holds a representation of the database in python
mycursor = mydb.cursor()

'''
# creates a new database
mycursor.execute("CREATE DATABASE testdb")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

# creates a new table with 2 collumns; name and age
mycursor.execute("CREATE TABLE testdb.students (name VARCHAR(255), age INTEGER(10))")
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

# addin new records to the table
sqlFormula = "INSERT INTO testdb.students (name, age) VALUES (%s, %s)"
students = [
    ("Joao",25), 
    ("Andre",28), 
    ("Pedro",38), 
    ("Melissa",22), 
    ("Adriana",48), 
]
mycursor.executemany(sqlFormula,students)

# listing data frmo the database
mycursor.execute("SELECT * FROM testdb.students;")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)

 
# changin records on a table
sql = "UPDATE testdb.students SET age = 45 WHERE name ='Andre'"
mycursor.execute(sql)
# listing data frmo the database
mycursor.execute("SELECT * FROM testdb.students ORDER BY age DESC LIMIT 5 OFFSET 3")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)

sql = "DELETE FROM testdb.students WHERE name = 'Andre'"
mycursor.execute(sql)


busca = "SELECT * FROM testdb.students"
mycursor.execute(busca)
for line in mycursor:
    print(line)
'''
# removing a table
sql = "DROP TABLE IF EXISTS testdb.students"
mycursor.execute(sql)

#mydb.commit()