import sys

m, n = map(int, sys.stdin.readline().split())

place = [sys.stdin.readline().rstrip() for _ in range(m)]
person = set()
wall = set()
count = 0
s=0
for aa in place:
    for k in range(n):
        if aa[k] == 'I':
            start = (s, k)
        elif aa[k] == 'X':
            wall.add(n*s+k)
        elif aa[k] == 'P':
            person.add(n*s+k)
    s += 1


Map = set([i for i in range(m*n)])  # 탐색 미완료 지역
QQ = []  # 큐
QQ.append(start)
Map.remove(n*start[0]+start[1])
while QQ and person: # 탐색 가능한 공간이 남아 있고 동시에 만날 사람이 존재할 경우
    Q = []

    while QQ:
        x, y = QQ.pop()

        # up
        if x != 0:
            a = x-1
            b = n*a+y
            if b in Map:
                Map.remove(b)
                if b in wall:
                    z=1
                else:
                    if b in person:
                        count += 1
                        person.remove(b)
                    Q.append((a,y))

        # down
        if x != m-1:
            a = x + 1
            b = n * a + y
            if b in Map:
                Map.remove(b)
                if b in wall:
                    z=1
                else:
                    if b in person:
                        count += 1
                        person.remove(b)
                    Q.append((a, y))

        # left
        if y != 0:
            a = y-1
            b = n*x+a
            if b in Map:
                Map.remove(b)
                if b in wall:
                    z=1
                else:
                    if b in person:
                        count += 1
                        person.remove(b)
                    Q.append((x,a))

        # left
        if y != n-1:
            a = y+1
            b = n*x+a
            if b in Map:
                Map.remove(b)
                if b in wall:
                    z=1
                else:
                    if b in person:
                        count += 1
                        person.remove(b)
                    Q.append((x,a))
    QQ = list(Q)
if count:
    print(count)
else:
    print('TT')