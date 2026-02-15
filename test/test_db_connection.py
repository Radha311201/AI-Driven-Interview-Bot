import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def test_db_connection():
    try:
        connection = psycopg2.connect(os.getenv('DATABASE_URL'))
        cursor = connection.cursor()
        cursor.execute('SELECT 1')
        print('Database connection successful!')
        cursor.close()
        connection.close()
    except Exception as e:
        print(f'Database connection failed: {e}')

if __name__ == '__main__':
    test_db_connection()
