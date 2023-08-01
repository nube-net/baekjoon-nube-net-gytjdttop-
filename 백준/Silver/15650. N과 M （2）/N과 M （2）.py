import sys
inputF = sys.stdin.readline
n, m = map(int, inputF().split())

def code(arr, start, depth):
    if depth == m:
        print(*arr)
        return

    for i in range(start, n + 1):
        arr.append(i)
        code(arr, i + 1, depth + 1)
        arr.pop()

code([], 1, 0)
