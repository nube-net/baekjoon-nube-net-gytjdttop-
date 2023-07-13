import sys

n = int(sys.stdin.readline())
w = [int(sys.stdin.readline().strip()) for _ in range(n)]
result=0
w.sort()

for i in w :
    if result < n*i:
        result = n*i
    n-=1

print(result)
    

