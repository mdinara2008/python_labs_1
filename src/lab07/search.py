def linear_search(nums, x):
    for i in range(len(nums)):
        if nums[i]==x:
            return i
    return -1
 
 
def binary_search(sorted_nums, x):
    lo = 0
    hi = len(sorted_nums) - 1
    while lo<=hi:
        mid = (lo+hi)//2
        val = sorted_nums[mid]

        if val==x:
            return mid
        elif x>val:
            lo = mid+1
        else:
            hi = mid-1
    return -1
 
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
 
 
def two_sum_fast(nums, target):
    seen = {}
    for i in range(len(nums)):
        current = nums[i]
        need = target - current

        if need in seen:
            return (seen[need], i)
        seen[current] = i

    return None 