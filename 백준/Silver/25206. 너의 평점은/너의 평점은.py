import sys
inputF = sys.stdin.readline

dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+': 1.5, 'D0':1.0, 'F':0}
sum_p = 0
sum_d = 0
for _ in range(20):
    z, x, y = map(str, inputF().split())
    if y != 'P':
        sum_p += float(x)*dic[y]
        sum_d += float(x)

print(sum_p/sum_d)
