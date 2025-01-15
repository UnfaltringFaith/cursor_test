import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="qwertry123",
    port="5432",
    client_encoding='utf8'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

print(cursor.fetchall())