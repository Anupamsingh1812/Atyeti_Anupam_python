#break pass continue


for i in range(5):
    if i == 2:
        pass  # does nothing, placeholder
        print("pass executed at i =", i)
    if i == 3:
        continue  # skips the rest of the loop for this iteration
    if i == 4:
        break  # exits the loop
    print("i =", i)