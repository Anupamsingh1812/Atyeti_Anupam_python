#Loop else clause: else clause after loops when no break occurs.
for i in range(6):
    print("Check i =", i)
    if i == 7:
        break
else:
    print("Loop completed without break")