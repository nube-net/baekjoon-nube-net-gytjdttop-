import sys
inputF = sys.stdin.readline

s = list(inputF().rstrip())
t = list(inputF().rstrip())
time = len(t) - len(s)
for _ in range(time):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()


if s == t:
    print(1)
else:
    print(0)