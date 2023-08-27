import sys
input = sys.stdin.readline

a, b = map(int, input().split())
tmp = [1] * (int(b ** 0.5) + 1)
tmp[0] = 0
tmp[1] = 0

for k in range(2, int(b ** 0.5) + 1):
    if tmp[k] == 1:
        for i in range(k * 2,int(b ** 0.5) + 1, k):
            tmp[i] = 0

cnt = 0
for i in range(len(tmp)):
    if tmp[i] == 1:
        n = 2
        while True:
            if i**n >= a:
                if i**n <= b:
                    cnt += 1
                else:
                    break
            n += 1
print(cnt)