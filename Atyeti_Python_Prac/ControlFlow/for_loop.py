# n = int(input("enter the number"))

# for i in range(1, 6):
#     for j in range(6 - i):
#         print(' ', end='') 
#     for k in range(i):
#         print('*', end='')  
#     print() 



# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=' ')
#     print('')


for i in range(1,6):
    for j in range(1,6):
        if i >= j:
            print('*',end='')
    print(' ')