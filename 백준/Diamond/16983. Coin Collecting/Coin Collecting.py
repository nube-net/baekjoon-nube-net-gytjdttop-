import sys
input = sys.stdin.readline

n = int(input())
a = [[0, 0] for _ in range(n + 1)]


ans = 0
for _ in range(n*2):
    x, y = map(int, input().split())
    
    if y <= 1:
        dy = 0
        ans += abs(1-y)
    else:
        dy = 1
        ans += abs(2-y)
    
    if x < 1:
        dx = 1
    elif x <= n:
        dx = x
    else:
        dx = n
        
    ans += abs(x - dx)
    a[dx][dy] += 1

#print(a)
x, y = 0, 0
for i in range(1, n + 1):
    x += a[i][0] - 1
    y += a[i][1] - 1
    tmp = 0
    
    if x < 0 and y > 0:
        tmp = min(-x, y)
        x += tmp
        y -= tmp
        ans += tmp
    elif x > 0 and y < 0:
        tmp = min(x, -y)
        x -= tmp
        y += tmp
        ans += tmp
    
    ans += abs(x) + abs(y)

print(ans)






