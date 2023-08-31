import sys
input = sys.stdin.readline

# 구해야 하는 것 : 플러그 '빼는' 횟수
n, k = map(int, input().split())
item = list(map(int, input().split()))

ans = 0
if n >= k:
    print(ans)
else:
    plug = set()
    idx = 0
    while len(plug) < n and idx < k:
        if item[idx] not in plug:
            plug.add(item[idx])
        idx += 1

    for i in range(idx, k):
        if item[i] in plug:
            continue
        else:
            cnt, x = -float('inf'), -float('inf')
            for j in plug:  
                if j in item[i:]:
                    c = item[i:].index(j)
                    if c > cnt:
                        cnt = c
                        x = j
                else:
                    x = j
                    break

            if x in plug:  
                plug.remove(x)
                plug.add(item[i])
                ans += 1

    print(ans)
