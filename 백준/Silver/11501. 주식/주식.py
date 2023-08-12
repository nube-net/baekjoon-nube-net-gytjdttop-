import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    point = list(map(int, input().split()))

    Max = point[-1]
    profit = 0

    for i in range(n-1, -1, -1):  
        if point[i] > Max:
            Max = point[i]
        else:
            profit += Max - point[i]

    print(profit)
