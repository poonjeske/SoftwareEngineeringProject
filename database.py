import mysql.connector
from mysql.connector import Error,ProgrammingError

conn = mysql.connector.connect(
    host='127.0.0.1',
    database='db',
    user='root',
    password= #'<ใช้ db ของมึงเลย>'
)
if conn.is_connected():
    print('Connected to database.')

