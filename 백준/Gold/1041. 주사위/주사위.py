import sys

n = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))  # 알파벳 위치 순서 대로 입력

plane = set(dice)  # 1칸짜리, n 3이상일 시 테두리 제외 공간
line = -1  # 2칸짜리,  n 3이상일 시 테두리 중간 공간
point = -1  # 3칸짜리, 꼭짓점

# line
tmp_l = 0
for i in range(6):
    for j in range(i+1, 6):
        if j == (5-i):
            continue
        else:
            if line == -1:
                line = dice[i]+dice[j]
                tmp_l = max(dice[i], dice[j])
            else:
                if line > dice[i]+dice[j]:
                    line = dice[i]+dice[j]
                    tmp_l = max(dice[i], dice[j])
                elif line == dice[i]+dice[j]:
                    tmp_l == max(tmp_l, dice[i], dice[j])


# point
tmp_p = 0
for i in range(6):
    for j in range(i+1,5):
        if j == (5-i):  # i j 반대편 위치 시 생략
            continue
        else:
            for k in range(j+1,6):
                if (k == (5-i)) or (k == (5-j)):
                    continue
                else:
                    if point == -1:
                        point = dice[i] + dice[j] + dice[k]
                        tmp_p = max(dice[i], dice[j], dice[k])
                    else:
                        if point > dice[i] + dice[j] + dice[k]:
                            point = dice[i] + dice[j] + dice[k]
                            tmp_p = max(dice[i], dice[j],dice[k])
                        elif point == dice[i] + dice[j] + dice[k]:
                            tmp_p == max(tmp_l, dice[i], dice[j], dice[k])


if n == 1:
    print(sum(dice)-max(plane))
elif n == 2:
    print(8*point-4*tmp_p)
else:
    print(5*((n-2)**2)*min(plane) +(8*point-4*tmp_p) + (12*(n-2)*line - 4*(n-2)*tmp_l))