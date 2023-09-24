import sys
input = sys.stdin.readline


n = int(input())
s = input().strip()
a = s.count('S')
b = s.count('LL')
ans = a
if b:
    ans += b*2  -(b-1)
print(ans)