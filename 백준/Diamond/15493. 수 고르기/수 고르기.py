import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
# if cur == a_i
# if cur + nxt >= a_i-1 + a_i+1 : choose cur +nxt
# nxt >= a_i-1 - a_i + a_i+1
hq = [(-a[i], i) for i in range(n)]
heapq.heapify(hq)

idx = [[(i - 1 + n) % n, (i + 1) % n] for i in range(n)]
visit = [False] * (2 * n)
value = list(a)
ptr = n
ans = 0
cnt = 0

while cnt < k:
    while True:
        val, i = heapq.heappop(hq)
        if visit[i] or visit[idx[i][0]] or visit[idx[i][1]]:
            continue
        break

    ans += -val
    cnt += 1

    l, r = idx[i]
    ll = idx[l][0]
    rr = idx[r][1]

    new_val = value[l] + value[r] - value[i]
    value.append(new_val)

    idx.append([ll, rr])
    new_i = ptr
    ptr += 1

    idx[ll][1] = new_i
    idx[rr][0] = new_i

    heapq.heappush(hq, (-new_val, new_i))

    visit[i] = True
    visit[l] = True
    visit[r] = True

print(ans)
