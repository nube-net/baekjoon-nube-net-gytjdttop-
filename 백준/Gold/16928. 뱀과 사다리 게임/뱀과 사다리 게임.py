import sys
inputF = sys.stdin.readline

# setting
n, m = map(int, inputF().split())
up = {}
for _ in range(n):  # 사다리(+) 수
    x, y = map(int, inputF().split())
    up[x] = y
down = {}
for _ in range(m):  # 뱀(-) 수
    x, y = map(int, inputF().split())
    down[x] = y

# BFS? DP?
Map = set([i for i in range(2,101)])  # 아직 안 가본 위치
Q = set()
Q.add(1)
count = 0
while 100 in Map: # 최종 위치에 도착 시 굴린 횟수 출력
    count += 1  # 주사위 굴림
    tmpQ = set()

    while Q:  # 현재 횟수 기준 출발할 수 있는 위치
        tmp = Q.pop()
        for i in range(1, 7):  # 주사위 1~6 숫자
            if tmp+i <= 100:
                if tmp+i in Map:  # 아직 안가본 곳이면
                    Map.remove(tmp+i)  # 경험 위치 체크
                    tmpQ.add(tmp+i)

                    if tmp+i in up:  # if 사다리
                        if tmp+i in tmpQ:
                            tmpQ.remove(tmp + i)
                        a = up[tmp+i]
                        if a in Map:
                            Map.remove(a)
                            tmpQ.add(a)
                    elif tmp+i in down:
                        if tmp + i in tmpQ:
                            tmpQ.remove(tmp + i)
                        a = down[tmp + i]
                        if a in Map:
                            Map.remove(a)
                            tmpQ.add(a)

    Q = set(tmpQ)

print(count)