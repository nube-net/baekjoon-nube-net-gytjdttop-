import sys
inputF = sys.stdin.readline
case0 = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(inputF())
for o in range(T):
    M, N, K = map(int, inputF().split()) 

    Map = set() 
    stack = []  
    for i in range(K):
        x, y = map(int, inputF().split())
        Map.add((x, y))  
    result = 0
    while Map:
        stack.append(Map.pop()) 
        result += 1
        while stack:
            x, y = stack[-1]
            key = 0
            for p in case0:
                nx, ny = x + p[0], y + p[1]
                if (nx, ny) in Map:
                    stack.append((nx, ny))
                    Map.remove((nx, ny))
                    key = 1
            if key == 0:
                stack.pop()
    print(result)
