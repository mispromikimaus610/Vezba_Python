import mysql.connector
import json


conn = mysql.connector.connect(
    host='localhost',
    user="root",
    password="root",
    database="test"   
)
cursor=conn.cursor()

cursor.execute("""
    Create table if not exists users(
                       
               
""")