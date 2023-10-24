import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
a = [int(input()) for _ in range(k)]
st = 1
end = m
ans = 0
for i in a:
    x, y = st-i, i-end
    if x <= 0 and y <= 0:
        continue
    if x > 0:
        ans += x
        end -= x
        st = i
    else:
        ans += y
        st += y
        end = i
print(ans)