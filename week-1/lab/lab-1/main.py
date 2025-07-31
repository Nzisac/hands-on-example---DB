import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root", # Add user
    password="pass123" # Add your password
)

# Create a cursor object
cursor = conn.cursor()

# Create a new database
database_name = "nzisa" # Add a unique Database name
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

print(f"Database '{nzisa}' created successfully!")

# Close the connection
cursor.close()
conn.close()
