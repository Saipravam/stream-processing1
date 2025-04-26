import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST", "localhost"),
    database="userdb",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, email TEXT, phone INT)''')
conn.commit()

def create_user_db(user):
    cursor.execute('INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)', (user['name'], user['email'], user['phone']))
    conn.commit()

def update_user_db(user_id, user):
    cursor.execute('UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s', (user['name'], user['email'],user['phone'], user_id))
    conn.commit()

def delete_user_db(user_id):
    cursor.execute('DELETE FROM users WHERE id=%s', (user_id))
    conn.commit()