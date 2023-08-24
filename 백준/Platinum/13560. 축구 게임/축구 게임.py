import sys
input = sys.stdin.readline

n = int(input())
win = list(map(int, input().split()))
play = sum(win)  # 경기 횟수
if play != n*(n-1)//2:  # 경기 횟수 정상 체크
    print(-1)
else:
    k = False
    win.sort()
    for i in range(n-1, 0, -1):
        play -= win[i]
        if play < i*(i-1)//2:
            break

        if i == 1:
            k = True
    if k:
        print(1)
    else:
        print(-1)

'''
0 1 3 6 10 15 21

4
3 2 1 0

6
4 3 2 3 2 1


'''