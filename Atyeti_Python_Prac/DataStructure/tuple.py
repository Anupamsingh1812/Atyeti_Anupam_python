#1. Tuple Creation
person = ("Alice", 30, "Engineer")

#2. Indexing
print("Name:", person[0])        # Alice
print("Age:", person[1])         # 30

#3. Slicing
print("Partial info:", person[1:])  # (30, 'Engineer')

#4. Tuple is immutable (this will raise an error if uncommented)
# person[1] = 31  # TypeError: 'tuple' object does not support item assignment

#5. Tuple unpacking
name, age, job = person
print(f"{name} is a {age}-year-old {job}.")

#6. Using tuple in a list (e.g., storing multiple records)
people = [
    ("Bob", 25),
    ("Charlie", 40),
    ("Diana", 35)
]

# Print each person's name and age
for name, age in people:
    print(f"{name} is {age} years old.")

#7. Tuples as keys in a dictionary (because they are hashable)
location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

print("Location for (40.7128, -74.0060):", location_data[(40.7128, -74.0060)])
