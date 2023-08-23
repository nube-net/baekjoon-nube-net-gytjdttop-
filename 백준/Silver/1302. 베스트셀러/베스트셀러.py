import sys
inputF = sys.stdin.readline

n = int(inputF())
dic = {}

for _ in range(n):
    s = inputF().rstrip()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

ans = ''
cnt = 0
for title in dic:
    if dic[title] < cnt:
        continue
    else:
        if dic[title] == cnt:
            ans = min(ans, title)
        else:
            ans = title
            cnt = dic[title]

print(ans)