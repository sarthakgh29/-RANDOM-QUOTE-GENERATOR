import tkinter as tk
import random
import mysql.connector

# Establish a connection to your MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="uruser",
    password="urpass",
    database="proj"
)

# Create a cursor object to interact with the database
db_cursor = db_connection.cursor()

# Function to retrieve a random quote from the MySQL database
def show_random_quote():
    db_cursor.execute("SELECT quote_text, author FROM quotes ORDER BY RAND() LIMIT 1")
    random_quote = db_cursor.fetchone()
    if random_quote:
        quote_label.config(text=f'"{random_quote[0]}" - {random_quote[1]}')
    else:
        quote_label.config(text="No quotes available in the database.")

# Create the main window
root = tk.Tk()
root.title("Random Quote Generator")

# Create a label for the quote
quote_label = tk.Label(root, text="", wraplength=300, font=("Helvetica", 12))
quote_label.pack(pady=20)

# Create a button to show a random quote
quote_button = tk.Button(root, text="Show Random Quote", command=show_random_quote)
quote_button.pack()

# Run the GUI main loop
root.mainloop()

# Close the database connection when the program exits
db_cursor.close()
db_connection.close()import tkinter as tk
import random
import mysql.connector

# Establish a connection to your MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="uruser",
    password="urpass",
    database="proj"
)

# Create a cursor object to interact with the database
db_cursor = db_connection.cursor()

# Function to retrieve a random quote from the MySQL database
def show_random_quote():
    db_cursor.execute("SELECT quote_text, author FROM quotes ORDER BY RAND() LIMIT 1")
    random_quote = db_cursor.fetchone()
    if random_quote:
        quote_label.config(text=f'"{random_quote[0]}" - {random_quote[1]}')
    else:
        quote_label.config(text="No quotes available in the database.")

# Create the main window
root = tk.Tk()
root.title("Random Quote Generator")

# Create a label for the quote
quote_label = tk.Label(root, text="", wraplength=300, font=("Helvetica", 12))
quote_label.pack(pady=20)

# Create a button to show a random quote
quote_button = tk.Button(root, text="Show Random Quote", command=show_random_quote)
quote_button.pack()

# Run the GUI main loop
root.mainloop()

# Close the database connection when the program exits
db_cursor.close()
db_connection.close()
