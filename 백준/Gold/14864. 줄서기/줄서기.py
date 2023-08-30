import sys

n, m = map(int, sys.stdin.readline().split())
order = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# (자신보다 뒤에 있으면서~) -> 정렬문제로 바꾸고 카드번호를 인덱스라 가정하면 (앞에 자기보다 큰 숫자가 존재하는가?) 라는 의미로 됨
# 반대로 입력값 후자는 앞에 나보다 작은 숫자가 있는가?
result = [i for i in range(n+1)]
for x, y in order:
    result[x] += 1
    result[y] -= 1
result= result[1:]
Map = set()
for i in result:
    if i in Map:
        print(-1)
        exit()
    Map.add(i)
if len(Map) != n:
    print(-1)
else:
    print(*result)