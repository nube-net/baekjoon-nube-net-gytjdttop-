import sys
inputF = sys.stdin.readline

a, b = map(str, inputF().rstrip().split())

cnt = 50
for i in range(0, len(b)-len(a)+1):
    tmp = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            tmp += 1

    cnt = min(tmp, cnt)

print(cnt)