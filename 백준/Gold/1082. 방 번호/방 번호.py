import sys
input = sys.stdin.readline


n = int(input())
cost = list(enumerate(map(int, input().split())))
a = list(cost)  # 정렬 전 상태 저장
m = int(input())
cost.sort(key = lambda x: (x[1],-x[0]))
if n == 1:
    print(0)
    exit()
# print(cost)
ans = []
ans_c = []
x = -1
# 1
if cost[0][0] == 0:
    x = cost[1][1]
    if x <= m:
        ans = [cost[1][0]]
        ans_c = [cost[1][1]]
        m -= x
else:
    x = cost[0][1]
    if x <= m:
        ans = [cost[0][0]]
        ans_c = [cost[0][1]]
        m -= x

# 2~
if 1:
    x = cost[0][1]
    ans += [cost[0][0]] * (m // x)
    ans_c += [cost[0][1]]* (m // x)
m %= x
#print(ans)
#print(m)
if ans[0] == 0:
    print(0)
    exit()

for i in range(len(ans)):
    if m == 0:
        break
    for j in range(n-1,-1,-1):
        if a[j][1]-ans_c[i] <= m:
            ans[i] = j
            m -= a[j][1]-ans_c[i]
            break
#print(ans)
#print(m)

for i in range(len(ans)):
    ans[i] = str(ans[i])
print(''.join(ans))