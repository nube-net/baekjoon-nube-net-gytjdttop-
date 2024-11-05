import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = [[] for _ in range(1000002)]
if n == 1:
    print(a[0])
    exit()
for x in a:
    cnt[x].append((str(x)))

while cnt[1]:
    cnt[1].pop()
    if cnt[2]:
        cnt[3].append(cnt[2].pop()+"+1")
    elif cnt[1]:
        cnt[1].pop()
        cnt[2].append("1+1")
    else:
        for i in range(2, 1000002):
            if cnt[i]:
                cnt[i+1].append(cnt[i].pop()+"+1")
                break

ans = []
for arr in cnt:
    if arr:
        for s in arr:
            ans.append("("+s+")")
            ans.append("*")
if ans[-1]== "*":
    ans.pop()
print("".join(ans))
