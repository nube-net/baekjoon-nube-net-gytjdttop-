import sys
from collections import deque
inputF = sys.stdin.readline

T = int(inputF())

for _ in range(T):
    # 입력
    n = int(inputF())
    a = deque(map(int, inputF().split()))
    b = deque(map(int, inputF().split()))

    # dp
    dp_a = deque()  # 최대 2개 씩 관리
    dp_b = deque()

    for i in range(n):
        if i == 0:
            dp_a.append(a.popleft())
            dp_b.append(b.popleft())
        elif i == 1:
            dp_a.append(a.popleft() + dp_b[0])
            dp_b.append(b.popleft() + dp_a[0])
        else :
            dp_a.append(a.popleft() + max(dp_b[0], dp_b[1], dp_a[0]))
            dp_b.append(b.popleft() + max(dp_a[0], dp_a[1], dp_b[0]))

            dp_a.popleft()
            dp_b.popleft()
            
    print(max(max(dp_a),max(dp_b)))
