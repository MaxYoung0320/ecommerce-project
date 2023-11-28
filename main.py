from inv import inv
from user import User

print("Hello World")

viewInv = inv("", "")
viewInv.viewInventory()
isbn = input("Enter the isbn to delete: ")
viewInv.decreaseStock(isbn)

# viewInv = inv("", "")

# viewInv.viewInventory()


user = User("db.db", "User")
user.createAccount()
user.login()

user.viewAccountInformation()

user.viewAccountInformation()

user.viewAccountInformation()

user.viewAccountInformation()

