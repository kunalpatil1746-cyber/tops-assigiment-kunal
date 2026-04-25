list = ["apple", "banana", "cherry"]
search_target = "banana"

# Simple for loop to iterate through each item
for item in list:
    # If condition to check for a match
    if item == search_target:
        print(f"String '{search_target}' found in the list!")
        break
else:
    print("String not found.")

