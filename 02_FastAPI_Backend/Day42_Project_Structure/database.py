import sqlite3
conn=sqlite3.connect(
    "students.db",
    check_same_thread=False
)

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    branch TEXT
)
""")

conn.commit()