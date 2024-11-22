from heapq import heappop, heappush, heapify
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] = [a[i], i]
a.sort()

ans = [[0,[]] for _ in range(m)]  # sum, arr[]
#print(a)
while a:
    level, idx = a.pop()
    #print(level)
    cur = 0 # idx
    val_a = 0
    val_b = 1 
    for i in range(m):
        tmp_a = b[i]*level  # 분자
        tmp_b = level+ans[i][0]  # 분모
        if val_a*tmp_b < tmp_a*val_b:
            val_a = tmp_a
            val_b = tmp_b
            cur = i
            #print(i)
    #print("cur",cur)
    ans[cur][0] += level
    ans[cur][1].append(idx+1)
for i in range(m):
    print(len(ans[i][1]), *ans[i][1])
    
    
    