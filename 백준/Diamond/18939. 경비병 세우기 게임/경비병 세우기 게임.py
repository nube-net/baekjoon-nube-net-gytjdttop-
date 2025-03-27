import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())

    if m < k*2:
        print("Yuto")
    else:
        if n%2 and m%2:
            print("Yuto")
        else:
            print("Platina")
