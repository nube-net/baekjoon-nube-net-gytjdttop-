import sys
inputF = sys.stdin.readline

def code():
    if len(stack) == m:
        if not tuple(stack) in Map:
            print(*stack)
            Map.add(tuple(stack))
        return  # 현재 코드 종료 -> 백트래킹(DFS)

    for num in range(n):
        if stack:
            if stack[-1] > nums[num]:
                continue
        stack.append(nums[num])
        code()
        stack.pop()


n, m = map(int, inputF().split())
nums = list(map(int, inputF().split()))
nums.sort()
stack = []  # 스택
Map =set()
code()