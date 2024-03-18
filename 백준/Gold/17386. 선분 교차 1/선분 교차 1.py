import sys
input = sys.stdin.readline
# 신발끈공식(area절댓값//2) = CCW 알고리즘(area 음수 시계방향)
# 선분교차판정 -> 두선분CCW값곱이 음수면 교차
def Shoelace_formula(n,x, y):
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += x[i] * y[j] - y[i] * x[j]

    return area

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
if Shoelace_formula(3,x+[x2[0]],y+[y2[0]])*Shoelace_formula(3,x+[x2[1]],y+[y2[1]]) < 0 and  Shoelace_formula(3,x2+[x[0]],y2+[y[0]])*Shoelace_formula(3,x2+[x[1]],y2+[y[1]]) < 0:
    print(1)
else:
    print(0)