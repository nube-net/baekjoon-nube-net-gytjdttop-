import sys
input = sys.stdin.readline


def code(x, y, n):
    if n <= 3:
        for i in range(3):
            Map[x+i][y-i:y+i+1] = '*' * (2*i + 1)
        Map[x+1][y] = ' '
        return
    d = n // 2
    code(x, y, d)
    code(x+d, y-d, d)
    code(x+d, y+d, d)


n = int(input())
Map = [[' ' for _ in range(n*2)] for _ in range(n)]

code(0, n-1, n)

for i in Map:
    print(''.join(i))
