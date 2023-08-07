import sys
inputF = sys.stdin.readline

n = inputF().rstrip()
m = "".join(reversed(n))

if n == m:
    print(1)
else:
    print(0)