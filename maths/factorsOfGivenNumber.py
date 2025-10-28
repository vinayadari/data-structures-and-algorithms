from math import sqrt
#brute force
n = int(input("enter n:"))
res = [i for i in range(1,n+1) if n%i==0]
# print(res) tc is O(n) and sc is O(K) k is total number of factors
#better solution 1
res1 = [i for i in range(1,n//2) if n%i==0]
res1.append(n)
#print(res1) tc is O(n) and sc is O(K) k is total number of factors
#better solution 2
res2 = []
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        res2.append(i)
        if n//i != i:
            res2.append(n//i)
# res2.sort()
    
        



