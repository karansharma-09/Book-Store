import sqlite3
#CREATING database 
Mybookstore=sqlite3.connect("bookstore.db")
curstore=Mybookstore.cursor()

# creating books table
q1='''CREATE TABLE books(
book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
author TEXT NOT NULL,
price REAL NOT NULL);'''
curstore.execute(q1)

Sample_data = [
        ("Think Python", "Allen B. Downey", 475.00),
        ("Learning Python", "Mark Lutz", 850.00),
        ("Introduction to Algorithms", "Thomas H. Cormen", 1200.00),
        ("The C Programming Language", "Brian W. Kernighan", 350.00)
    ]

curstore.executemany('''
INSERT INTO books (title ,author,price)
VALUES (?,?,?)''',Sample_data)

#commit changes
Mybookstore.commit()

#closing the connection
Mybookstore.close()

print("Database created successfully")
