# 1. Dictionary Creation
person = {
    "name": "Alice",
    "age": 30,
    "profession": "Engineer"
}

# 2. Accessing values using keys
print("Name:", person["name"])        # Alice
print("Age:", person.get("age"))      # 30

#3. Adding and updating values
person["city"] = "New York"           # Add new key-value pair
person["age"] = 31                    # Update existing value
print("Updated person:", person)

#4. Removing elements
person.pop("profession")              # Removes key 'profession'
# person.pop("salary") → KeyError
person.pop("salary", None)            # Safe removal
print("After removal:", person)

#5. Looping through dictionary
for key, value in person.items():
    print(f"{key} => {value}")

#6. Dictionary keys, values, and items
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

#7. Dictionary comprehension — squares of numbers
squares = {x: x**2 for x in range(5)}
print("Squares:", squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
