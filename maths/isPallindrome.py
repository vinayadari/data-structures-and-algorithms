num = int(input())
n = num
res = 0
while num > 0:
    temp = num % 10
    res = res*10 + temp
    num //= 10
print(res == n)
 