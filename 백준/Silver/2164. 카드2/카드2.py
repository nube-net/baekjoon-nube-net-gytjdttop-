import sys
input= sys.stdin.readline

n = int(input())
cards = []
for i in range(n,0,-1 ) :
    cards.append(i)
tmp = 0
for k in range(n-2) :
    if len(cards)<=1 :
        break
    cards0=[]
    if len(cards)%2 == 0 :
        for o in range(0,len(cards),2):
            cards0.append(cards[o])
        cards=[]
        cards += cards0
    else :
        cards.pop()
        tmp = cards.pop()
        cards.insert(0,tmp)

print(cards[0])
