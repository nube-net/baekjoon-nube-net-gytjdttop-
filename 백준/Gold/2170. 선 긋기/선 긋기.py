import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
st, end = -float('inf'), -float('inf')
ans = 0
for x, y in lines:
    if x > end:
        if st != -float('inf'):
            ans += end-st
        st = x
        end = y
    else:
        if y > end:
            end = y
ans += end-st
print(ans)