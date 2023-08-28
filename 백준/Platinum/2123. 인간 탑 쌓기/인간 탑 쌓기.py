import sys
inputF = sys.stdin.readline

n = int(inputF())
people = [list(map(int, inputF().split())) for _ in range(n)]
all_W = sum([w for w, p in people])
people.sort(key=lambda x: -(all_W - (x[0] + x[1])))

total = 0
ans = -float('inf')
for w, p in people:
    ans = max(ans, total - p)
    total += w
print(ans)