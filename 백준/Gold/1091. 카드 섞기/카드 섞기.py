import sys
inputF = sys.stdin.readline

n = int(inputF())
cards = [card for card in range(n)]  # 원본
p = list(map(int, inputF().split()))  # 최종 목적
s = list(map(int, inputF().split()))  # 셔플 공식
Map = set()  # 위치 저장
count = 0
tmp = list(cards)  # 더미
key = False
while True:
    if tuple(cards) in Map:  # 되돌아 왔을 시 탐색 중지
        count = -1
        break
    else:
        for j in range(n):
            if cards.index(j)%3 != p[j] :
                break
            if j == n-1:
                key = True
        if key:
            break
        Map.add(tuple(cards))
    for i in range(n):
        tmp[s[i]] = cards[i]
    count += 1
    cards = list(tmp)

print(count)