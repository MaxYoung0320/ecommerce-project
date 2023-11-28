from inv import inv
from user import User

print("Hello World")

<<<<<<< HEAD
viewInv = inv("", "")
viewInv.viewInventory()
isbn = input("Enter the isbn to delete: ")
viewInv.decreaseStock(isbn)
=======
# viewInv = inv("", "")

# viewInv.viewInventory()


user = User("db.db", "User")
user.createAccount()
user.login()
user.viewAccountInformation()
>>>>>>> ba2554bc88b407bded2c871b86ff64b2913c94df
