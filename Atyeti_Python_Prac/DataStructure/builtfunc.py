# ✅ Sample data
numbers = [5, 10, 15, 20, 25]

#1. len() — Get the number of elements
print("Length:", len(numbers))  # Output: 5

#2. sum() — Total of all elements
print("Sum:", sum(numbers))     # Output: 75

#3. min() — Smallest value
print("Minimum:", min(numbers))  # Output: 5

#4. max() — Largest value
print("Maximum:", max(numbers))  # Output: 25

#5. sorted() — Returns a new sorted list (doesn’t modify original)
print("Sorted:", sorted(numbers, reverse=True))  # [25, 20, 15, 10, 5]

#6. type() — Returns the data type
print("Type of numbers:", type(numbers))  # <class 'list'>

#7. isinstance() — Check data type
print("Is numbers a list?", isinstance(numbers, list))  # True

#8. any() — True if at least one element is true
bools = [False, False, True]
print("Any true?:", any(bools))  # True

#9. range() — Create a sequence of numbers
print("Range list:", list(range(1, 6)))  # [1, 2, 3, 4, 5]
