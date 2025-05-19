#1. Set Creation (duplicates are automatically removed)
fruits = {"apple", "banana", "cherry", "apple"}
print("Fruits set:", fruits)  # Output: {'apple', 'banana', 'cherry'}

#2. Adding elements
fruits.add("date")       # Add new element
fruits.add("apple")      # Duplicate; will not be added
print("After adding date and apple:", fruits)

#3. Removing elements
fruits.remove("banana")  # Removes 'banana'
# fruits.remove("kiwi")  #Error if element not found
fruits.discard("kiwi")   #No error if element not found
print("After removals:", fruits)

# 4. Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)          # {1, 2, 3, 4, 5, 6}
print("Intersection:", set1 & set2)   # {3, 4}
print("Difference:", set1 - set2)     # {1, 2}
print("Symmetric Difference:", set1 ^ set2)  # {1, 2, 5, 6}

#5. Checking membership
print("Is 'apple' in fruits?", "apple" in fruits)  # True

#6. Set comprehension — square of even numbers from 0 to 9
squares = {x**2 for x in range(10) if x % 2 == 0}
print("Even squares:", squares)
