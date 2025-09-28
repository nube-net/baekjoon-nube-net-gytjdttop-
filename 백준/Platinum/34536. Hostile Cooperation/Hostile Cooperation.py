import sys
 
input = sys.stdin.readline
#스파게티코드 ㅇㅅㅇ
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
m, M = min(arr[2]), max(arr[2])
x = k-(m + M) / 2
arr[0].sort()
arr[1].sort()
ans = float('inf')
i, j = 0, n - 1
a, b = arr[0][0], arr[1][0]
while i < n and j >= 0:
    cur = arr[0][i] + arr[1][j]
    diff = abs(cur - x)
    
    if diff < ans:
        ans = diff
        a, b = arr[0][i], arr[1][j]
    elif diff == ans and (a+b > arr[0][i]+ arr[1][j]):
        ans = diff
        a, b = arr[0][i], arr[1][j]
    
    if cur < x:
        i += 1
    else:
        j -= 1
 
ans = []
tmp, tmp2 = 0, 0
if True:
    if abs(k - (arr[0][0] + arr[1][0] + M)) >= abs(k - (arr[0][0] + arr[1][0] + m)):
        ans.append([abs(k - (arr[0][0] + arr[1][0] + M)), arr[0][0] + arr[1][0] + M])
    else:
        ans.append([abs(k - (arr[0][0] + arr[1][0] + m)), arr[0][0] + arr[1][0] + m])
if True:
    if abs(k - (arr[0][-1] + arr[1][-1] + M)) >= abs(k - (arr[0][-1] + arr[1][-1] + m)):
        ans.append([abs(k - (arr[0][-1] + arr[1][-1] + M)), arr[0][-1] + arr[1][-1] + M])
    else:
        ans.append([abs(k - (arr[0][-1] + arr[1][-1] + m)), arr[0][-1] + arr[1][-1] + m])
 
if abs(a + b + m - k) >= abs(a + b + M - k):
    ans.append([abs(a + b + m - k), a + b + m])
else:
    ans.append([abs(a + b + M - k), a + b + M])
ans.sort()
print(abs(ans[0][1] - k))
