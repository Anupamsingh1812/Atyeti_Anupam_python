#Loop else clause: else clause after loops when no break occurs.

# Loop from 0 to 5
for i in range(6):
    print("Check i =", i)
    
    # If i becomes 7 (which never happens here), break the loop
    if i == 7:
        break

# This else block runs only if the loop completes without hitting break
else:
    print("Loop completed without break")
