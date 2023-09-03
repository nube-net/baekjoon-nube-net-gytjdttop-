import sys

n = int(sys.stdin.readline())
S = list(sys.stdin.readline().rstrip())

visited = set()
idx = 0
for _ in range((2**n)//2):
    print(''.join(S))
    visited.add(''.join(S))
    S = ['1' if x == '0' else '0' for x in S]
    print(''.join(S))
    visited.add(''.join(S))
    for i in range(n):
        tmp = S[i]
        for j in range(n):
            if j != i:
                if S[j] == '0':
                    S[j] = '1'
                else:
                    S[j] = '0'

        if ''.join(S) in visited:
            S[i] = tmp
            for j in range(n):
                if j != i:
                    if S[j] == '0':
                        S[j] = '1'
                    else:
                        S[j] = '0'
            continue
        else:
            break
