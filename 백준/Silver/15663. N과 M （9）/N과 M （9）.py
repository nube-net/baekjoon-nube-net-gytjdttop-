import sys
inputF = sys.stdin.readline

# 백트래킹 공부 중
def code():
    if len(stack) == m:
        if not tuple(stack) in Map:
            print(*stack)
            Map.add(tuple(stack))
        return  # 현재 코드 종료 -> 백트래킹(DFS)

    for num in range(n):
        if num in Map1:  # 숫자 중복 안됨
            continue
        else:
            stack.append(nums[num])
            Map1.add(num)
            code()
            stack.pop()
            Map1.remove(num)


n, m = map(int, inputF().split())
nums = list(map(int, inputF().split()))
nums.sort()
stack = []  # 스택
Map =set()
Map1 = set()
code()