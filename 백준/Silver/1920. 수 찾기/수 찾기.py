n1 = int(input())
set1 = set(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))

for num in list2:
    if num in set1:
        print(1)
    else:
        print(0)
