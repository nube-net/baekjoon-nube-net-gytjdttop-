import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    while n > 0:
        m = sys.maxsize
        min_index = 0
        for j in range(len(a)):
            if a[j] < m:
                min_index = j
                m = a[j]

        ans += min(min_index, n-min_index- 1)
        a.pop(min_index)
        n -= 1

    print(f"Case #{i+1}: {ans}")
