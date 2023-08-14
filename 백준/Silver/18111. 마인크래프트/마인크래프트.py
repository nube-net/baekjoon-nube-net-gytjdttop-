import sys
inputF = sys.stdin.readline

n, m, block = map(int, inputF().split())
world = [list(map(int, inputF().split())) for _ in range(n)]
time, high = 100000000, 0

for i in range(257):
    P = 0
    M = 0
    for x in range(n):
        for y in range(m):
            if world[x][y] > i:
                P += world[x][y] - i
            else:
                M += i - world[x][y]

    if M > P + block:
        continue
    else:    
        if P*2+M <= time:
            time = P*2 + M
            high = i

print(time, high)

