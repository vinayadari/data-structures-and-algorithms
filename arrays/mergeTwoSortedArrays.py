def merge_array(left,right):
    i, j = 0, 0
    res = []
    n, m = len(left), len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            res.append(left[i])
            i += 1
            print(res)
        else:
            res.append(right[j])
            j += 1
            print(res)
        
    while i<n:
        res.append(left[i])
        i += 1
        print(res)  
        
    while j<m:
        res.append(right[j])
        j += 1
        print(res)
    return res
left = [1, 2, 3]
right = [2, 5, 6]
print(merge_array(left, right))