#1. List Creation
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

#2. Indexing
first_fruit = fruits[0]        # Access first element
last_fruit = fruits[-1]        # Access last element

print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)

#3. Slicing
middle_fruits = fruits[1:4]    # Elements from index 1 to 3
print("Middle fruits:", middle_fruits)

#4. List Methods
fruits.append("fig")           # Add item to end
fruits.insert(2, "grape")      # Insert at index 2
fruits.remove("banana")        # Remove by value
popped = fruits.pop()          # Remove last item and return it
fruits.sort()                  # Sort list alphabetically

print("Updated fruits:", fruits)
print("Popped fruit:", popped)

#5. List Comprehension — get fruit names with length > 5
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print("Long fruits:", long_fruits)

#6. Convert all fruits to uppercase using comprehension
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)
