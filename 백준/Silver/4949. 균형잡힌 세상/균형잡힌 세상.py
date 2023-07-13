import sys
from collections import deque

input_func = sys.stdin.readline

# 괄호, 대괄호 카운팅(최종적으로 0, 중간에 음수되면 no 리턴)
small = 0
big = 0

while True:  # "." 인식시 컨티뉴
    word = input_func().rstrip()
    stack = []
    result = "yes"

    if word == ".":
        break

    for i in range(len(word)):
        a = word[i]

        if a == "(":
            stack.append(a)
        elif a == ")":
            if not stack or stack[-1] != "(":
                result = "no"
                break
            stack.pop()
        elif a == "[":
            stack.append(a)
        elif a == "]":
            if not stack or stack[-1] != "[":
                result = "no"
                break
            stack.pop()

    if stack:
        result = "no"

    print(result)
