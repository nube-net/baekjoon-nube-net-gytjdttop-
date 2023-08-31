import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        ans = 1
        tmp = 1
        mod = tmp%n
        if n % 2 == 0 or n % 5 == 0:
            print(-1)
        else:
            while mod != 0:
                ans += 1
                tmp = (tmp % n) * 10 + 1
                mod = tmp%n
            print(ans)
    except:
        break
