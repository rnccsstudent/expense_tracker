import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()  # এটি লোকাল .env ফাইল থেকে variables লোড করে

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
