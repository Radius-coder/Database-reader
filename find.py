#! C:\Program Files (x86)\Python38-32/python.exe
import cgi, cgitb, re, datetime, dbfunc, mysql.connector;
from mysql.connector import Error
cgitb.enable()

#Connect to database
conn = dbfunc.getConnection()
cur = conn.cursor()

# Create instance of FieldStorage
form = cgi.FieldStorage()
print('content-type: text/html \n')
print("<HTML><TITLE>NHS Record Finder</TITLE>")

fh = open("NHS.css", "r")
temp = fh.readlines()

page = ""
for line in temp:
    page += (line)
fh.close()

print(page)

#vairable intialisation
fName = ""

fName = form.getvalue('fName')
if (fName != None):
    fName = (fName).replace(' ', '')

#Your fName must not be blank
if fName != None:
    if len(fName) > 2 :
        fNameCheck = 0
    else:
        fNameCheck = -1


 #If any of the tests are not passed, and error message is dispalyed as appropriate
    if fNameCheck == -1:

        errMsg = """<table align='center' style='background-COLOR: #ffffff;
        border-radius: 25px;padding: 20px;
        float: none; clear: both;'>"""

        if (fNameCheck == -1):
            errMsg+=("<tr><th style='font-size: 20px; '>Please enter a valid first name</th></tr>")

        errMsg +=("</table><br/>")
        print(errMsg)

    else:
        
            
            cur.execute("SELECT * FROM customer")
            try:
                rows = cur.fetchall()
                for aline in rows:
                    if aline[1] == fName:
                        print("YES")
            except:
                print("error finding category")



