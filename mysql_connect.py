import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="haideepx"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sql_haideep")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
