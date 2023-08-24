import sys
input = sys.stdin.readline

n = int(input())
num = list(map(str, input().rstrip().split()))
num.sort(key=lambda x: x*10, reverse=True)
print(int(''.join(num)))