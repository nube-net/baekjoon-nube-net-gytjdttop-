import sys
input = sys.stdin.readline
def find(a):
    if S[a] != a:
        S[a] = find(S[a])
    return S[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    S[root_a] = root_b


n, m, k = map(int, input().split())
S = [i for i in range(m)]
minsu = list(map(int, input().split()))
chulsu = list(map(int, input().split()))
minsu.sort()
#print(minsu)
for card in chulsu:
    #print(S)
    st, end = 0, m - 1
    ans = 0
    while True:
        if st > end:
            break
        mid = (st + end) // 2

        if minsu[mid] <= card:
            st = mid + 1
        else:
            end = mid - 1
    #print(st)
    ans = find(st)
    print(minsu[ans])
    if find(S[ans])!= m-1:
        union(S[ans],S[ans]+1)
    #print(S)
    #print()