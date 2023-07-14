import sys
inputF = sys.stdin.readline

n, k = map(int, inputF().split())

trees = list(map(int, inputF().split()))
trees.sort()  # 최대 n 제곱
store = 0  # 나무 길이 합
tmp = 0
result = 0
for i in range(n):
    store += trees.pop()

    tmp = (store-k)/(i+1)

    if tmp > result:
        result = tmp



print(int(result))