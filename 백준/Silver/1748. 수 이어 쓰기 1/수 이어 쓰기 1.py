import sys
input = sys.stdin.readline

n = input().strip()
ans = 0
l = len(n)
for i in range(1,l+1):
    if i == l:
        ans += i*(int(n)-10**(i - 1)) + i
    else:
        ans += i*(10**(i-1))*9

print(ans)