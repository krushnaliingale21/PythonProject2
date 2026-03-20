#1. Take input from user
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))

# a) Total number of items
print("Total items:", len(numbers))

# b) Last item
print("Last item:", numbers[-1])

# c) Reverse tuple
print("Reversed tuple:", numbers[::-1])

# d) Check if 5 exists
if 5 in numbers:
    print("Yes")
else:
    print("No")

# e) Remove first & last, sort remaining
new_tuple = numbers[1:-1]
sorted_tuple = tuple(sorted(new_tuple))
print("After removing first & last and sorting:", sorted_tuple)




#2. Input prices
prices = tuple(map(int, input("Enter prices of items: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Cheapest item
print("Cheapest item price:", min(prices))

# c) Costliest item
print("Costliest item price:", max(prices))

# d) Prices in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items
max_price = max(prices)
count = prices.count(max_price)
print("Number of costliest items sold:", count)