# Take input from the user 
n = int(input("Enter the number: "))

# First pattern: Right-aligned triangle of stars
for i in range(1, 6):
    for j in range(6 - i):         # Print spaces for right alignment
        print(' ', end='') 
    for k in range(i):             # Print stars
        print('*', end='')  
    print()                        # Move to next line after each row

# Second pattern: 5x5 square of stars
for i in range(1, 6):
    for j in range(1, 6):          # Print 5 stars in each row
        print("*", end=' ')
    print('')                      # Move to next line after each row

# Third pattern: Left-aligned triangle of stars
for i in range(1, 6):
    for j in range(1, 6):
        if i >= j:                 # Print star only if row number >= column number
            print('*', end='')
    print(' ')                     # Move to next line after each row
