import sys
input = sys.stdin.readline

n =int(input())
for _ in range(n):
    tmp = input()
    a = list(map(int, input().split()))
    arr = a[:3]
    arr.sort()
    ans = []
    total = sum(arr)-a[-1]
    for i in range(3,1,-1):
        tmp = total//i
        if tmp > arr[3-i]:
            ans.append(arr[3-i])
            total -= arr[3-i]
        else:
            ans.append(tmp)
            total -= tmp
    print(ans[0]*ans[1]*total)



