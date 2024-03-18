import sys
input = sys.stdin.readline
# 신발끈공식
# 딱히 좌표들의 정렬이 필요하진 않는다. 외적이용
def Shoelace_formula(n,x, y):
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += x[i] * y[j] - y[i] * x[j]

    return area

n = 3
x = []
y= []
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

ans = Shoelace_formula(n,x, y)
if ans < 0:
    print(-1)
elif ans > 0:
    print(1)
else:
    print(0)
