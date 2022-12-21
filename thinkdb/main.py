import sqlite3

with sqlite3.connect("database.sqlite") as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    author VARCHAR,
    likes INT,
    content VARCHAR
    )""")

    # title, author, content
    #
    # values = [
    #     (title, author, content)
    # ]
    #
    #
    # cursor.executemany(
    #     "INSERT INTO articles(title, author, content) VALUES(?, ?, ?)",
    #     values)

    cursor.execute("SELECT * FROM articles")
    #cursor.execute("DELETE FROM articles WHERE id = 3")
    print(cursor.fetchall())


with sqlite3.connect("database1.sqlite") as db:
   cursor = db.cursor()

   cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nickname VARCHAR,
        password VARCHAR,
        id_likes VARCHAR
        )""")

        # title, author, content
        #
        # values = [
        #     (title, author, content)
        # ]
        #
        #
        # cursor.executemany(
        #     "INSERT INTO articles(title, author, content) VALUES(?, ?, ?)",
        #     values)

   cursor.execute("SELECT * FROM users")
   # cursor.execute("DELETE FROM articles WHERE id = 3")
   print(cursor.fetchall())
