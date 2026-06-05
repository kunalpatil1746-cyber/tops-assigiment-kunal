
fruits = ["Apple", "Banana", "Mango"]


fruits.append("Orange")
print("After append():", fruits)


fruits.insert(1, "Grapes")
print("After insert():", fruits)

fruits.remove("Banana")
print("After remove():", fruits)

removed_item = fruits.pop(0)
print("Removed item:", removed_item)
print("After pop():", fruits)