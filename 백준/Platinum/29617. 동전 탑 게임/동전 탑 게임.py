import sys
input = sys.stdin.readline
# 주의사항 승리조건은 보유동전개수가아님(?????)
a, b, k = list(map(int, input().split()))
if a == b: # 결과적으로 1개 1개 상황으로 유도해야 됨
    if k >= 0:
        print('Second')
    else:  # k < 0
        if a == 1:
            print('First')
        else:
            if k == -1:
                print('First')
            else:
                print('Second')
else:
    if k >= 0:  # 가장 많은 동전 먹고 K개, 만약 K개 값이 엄청 크거나 둘중 하나가 0이면 마찬가지로 1개 1개 상황 유도
        print('First')
    else:
        if a+b == 1:
            print('Second')
        else:
            print('First')
