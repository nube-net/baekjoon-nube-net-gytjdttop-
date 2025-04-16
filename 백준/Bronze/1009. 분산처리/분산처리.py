import sys
inputF = sys.stdin.readline

T = int(inputF())

for _ in range(T):
    a, b = map(int, inputF().split())
    r=1
    for i in range(b):
        r*= a
        r%=10
        
    result = r%10
    if result == 0:
        result =10
    print(result)
