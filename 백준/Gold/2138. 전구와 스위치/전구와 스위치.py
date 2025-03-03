import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, list(input().strip())))
b = list(map(int, list(input().strip())))

def code(a, z):
    x = a[:]  
    cnt = 0
    if z:  
        x[0] ^= 1
        x[1] ^= 1
        cnt += 1

    for i in range(1, n):
        if x[i - 1] != b[i - 1]:  
            cnt += 1
            x[i - 1] ^= 1
            x[i] ^= 1
            if i + 1 < n:
                x[i + 1] ^= 1

    return cnt if x == b else sys.maxsize

ans = min(code(a, 0), code(a, 1))

print(ans if ans != sys.maxsize else -1)
