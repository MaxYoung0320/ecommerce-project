from inv import inv
from user import User
from cart import Cart


# create class instances
inventory = inv("db.db", "User")
user = User("db.db", "User")
cart = Cart("db.db", "Cart")

def cartInfo():
    while(1):
        print()
        print("1 - view cart")
        print("2 - add to cart")
        print("3 - remove from cart")
        print("4 - check out")
        print("5 - Go Back")
        choice = int(input("Enter a number: "))
        match choice:
            case 1:
                cart.viewCart(user.getUserID(), "db.db")
            case 2:
                inventory.viewInventory()
                print()
                isbn = input("Enter the ISBN of the book to purchase: ")
                
                cart.addToCart(user.getUserID(), isbn)
            case 3:
                cart.viewCart(user.getUserID(), "db.db")
                print()
                isbn2 = input("Enter the ISBN of the book to remove: ")

                cart.removeFromCart(user.getUserID(), isbn2)
            case 4:
                cart.checkOut(user.getUserID())
            case 5:
                afterLogin()
                break

def invInfo():
    while(1):
        print()
        print("1 - view inventory")
        print("2 - search inventory")
        print("3 - Go Back")
        choice1 = int(input("Enter a number: "))
        match choice1:
            case 1:
                inventory.viewInventory()
            
            case 2:
                inventory.searchInventory()
            
            case 3:
                afterLogin()
                break

def afterLogin():
    while(1):
        print()
        print("1 - view account information")
        print("2 - Inventory information")
        print("3 - cart information")
        print("4 - Logout")
        choice2 = int(input("Enter a number: "))
        match choice2:
            case 1:
                user.viewAccountInformation()
            case 2:
                invInfo()
            case 3:
                cartInfo()
            case 4:
                user.logout()
                break

def beforeLogin():
    while(1):
        print()
        print("1 - Login")
        print("2 - Create Account")
        print("3 - Exit")
        choice3 = int(input("Enter a number: "))
        match choice3:
            case 1:
                if(user.login()):
                    #will send the user to the next menu
                    break
                else:
                    print()
            case 2:
                user.createAccount()
            case 3:
                break

            
while(1):
    beforeLogin()
    if(not user.getLoggedIn()):
        break
    afterLogin()
    if(not user.getLoggedIn()):
        break
print()
print("Thanks for Shopping!")


    


