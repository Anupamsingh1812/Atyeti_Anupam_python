
# 1. Arithmetic Operators
num1 = 15
num2 = 4

# Basic math operations
print("Addition:", num1 + num2)        # 15 + 4 = 19
print("Subtraction:", num1 - num2)     # 15 - 4 = 11
print("Multiplication:", num1 * num2)  # 15 * 4 = 60
print("Division:", num1 / num2)        # 15 / 4 = 3.75
print("Floor Division:", num1 // num2) # 15 // 4 = 3 (no decimals)
print("Modulus:", num1 % num2)         # 15 % 4 = 3 (remainder)
print("Exponent:", num1 ** num2)       # 15^4 = 50625

# 2. Assignment Operators

y = 8          # Start with 8

y += 5         # Add 5 , y = 13
y *= 2         # Multiply by 2 → y = 26
y -= 6         # Subtract 6 , y = 20
y //= 4        # Floor divide by 4 , y = 5

print("Final value of y:", y)  # Output: 5


# 3. Comparison Operators
a = 30
b = 25

# Compare values using logical tests
print("a == b:", a == b)       # False, because 30 ≠ 25
print("a != b:", a != b)       # True
print("a > b:", a > b)         # True, 30 > 25
print("a < b:", a < b)         # False
print("a >= 30:", a >= 30)     # True
print("b <= 25:", b <= 25)     # True

# 4. Logical Operators
logged_in = False
is_admin = True

# Logical operations between booleans
print("logged_in and is_admin:", logged_in and is_admin)  # False AND True = False
print("logged_in or is_admin:", logged_in or is_admin)    # False OR True = True
print("not is_admin:", not is_admin)                      # NOT True = False


# 5. Bitwise Operators
x = 12        # Binary: 1100
z = 5         # Binary: 0101

# Bitwise operations (work on binary digits)
print("AND:", x & z)           # 1100 & 0101 = 0100 (4)
print("OR:", x | z)            # 1100 | 0101 = 1101 (13)
print("XOR:", x ^ z)           # 1100 ^ 0101 = 1001 (9)
print("NOT x:", ~x)            # ~1100 = -13 (inverts all bits)
print("x << 2:", x << 2)       # Shift left by 2 bits: 110000 = 48
print("z >> 1:", z >> 1)       # Shift right by 1 bit: 0010 = 2
