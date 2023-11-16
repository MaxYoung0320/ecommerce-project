import sqlite3
import sys

class inv():
    #opening the db
    try:
    connection = sqlite3.connect("methods.db")

    print("Successful connection.")

except:
    print("Failed connection.")

    sys.exit()

print()

cursor = connection.cursor()



    def __init__(self):
        self.databaseName = databaseName
        self.tableName = tableName

    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def inventory(self):
        
    def viewInventory(self):

        cursor.execute("SELECT * FROM books")

        

    def searchInventory(self):

        print("Enter the title of the book: ")
        
        cursor.execute("SELECT * FROM books")

        result = cursor.fetchall()

        print("Entire result set: ", result, sep="\n", end="\n\n\n")

        for x in result:

            print("Entire row:", x, "\n") ## all

            print("Row broken down into each column: ")
            
            for y in x:
                print(y)
            
            print()

            print("ISBN:", x[0]) ## only the ISBN
            print("Title:", x[1], "\tAuthor:", x[2])
            print("\n\n")


    def decreaseStock(self, ISBN):

    

