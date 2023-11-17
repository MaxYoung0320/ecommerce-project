import sqlite3
import sys

class inv():

    def __init__(self):
        self.databaseName = ""
        self.tableName = ""

    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def inventory(self):
        print()
    def viewInventory(self):
        try:
            connection = sqlite3.connect("db.db")

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        print()

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Inventory")

        result = cursor.fetchall()
        for i in result:
            print(i[1])

        

    def searchInventory(self):
        try:
            connection = sqlite3.connect("db.db")

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        print()

        cursor = connection.cursor()

        book = input("Enter the title of the book: ")
        
        cursor.execute(f"SELECT * FROM Inventory WHERE title LIKE '%{book}%'" )

        result = cursor.fetchall()
        for i in result:
            print(i[1])
        #print("Entire result set: ", result, sep="\n", end="\n\n\n") 

    def decreaseStock(self):
        try:
            connection = sqlite3.connect("db.db")

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        print()

        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM Inventory")
        result = cursor.fetchall()
        for i in result:
            print(i[0],"-", i[1])
        book = input("Enter the isbn of the book to buy: ")

        cursor.execute(f"SELECT * FROM Inventory WHERE isbn LIKE '{book}'" )

        result1 = cursor.fetchall()
        for i in result1:
            print(i[0], i[1], i[6], "- old stock")
            numbooks = i[6]
            isbn = i[0]
            bookName = i[1]
            newnumbooks = numbooks - 1
        cursor.execute(f"UPDATE Inventory SET stock = '{newnumbooks}' WHERE isbn = '{isbn}'")
        print(isbn, bookName, newnumbooks, "- new stock")
        
    

