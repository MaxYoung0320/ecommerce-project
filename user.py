import sqlite3
import sys
import itertools

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
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed connection.")

        ## exits the program if unsuccessful
            sys.exit()

        ## cursor to send queries through
        cursor = connection.cursor()

        while(1):
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            ## selects the entry with a matching email and password
            cursor.execute(f"SELECT * FROM {self.tableName} WHERE Email = '{email}' AND Password = '{password}'")
            result = cursor.fetchall()

            if not result:
                ## when the select query doesn't match an entry
                print()
                print("Failed Login: The email and password does not match an exisiting account")
                print("1 - Try Again")
                print("2 - Return To Main Menu")
                choice = int(input("Type a Number: "))
                if (choice == 2):
                    return False
                print()
            else:
                ## sets userID/loggedIn
                self.userID = result[0][-1]
                self.loggedIn = True
                print()
                print("Successfully Logged In")
                return True
    def logout(self):
        self.userID = ""
        self.loggedIn = False
    def viewAccountInformation(self):
        ## attempts to connect to the database
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed connection.")

        ## exits the program if unsuccessful
            sys.exit()

        ## cursor to send queries through
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM User WHERE UserID == '{self.userID}'")


        result = cursor.fetchall()[0]
        ## categories will match the query in result
        categories = ["Email", "Password", "First Name", "Last Name", "Address", "City", "State", "Zip", "Payment", "UserID"]

        ##prints the category and its corresponding result
        for (cat, val) in zip(categories, result):
            print(f"{cat}: {val}")

    def createAccount(self):
        #inputs for account information
        print()
        print("Enter Account Info")
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")
        firstName = input("Enter Your First Name: ")
        lastName = input("Enter Your Last Name: ")
        address = input("Enter Your Address: ")
        city = input("Enter Your City: ")
        state = input("Enter Your State: ")
        zip = input("Enter Your Zip Code: ")
        payment = input("Enter Your Payment Information: ")
        print()

        ## attempts to connect to the database
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed connection.")

        ## exits the program if unsuccessful
            sys.exit()

        ## cursor to send queries through
        cursor = connection.cursor()
        
        #insert values
        cursor.execute(f"INSERT INTO User(Email, Password, FirstName, LastName, Address, City, State, Zip, Payment, UserID) VALUES('{email}', '{password}', '{firstName}', '{lastName}', '{address}', '{city}', '{state}','{zip}', '{payment}','{email}')")
        connection.commit()

        print("Account Successfully Created")

    def getLoggedIn(self):
        return self.loggedIn
    def getUserID(self):
        return self.userID

 