import sqlite3
import sys

class User():
    def __init__(self):
        self.databaseName = ""
        self.tableName = ""
        self.loggedIn = False
        self.userID = ""
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = False
        self.userID = ""
    def login(self):

        ## attempts to connect to the database
        try:
            connection = sqlite3.connect("methods.db")

            print("Successful connection.")

        except:
            print("Failed connection.")

        ## exits the program if unsuccessful
            sys.exit()

        print() ## spacing's sake

        ## cursor to send queries through
        cursor = connection.cursor()

        while(1):
            email = input("Enter your email: ")
            print()
            password = input("Enter your password: ")

            cursor.execute(f"SELECT * FROM Users WHERE ")
            result = cursor.fetchall()

        #ask for email/password
        #verify that they are correct
        #keep looping until they are correct
        #offer option to exit the menu and return false if they do
        return True #and update userID and set loggedIn to true
    def logout(self):
        self.userID = ""
        self.loggedIn = False
    def viewAccountInformation(self):
        #set up query to view all account info
        print()
    def createAccount(self):
        #inputs for account info + query to insert into user db
        print()
    def getLoggedIn(self):
        return self.loggedIn
    def getUserID(self):
        return self.userID

 