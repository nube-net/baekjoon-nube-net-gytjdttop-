from collections import deque
import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
if n+1 < a+b:
    print(-1)
    exit()
if a >= b:
    A = [i for i in range(1, a + 1)]
    B = [i for i in range(1, b)]
    ans = [1 for _ in range(n - len(A) - len(B))] + A + B[::-1]
else:
    if a != 1:
        A = [i for i in range(1, a)]
        B = [i for i in range(1, b+1)]
        ans = [1 for _ in range(n - len(A) - len(B))]+A + B[::-1]
    else:
        B = [i for i in range(b,0,-1)]
        ans = [B[0]] + [1 for _ in range(n-len(B))] +B[1:]
print(*ans)