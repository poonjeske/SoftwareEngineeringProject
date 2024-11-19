import mysql.connector
from mysql.connector import Error,ProgrammingError

conn = mysql.connector.connect(
    host='127.0.0.1',
    database='db',
    user='root',
    password='poon@psm16828'
)
if conn.is_connected():
    print('Connected to database.')

