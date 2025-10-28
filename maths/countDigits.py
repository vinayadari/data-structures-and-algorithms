from math import log10
# method 1
# needs logarithm
num = int(input("enter num:"))  
print(int(log10(num)+1))
# method 2
count = 0
while num:
    count += 1
    num //= 10
print(count)


