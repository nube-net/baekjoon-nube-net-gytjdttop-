import sys
input = sys.stdin.readline

n= int(input())
a= list(map(int,input().split()))
dic = [[] for _ in range(1000002)]
if n == 1:  # 계산 불필요
    print(a[0])
    exit()

for x in a:
    tmp = str(x)
    dic[x].append(tmp)

if dic[1]:
    while len(dic[1]) >= 2:  # 1 자체로는 곱에 무의미, 1을 다른 수에 더하면 그만큼 커짐. 3부터는 만들 수 있다면 두배로 더 커짐
        if len(dic[2]) >= 1:
            dic[1].pop()
            dic[3].append(dic[2].pop() + "+1")
        else:
            dic[1].pop()
            dic[1].pop()
            dic[2].append("1+1")
    if dic[1]:
        for i in range(2,1000002):
            if dic[i]:
                dic[1].pop()
                dic[i+1].append(dic[i].pop()+"+1")
                break
ans = []
for arr in dic:
    if arr:
        for s in arr:
            ans.append("("+s+")")
            ans.append("*")
if ans[-1]== "*":
    ans.pop()
print("".join(ans))