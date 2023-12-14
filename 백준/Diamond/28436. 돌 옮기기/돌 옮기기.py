import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    cnt = 0
    result = 0
    empty = False  

    for rock in reversed(S):
        if rock == '.': 
            empty = True
        else:
            empty = False
            if rock == 'B':
                if cnt >0:
                    cnt = 0
                else:
                    cnt -= 1
            else:
                if cnt < 0:
                    cnt = 0
                else:
                    cnt += 1
        if empty:
            result += cnt

    if result > 0:
        print('WHITE')
    else:
        print('BLACK')