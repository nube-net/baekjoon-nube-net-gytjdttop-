import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()
cur, cnt = 0, 0
while cur < len(p):
    cnt += 1
    tmp = []

    for start in range(len(s)):
        d=0
        key = 0
        for i in range(start,len(s)):
            if s[i] == p[cur+d]:
                d += 1
                key = 1
                if cur+d >= len(p):
                    break
                continue
            else:
                if key:
                    break
        tmp.append(d)
    cur += max(tmp)

print(cnt)


