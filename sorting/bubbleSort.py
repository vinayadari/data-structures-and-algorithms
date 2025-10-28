nums = [5, 7, 8, 4, 1, 6, 9, 2]
def buuble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
buuble_sort(nums)
print(nums)
