FreqMap = {}
nums = list(eval(input()))
for num in nums:
    FreqMap[num]=FreqMap.get(num,0)+1
print(FreqMap.items())


 
