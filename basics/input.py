c = int(input("Enter number of rows: "))

matrix = []

for i in range(c):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)
