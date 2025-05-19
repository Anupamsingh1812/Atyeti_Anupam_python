#1. String Creation
text = "  Hello, Python World!  "

#2. Immutability — strings cannot be changed directly
# text[0] = "h"  This will raise an error

#3. Slicing
print("First 5 chars:", text[:5])       # '  Hel'
print("Last word:", text[-6:-1])        # 'World'

#4. String Methods
print("Lowercase:", text.lower())       # '  hello, python world!  '
print("Uppercase:", text.upper())       # '  HELLO, PYTHON WORLD!  '
print("Stripped:", text.strip())        # Removes leading/trailing spaces
print("Replaced:", text.replace("Python", "Java"))  # Replace word

#5. Splitting and Joining
words = text.strip().split(" ")         # Split by space
print("Words list:", words)
joined = "-".join(words)                # Join with "-"
print("Joined:", joined)

#6. Checking content
print("Starts with 'Hello'?", text.strip().startswith("Hello"))  # True
print("Contains 'World'?", "World" in text)                      # True
print("Length of string:", len(text))                            # Includes spaces

#7. String Formatting
name = "Alice"
lang = "Python"
print(f"{name} loves coding in {lang}!")  # f-string
