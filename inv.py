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
            print(i[6])

        

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

    def decreaseStock(self, ISBN):
        try:
            connection = sqlite3.connect("db.db")

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        print()

        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Inventory WHERE title LIKE '{book}'" )

        result = cursor.fetchall()
        for i in result:
            numbooks = i[6]
            newnumbooks = numbooks - 1
    

