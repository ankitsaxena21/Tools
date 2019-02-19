//use a server eg.Xampp or apache to run these scripts on your brower
#!C:\Users\Ankit\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html")
print()
import cgi

print("<h1>Welcome to python Web programming</h1>")
print("<hr/>")

form = cgi.FieldStorage()
roll = form.getvalue("roll")
name = form.getvalue("name")

import mysql.connector
con = mysql.connector.connect(user='root', password='', host='localhost', database='addpy')
cur = con.cursor()

cur.execute("INSERT INTO student values(%s,%s)", (roll,name))
con.commit()
cur.close()
con.close()
print("<h1>Record Submitted Congo.</h1>")