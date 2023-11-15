import mysql.connector

# Function to add a new quote to the "quotes" table
def add_quote():
    quote_text = input("Enter the quote text: ")
    author = input("Enter the author: ")

    try:
        cursor.execute("INSERT INTO quotes (quote_text, author) VALUES (%s, %s)", (quote_text, author))
        connection.commit()
        print("Quote added successfully!")
    except mysql.connector.Error as err:
        print(f"Error adding quote: {err}")
        connection.rollback()

# Connect to the MySQL database (update with your actual details)
connection = mysql.connector.connect(
    host="localhost",
    user="uruser",
    password="urpass",
    database="proj"
)
cursor = connection.cursor()

# Use the "quotes" database
cursor.execute("USE proj")

# Main program loop to add quotes
while True:
    add_quote()
    another = input("Do you want to add another quote? (y/n): ")
    if another.lower() != 'y':
        break

# Close the connection
cursor.close()
connection.close()
