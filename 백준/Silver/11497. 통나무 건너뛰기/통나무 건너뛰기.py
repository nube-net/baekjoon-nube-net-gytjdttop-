import sys
inputF = sys.stdin.readline

T = int(inputF())

for _ in range(T):
    n = int(inputF())
    H = list(map(int, inputF().split()))
    H.sort()
    L = H.pop()
    R = L

    result = 0
    a = 0
    for i in range(len(H)):
        tmp = H.pop()
        if a == 0:
            result = max(result, L-tmp)
            L = tmp
            a = 1

        else:
            result = max(result, R - tmp)
            R = tmp
            a = 0
    result = max(result, abs(R-L))

    print(result)