import sys
from collections import deque
inputF = sys.stdin.readline

a, b, c = map(int, inputF().split())
Map = set()  # 탐색 완료 튜플 저장
Q = deque()  # 큐
Q.append((0,0,c))
result = set()

while Q:
    tmp = Q.popleft()
    if tmp in Map:
        continue
    else:
        Map.add(tmp)
        if tmp[0] == 0:
            result.add(tmp[2])
        if tmp[0] > 0:
            # A를 B에
            empty = b - tmp[1]  # 남은 용량
            if tmp[0] >= empty:
                Q.append((tmp[0] - empty, b, tmp[2]))
            else:
                Q.append((0, tmp[0] + tmp[1], tmp[2]))
            # A를 C에
            empty = c - tmp[2]  # 남은 용량
            if tmp[0] >= empty:
                Q.append((tmp[0] - empty, tmp[1], c))
            else:
                Q.append((0, tmp[1], tmp[2] + tmp[0]))

        if tmp[1] > 0:
            # B를 A에
            empty = a - tmp[0]  # 남은 용량
            if tmp[1] >= empty:
                Q.append((a, tmp[1] - empty, tmp[2]))
            else:
                Q.append((tmp[0] + tmp[1], 0, tmp[2]))
            # B를 C에
            empty = c - tmp[2]  # 남은 용량
            if tmp[1] >= empty:
                Q.append((tmp[0], tmp[1] - empty, c))
            else:
                Q.append((tmp[0], 0, tmp[2] + tmp[1]))

        if tmp[2] > 0:
            # C를 A에
            empty = a - tmp[0]
            if tmp[2] >= empty:
                Q.append((a, tmp[1], tmp[2] - empty))
            else:
                Q.append((tmp[0] + tmp[2], tmp[1], 0))

            # C를 B에
            empty = b - tmp[1]
            if tmp[2] >= empty:
                Q.append((tmp[0], b, tmp[2] - empty))
            else:
                Q.append((tmp[0], tmp[1] + tmp[2], 0))


print(*sorted(result))