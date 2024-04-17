import sys
input = sys.stdin.readline

n = int(input())
capitals = list(map(int, input().split()))*2
S = sum(capitals)//2

for i in range(1, n*2):
    capitals[i] += capitals[i - 1]

result = 0
for i in range(n):
    for j in range(n):
        tmp = capitals[j + i] - capitals[j]
        if tmp < 0:
            result += abs(tmp)//S
            if abs(tmp)%S != 0:
                result += 1
                
print(result)
