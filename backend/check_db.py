import sqlite3

conn = sqlite3.connect("honestybox.db")
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Try selecting from `user`
try:
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    print("User rows:", rows)
except Exception as e:
    print("Error querying user table:", e)

conn.close()

