import sys
a= set()
b=set()
n = int(sys.stdin.readline())
a = map(int,sys.stdin.readline().split())#a,b 각 원소는 100보다 작거나 같은 음이아닌정수(0<= a,b <=100)
b = map(int,sys.stdin.readline().split())
result = 0

a= sorted(a)
b= sorted(b)

for i in range(0,n) :
    result += int(a[i]*b[n-1-i])

print(result)
    
