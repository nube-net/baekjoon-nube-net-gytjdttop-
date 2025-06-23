import sys
input = sys.stdin.readline

u, v= map(int,input().split())
A = input().rstrip()
B = input().rstrip()
if u==v:
    if A < B:
        print("auq")
    elif A > B:
        print("ras")
    else:
        print("rasauq")
elif len(A) < 30:
    if int(A, u) < int(B, v):
        print("auq")
    elif int(A, u) > int(B, v):
        print("ras")
    else:
        print("rasauq")
else:
    if u < v:
        print("auq")
    elif u > v:
        print("ras")