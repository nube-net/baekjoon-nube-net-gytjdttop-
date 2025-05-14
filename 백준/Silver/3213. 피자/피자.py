import heapq
import sys
input = sys.stdin.readline

n =int(input())
a= [0,0,0]
for _ in range(n):
    tmp = input().rstrip()
    if tmp == "1/2":
        a[1] +=1
    elif tmp == "1/4":
        a[0] += 1
    else:
        a[2] +=1

ans = 0
if a[2]:
    a[0] -= min(a[0],a[2])
    ans += a[2]
ans += a[1]//2
ans += (a[0]+(a[1]%2))//4
if (a[0]+(a[1]%2))%4:
    ans +=1
print(ans)