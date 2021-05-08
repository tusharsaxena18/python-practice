import random

start=int(input("Enter the first number: "))
end=int(input("Enter the second number: "))
range =int(input("Enter the range: "))
n = 0
while n < range:
    y=random.randint(start,end)
    print(y)
    k=random.randint(start,end)
    n+=1
    