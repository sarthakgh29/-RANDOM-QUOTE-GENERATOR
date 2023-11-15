import mysql.connector

# Replace these with your MySQL database details
mysql_host = "localhost"
mysql_user = "uruser"
mysql_password = "urpass"

# Connect to MySQL (usually, you need a superuser account to create a database)
connection = mysql.connector.connect(host=mysql_host, user=mysql_user, password=mysql_password)
cursor = connection.cursor()

# Create a new database named "proj"
try:
    cursor.execute("CREATE DATABASE proj")
    print("Database 'proj' created successfully.")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")

# Use the "proj" database
cursor.execute("USE proj")

# Create the "quotes" table
create_table_query = """
CREATE TABLE quotes (
    quote_id INT AUTO_INCREMENT PRIMARY KEY,
    quote_text TEXT NOT NULL,
    author VARCHAR(255) NOT NULL
)
"""
try:
    cursor.execute(create_table_query)
    print("Table 'quotes' created successfully.")
except mysql.connector.Error as err:
    print(f"Error creating table: {err}")

# Close the connection
cursor.close()
connection.close()
