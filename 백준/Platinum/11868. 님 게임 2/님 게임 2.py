import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if True:
    sumofxor = 0
    for x in arr:
        sumofxor = sumofxor ^ x
        
    if sumofxor == 0:
        print("cubelover")
    else:
        print("koosaga")

