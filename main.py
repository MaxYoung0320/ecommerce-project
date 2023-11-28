from inv import inv
from user import User

print("Hello World")

# viewInv = inv("", "")

# viewInv.viewInventory()


user = User("db.db", "User")
user.createAccount()
user.login()
user.viewAccountInformation()