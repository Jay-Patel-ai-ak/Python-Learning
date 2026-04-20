# List Uniqueness checker 

items = ["apple", "banana", "orange", "apple", "mango", "grape", "banana"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)