import sys
input = sys.stdin.readline
a, b = map(int, input().split())
x = abs(a - b)
print(-1 if x & 1 else f"{x.bit_length()-1} {(1 << (x.bit_length()-1)) - x//2}")
