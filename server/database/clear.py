import sqlite3

# clear likes of all users and articles

conn = sqlite3.connect('database/db.sqlite3')
cursor = conn.cursor()

cursor.execute('UPDATE users SET likes = ""')
cursor.execute('UPDATE articles SET likes = 0')
conn.commit()
