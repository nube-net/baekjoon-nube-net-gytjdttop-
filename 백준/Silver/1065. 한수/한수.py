import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for i in range(1, n+1):
    tmp = str(i)
    if i < 100:
        ans += 1
    elif int(tmp[0]) - int(tmp[1]) == int(tmp[1]) - int(tmp[2]):
        ans += 1

print(ans)
