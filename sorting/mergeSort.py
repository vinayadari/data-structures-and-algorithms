def merge_sort(arr):
    if len(arr) <= 1: 
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]
nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]
print(merge_sort(nums))