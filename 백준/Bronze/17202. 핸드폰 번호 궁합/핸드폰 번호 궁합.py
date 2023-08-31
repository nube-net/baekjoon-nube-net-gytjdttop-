import sys
input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())

s = []
for i in range(8):
    s.append(int(a[i]))
    s.append(int(b[i]))

for _ in range(14):
    tmp = []
    for i in range(len(s)-1):
        tmp.append((s[i]+s[i+1])%10)
    s = list(tmp)

print(s[0], end='')
print(s[1])