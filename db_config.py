import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # নিজের পাসওয়ার্ড দিন
        database="expense_tracker"
    )
