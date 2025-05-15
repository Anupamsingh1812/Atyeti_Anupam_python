# 1. Convert int to float
n = 10             # Integer value
f = float(n)       # Cast to float

print("Integer:", n)           # 10
print("Converted to float:", f)  # 10.0
print("Type:", type(f))      # <class 'float'>

# 2. Convert float to int

price = 19.99
price_int = int(price)  # Truncates decimal 

print("Float:", price)                # 19.99
print("Converted to int:", price_int)  # 19
print("Type:", type(price_int))       # <class 'int'>

# 3. Convert int to string

n = 100
s = str(n)

print("Integer:", n)             # 100
print("Converted to string:", s)  # "100"
print("Type:", type(s))      # <class 'str'>


# # 4. Convert float to string
pi = 3.14159
str_pi = str(pi)

print("Float:", pi)                   # 3.14159
print("Converted to string:", str_pi)  # "3.14159"
print("Type:", type(str_pi))         # <class 'str'>

# # 5. Convert string to int

num = "42"
num_int = int(num)

print("String:", num)            # "42"
print("Converted to int:", num)      # 42
print("Type:", type(num))            # <class 'int'>

# # 6. Convert string to float

price_str = "29.95"
price_float = float(price_str)

print("String:", price_str)          # "29.95"
print("Converted to float:", price_float)  # 29.95
print("Type:", type(price_float))    # <class 'float'>


# 7. Invalid conversion (will raise error)

invalid_str = "hello"
# num_invalid = int(invalid_str)  # This will cause ValueError
# print(num_invalid)

# Only numeric strings like "123" or "45.6" can be converted
