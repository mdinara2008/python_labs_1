N = int(input())
ochno = 0
zaochno = 0
for i in range(N):
    l_name, name, age, format = input().split()
    if format=='True':
        ochno+=1
    else:
        zaochno+=1
print(f'{ochno} {zaochno}')