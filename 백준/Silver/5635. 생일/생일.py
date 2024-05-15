import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(str,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(1,4):
        arr[i][j] = int(arr[i][j])
arr.sort(key=lambda x: (x[3],x[2],x[1]))
print(arr[-1][0])
print(arr[0][0])
