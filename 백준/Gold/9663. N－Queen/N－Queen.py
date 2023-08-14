import sys
inputF = sys.stdin.readline
# 처음에는 2차원 배열을 생각했었는데 스택만으로도 풀 수있을것 같았음

def dfs():
    if len(stack) == n:
        cnt[0] += 1
        return

    for i in range(n):
        if i in stack:
            continue
        else:
            k = False
            for j in range(len(stack)):
                if i == stack[j]-(len(stack)-j) or i == stack[j]+(len(stack)-j):
                    k = True
                    break
            if k:
                continue

            stack.append(i)

            dfs()

            stack.pop()


n = int(inputF())
stack = []
cnt = [0]
dfs()
print(*cnt)