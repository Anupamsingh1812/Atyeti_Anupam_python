#if elif else

# Take the bill amount as input from the user and convert it to float
amount = float(input('Enter the Bill amount: '))

# Apply discount based on the bill amount range
if amount <= 1000:
    total = amount - amount * 0.10     # 10% discount for <= 1000
elif amount >= 1000 and amount < 5000:
    total = amount - amount * 0.15     # 15% discount for 1000–4999
elif amount >= 5000 and amount < 10000:
    total = amount - amount * 0.20     # 20% discount for 5000–9999
else:
    total = amount - amount * 0.25     # 25% discount for >= 10000

# Print the final amount to be paid after discount
print('Pay:', total)



