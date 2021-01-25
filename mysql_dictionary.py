from os import linesep
import mysql.connector
from mysql.connector.errors import custom_error_exception

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor =  conn.cursor()

word = input("Enter a word to search for: ")



query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No results")
