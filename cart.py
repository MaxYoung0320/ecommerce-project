from inv import inv  
import sqlite3
import sys

class Cart():
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.inventory_obj = inv(databaseName, tableName)  

    def viewCart(self, userID, inventoryDatabase):
        self.inventory_obj.viewInventory(userID, inventoryDatabase)

    def addToCart(self, userID, ISBN):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()
            
            cursor.execute(f"INSERT INTO {self.tableName} VALUES (?, ?)", (userID, ISBN))
            connection.commit()
            
            print("Book added to the cart successfully.")

        except sqlite3.Error as error:
            print("Failed to add book to the cart:", error)

        if connection:
            connection.close()

    def removeFromCart(self, userID, ISBN):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()

            cursor.execute(f"DELETE FROM {self.tableName} WHERE userID = ? AND ISBN = ?", (userID, ISBN))
            connection.commit()

            print("Book removed from the cart successfully.")

        except sqlite3.Error as error:
            print("Failed to remove book from the cart:", error)

        if connection:
            connection.close()

    def checkOut(self, userID):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()

            cursor.execute(f"SELECT ISBN FROM {self.tableName} WHERE userID = ?", (userID,))
            books_in_cart = cursor.fetchall()

            cursor.execute(f"DELETE FROM {self.tableName} WHERE userID = ?", (userID,))
            connection.commit()

            print("Checked out successfully.")

            for book in books_in_cart:
                self.inventory_obj.decreaseStock(book[0]) 
                
        except sqlite3.Error as error:
            print("Failed to check out:", error)
            
        if connection:
            connection.close()

