import sys
inputF = sys.stdin.readline

# 백트래킹 공부 중
def code():
    if len(stack) == m:
        print(*stack)
        # stack.pop() 1번위치
        return  # 현재 코드 종료 -> 백트래킹(DFS)

    for num in nums:
        if num in stack:  # 숫자 중복 안됨
            continue
        else:
            stack.append(num)
            code()
            stack.pop()  # 2번 위치, 처음 제출 코드는 1번 위치 였으나 틀림.


n, m = map(int, inputF().split())
nums = list(map(int, inputF().split()))
nums.sort()
stack = []  # 스택

code()