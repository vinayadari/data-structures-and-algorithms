# def partition(nums,low,high):
#     pivot=nums[low]
#     i,j=low,high
#     while i<j:
#         while nums[i]<=pivot and i<=high-1:
#             i+=1
#         while nums[j]>pivot and j>=low+1:
#             j-=1
#         if i<j:
#             nums[i],nums[j]=nums[j],nums[i]
#     nums[low],nums[j]=nums[j],nums[low]
#     return j
# def quick_sort(nums,low,high):
#     if low<high:
#         p = partition(nums,low,high)
#         quick_sort(nums,low,p-1)
#         quick_sort(nums,p+1,high)
nums = [4,1,7,6,3,2,8]
# quick_sort(nums,0,len(nums)-1)
# print(nums)
## The most Pythonic ways way !
def quick_sort(nums):
    if len(nums)<=1: return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x<=pivot]
    right = [x for x in nums[1:] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
print(quick_sort(nums))
#one liner
#quick_sort = lambda nums: nums if len(nums) <= 1 else quick_sort([x for x in nums[1:] if x <= nums[0]]) + [nums[0]] + quick_sort([x for x in nums[1:] if x > nums[0]])

