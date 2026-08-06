import sqlite3

# Connect to database
conn=sqlite3.connect("students.db")

# Create a cursor
cursor=conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    branch TEXT
)
""")

# Read data
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Save changes
conn.commit()

print("Data read successfully")

# Close connection
conn.close()