import sys
inputF = sys.stdin.readline

T = int(inputF())
for _ in range(T):
    n, m = map(int, inputF().split())
    tmp = [m, m-n, n]
    result = [1, 1, 1]
    for i in range(3):
        for j in range(1, tmp[i]+1):
            result[i] *= j

    print(result[0]//(result[1]*result[2]))