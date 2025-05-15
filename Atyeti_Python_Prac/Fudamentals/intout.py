
# Ask the user to enter their name 
name = input("Enter your name: ")

# Ask for age and convert it to an integer
age = int(input("Enter your age: "))

# Ask for height and convert it to a float
height = float(input("Enter your height in meters: "))

# 2. Displaying output using print()

print("Hello", name)  # Using comma to separate values
print("You are", age, "years old")


# 3. Using formatted strings (f-strings)

# f-strings make it easy to embed variables directly in text
print(f"Nice to meet you, {name}!")
print(f"You are {age} years old and {height} meters tall.")

