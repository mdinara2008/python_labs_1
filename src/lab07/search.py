def linear_search(nums, x):
    """Возвращает индекс первого вхождения x в списке nums или -1, если элемент не найден."""
    for i in range(len(nums)):
        if nums[i]==x:
            return i
    return -1
 
 
def binary_search(sorted_nums, x):
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён."""
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
    """Находит индексы (i, j) двух элементов с суммой target полным перебором за O(n^2)."""
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
 
 
def two_sum_fast(nums, target):
    """Быстро находит индексы (i, j) двух элементов с суммой target за один проход со словарём за O(n)."""
    seen = {}
    for i in range(len(nums)):
        current = nums[i]
        need = target - current

        if need in seen:
            return (seen[need], i)
        seen[current] = i

    return None 