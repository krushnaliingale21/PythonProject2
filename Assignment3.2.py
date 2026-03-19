# Take input list from user
items = list(map(int, input("Enter item numbers separated by space: ").split()))

# a) Total number of items
print("Total items:", len(items))

# b) Last item
print("Last item:", items[-1])

# c) Sorted list
sorted_items = sorted(items)
print("Sorted list:", sorted_items)

# d) Check item 515
if 515 in items:
    print("Yes")
else:
    print("No")

# e) Add new items and sort
items.extend([121, 321])
items.sort()
print("Updated sorted list:", items)