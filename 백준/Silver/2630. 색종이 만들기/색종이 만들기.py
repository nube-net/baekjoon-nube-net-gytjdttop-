import sys
def code(paper):
    tmp = 3  # 아직 미탐색 상태

    # 탐색 과정(스캔)
    for i in paper:  # 첫번째 배열 추출
        if tmp == 4:  # 다른 색 존재 확인 시 탐색 중단
            break
        for k in range(len(i)):  # 각 배열 색깔 확인
            if tmp == 3:  # 시작 지점 색깔 저장
                tmp = i[k]
            else:
                if tmp == i[k]:  # 저장된 색과 동일할 시 계속
                    continue
                else:
                    tmp = 4  # 다른 색 존재
                    break

    # 탬색 종료 혹은 재탐색
    if tmp == 4:  # 색종이 4 분할
        L  = len(paper)//2

        tmp0 = []  # 1
        for p in paper[:L]:
            tmp0.append(p[:L])
        code(tmp0)

        tmp0 = []  # 2
        for p in paper[:L]:
            tmp0.append(p[L:])
        code(tmp0)

        tmp0 = []  # 3
        for p in paper[L:]:
            tmp0.append(p[:L])
        code(tmp0)

        tmp0 = []  # 4
        for p in paper[L:]:
            tmp0.append(p[L:])
        code(tmp0)
        return
    else:  # 색종이 개수 추가
        result[tmp] += 1
        return


n = int(sys.stdin.readline())
result = [0,0]  # 색종이 개수
paper_color = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 2차원 배열 형태로 저장

code(paper_color)

for x in result:
    print(x)

