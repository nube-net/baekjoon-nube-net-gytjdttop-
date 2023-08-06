import sys
c=1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if not (l or p or v):
        break
    tmp=0
    tmp += l*(v//p) + min(l,v%p)
    print(f"Case {c}: {tmp}")
    c+=1