import sys
inputF = sys.stdin.readline

N, K = map(int, inputF().split())
people = []  # 사람 도착 시간
num = []  # 도착 시간 차

for i in range(N): # 사람 다수
    people.append(int(inputF()))

if people and len(people) > 1:
    for k in range(len(people)-1):
        num.append(people[k+1]-people[k])
num.sort()
result = 0
if N == 1:
    result = 1
elif K == 1:
    result = people[-1] - people[0] + 1
elif N == K:
    result = N
elif N > K:
    for o in range(K-1):
        num.pop()
    result = K + sum(num)
    
print(result)