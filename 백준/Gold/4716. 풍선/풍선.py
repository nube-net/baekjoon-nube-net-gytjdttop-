import sys

inputF = sys.stdin.readline

while True:
    n, a, b = map(int, inputF().split())
    if n + a + b == 0:
        break
    teams = []
    for _ in range(n):
        k, d_a, d_b = map(int, inputF().split())
        teams.append((k, d_a, d_b))

    teams.sort(key=lambda x: -abs(x[1] - x[2]))  # 풍선 개수에 제약이 있기에 손해 최소화

    result = 0
    for k, da, db in teams:
        if da <= db:  # A가 더 가까울 때
            if a >= k:
                a -= k
                result += k * da
            else:
                result += a * da
                k -= a
                a = 0
                b -= k
                result += k * db
        else:
            if b >= k:
                b -= k
                result += k * db
            else:
                result += b * db
                k -= b
                b = 0
                a -= k
                result += k * da

    print(result)

