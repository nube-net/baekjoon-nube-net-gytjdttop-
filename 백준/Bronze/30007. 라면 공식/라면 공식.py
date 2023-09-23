import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    line = list(map(int, input().split()))
    print(line[0]*(line[2]-1) +line[1])
