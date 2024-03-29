import sys
input = sys.stdin.readline

def Shoelace_formula(n,x, y):
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += x[i] * y[j] - y[i] * x[j]

    return area
if True:
    x,y = [], []
    x2,y2 = [], []
    a,b,c,d = map(int,input().split())
    x.append(a)
    y.append(b)
    x.append(c)
    y.append(d)
    a,b,c,d = map(int,input().split())
    x2.append(a)
    y2.append(b)
    x2.append(c)
    y2.append(d)
    C1 = Shoelace_formula(3,x+[x2[0]],y+[y2[0]])*Shoelace_formula(3,x+[x2[1]],y+[y2[1]])
    C2 = Shoelace_formula(3,x2+[x[0]],y2+[y[0]])*Shoelace_formula(3,x2+[x[1]],y2+[y[1]])
#print(C1)
#print(C2)

if C1 <= 0 and C2 <= 0:
    k=False
    k2=False
    if max(x) >= min(x2) and max(x2) >= min(x):
        k =True
    if max(y) >= min(y2) and max(y2) >= min(y):
        k2 =True
    if k and k2:
        print(1)
    else:
        print(0)
else:
    print(0)
