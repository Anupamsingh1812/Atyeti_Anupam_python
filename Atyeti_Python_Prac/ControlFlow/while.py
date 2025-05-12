
# use while loop

# Take an integer input from the user
n = int(input("Enter the number: "))

r = 0           # Variable to store the reversed number
c = n           # Store original number for comparison

# Reverse the number using a while loop
while n > 0:
    k = n % 10           # Get the last digit
    r = r * 10 + k       # Append the digit to the reversed number
    n = n // 10          # Remove the last digit from the original number

# Check if the reversed number is equal to the original
if r == c:
    print("palindrome")  # It's a palindrome
else:
    print("not")         # It's not a palindrome
