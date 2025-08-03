import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split()))[1] for _ in range(m)]

print(f"{sum(b)/n:.5f}")

