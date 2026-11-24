def bubble_sort(nums):
    a = list(nums)
    n = len(a)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def insertion_sort(nums):
    a = list(nums)
    n = len(a)
    for i in range(1,n):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                a[j-1], a[j] = a[j], a[j-1]
            else:
                break
    return a
 
def selection_sort(nums):
    a = list(nums)
    n = len(a)
    for i in range(n-1):
        min1 = a[i]
        position = i
        for j in range(i+1,n):
            if min1>a[j]:
                min1 = a[j]
                position = j
        if position!=i:
            t = a[i]
            a[i] = a[position]
            a[position] = t
    return a   
