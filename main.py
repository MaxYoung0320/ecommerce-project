from inv import inv

print("Hello World")

viewInv = inv("", "")
viewInv.viewInventory()
isbn = input("Enter the isbn to delete: ")
viewInv.decreaseStock(isbn)