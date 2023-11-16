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

        cursor.execute("SELECT * FROM Inventory")

        

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
        
        cursor.execute(f"SELECT * FROM Inventory WHERE title LIKE '{book}'" )

        result = cursor.fetchall()

        print("Entire result set: ", result, sep="\n", end="\n\n\n")

    def decreaseStock(self, ISBN):
        print()
    

