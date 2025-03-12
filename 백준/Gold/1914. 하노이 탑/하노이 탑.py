import sys
input = sys.stdin.readline


def aaa(n, st, end):
    if n == 1:
        print(st, end)
        return
    
    aaa(n-1, st, 6 - st- end)
    print(st, end)
    aaa(n - 1, 6 - st - end, end)

n = int(input())
print(2**n-1)
if n>20:
    exit()
aaa(n, 1, 3)