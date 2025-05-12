
# use while loop

n = int(input("Enter the number"))

r = 0
c=n
while n > 0:
    k = n % 10
    r = r * 10 + k
    n = n // 10

if r==c:
    print("palindrome")
else:
    print("not")