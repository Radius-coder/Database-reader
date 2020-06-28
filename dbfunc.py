#! C:\Program Files (x86)/Python38-32/python.exe
import cgi, cgitb, mysql.connector

# MYSQL CONFIG VARIABLES
host           = "localhost";
db             = "patients";
user           = "root";
passwd         = ""



def getConnection():
	conn = mysql.connector.connect(user=user,
				password=passwd,
				host=host,
				database=db)
	return conn



