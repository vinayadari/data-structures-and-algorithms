# a number is armstrong number is a number if the sum of cubes of indivisual digits
num = int(input("enter num:"))
n = num
sum = 0
while num > 0:
    temp = num % 10
    sum = sum + temp**3
    num = num//10

print(n == sum)
