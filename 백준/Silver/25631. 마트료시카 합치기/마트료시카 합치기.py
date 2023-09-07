n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = [a[0]]
for i in range(1, n):
    l = len(ans)
    for j in range(l):
        if ans[j] < a[i]:
            ans[j] = a[i]
            break
        if j == l-1:
            ans.append(a[i])
print(len(ans))

