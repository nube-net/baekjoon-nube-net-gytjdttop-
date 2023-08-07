import sys
inputF = sys.stdin.readline

T = int(inputF())

for _ in range(T):  # 흰색 돌이 먼저 움직임
    S = inputF().rstrip()
    count = 0  # 이득 계산
    empty = 0  # 빈 공간
    result = 0
    for i in range(len(S)-1, -1, -1):  # 맨 뒤에서 부터 탐색, 앞부터 움직일 시 그 뒤에 공간이 생김
        rock = S[i]  # 현재 위치 상태

        # 경우의 수 2가지(+1)
        if rock == '.':  # 공간
            empty = 1
        else:  # 돌
            empty = 0
            if rock == 'B':
                if count > 0:
                    count = 0
                else:
                    count -= 1  # 흰 돌 기준
            elif rock == 'W':
                if count < 0:
                    count = 0
                else:
                    count += 1
        result += empty*count

    # 마무리
    if result > 0:  # 먼저 시작 이기에 이득이 1이상 이어야 함
        print('WHITE')
    else:
        print('BLACK')

