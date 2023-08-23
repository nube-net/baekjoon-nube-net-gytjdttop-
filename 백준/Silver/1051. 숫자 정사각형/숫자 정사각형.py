import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
end = min(n, m)
Map = [list(input()) for _ in range(n)]

ans = 1
for a in range(end):
    for i in range(n-a):
        for j in range(m-a):
            if Map[i][j] == Map[i][j+a] == Map[i+a][j] == Map[i+a][j+a]:
                ans = (a+1)**2
                break

print(ans)