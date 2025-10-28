num = int(input("enter num:"))
while num:
    last_digit = num % 10
    print(last_digit)
    num = num//10
