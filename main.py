from inv import inv
from user import User
from cart import Cart

print("Hello World")

# create class instances
inventory = inv("db.db", "User")
user = User("db.db", "User")
cart = Cart("db.db", "Cart")

while(1):
    # second while loop is for the before login menu only
    while(1):
        print("1 - Login")
        print("2 - Create Account")
        print("3 - Logout")
        choice = int(input("Enter a number: "))
        match choice:
            case 1:
                if(user.login()):
                    #will send the user to the next menu
                    break
                else:
                    print()
            case 2:
                user.createAccount()
            case 3: 
                if (not user.getLoggedIn()):
                    print()
                    print("You Are Already Logged Out")
                    print()
                else:
                    user.logout()

