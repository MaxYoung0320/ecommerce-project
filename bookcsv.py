import csv
import random
import sqlite3
import sys

try:
    connection = sqlite3.connect("db.db")

    print("Successful Connection")

except:
    print("Failed Connection")
    sys.exit()

cursor = connection.cursor()

# cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' ;")

# table_names = cursor.fetchall()

# print("Table Names: ")
# for table_name in table_names:
#     print(table_name)

book_genres = ["fiction", "non-fiction", "fantasy", "horror", "historical", "drama", "folklore", "romance", "young adult", "poetry"]
with open("books.csv") as f:
    next(f)
    for line in f:
        isbn = line.split(',')[5] # isbn
        titleBeforeApostrophes = line.split(',')[1] # title
        title = titleBeforeApostrophes.replace("'", "''") # some titles have apostrophes that need escaping
        authorBeforeApostrophes = line.split(',')[2] # author
        author = authorBeforeApostrophes.replace("'", "''") # some authors have apostrophes that need escaping
        pages = line.split(',')[7] # pages
        release_date = line.split(',')[10] # release date
        genre = random.choice(book_genres) # genre
        stock = random.randint(0, 50) # stock

        cursor.execute(f"INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) VALUES ('{isbn}', '{title}', '{author}', '{genre}', '{pages}', '{release_date}', '{stock}')")
        connection.commit()
        print(cursor.rowcount, "record inserted.")
        print()


        #SELECT OJGODKFG WHERE Title LIKE 'title'