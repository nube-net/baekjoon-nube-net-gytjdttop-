import sys
input = sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.insert(0, 0)
for i in range(1, n+1):
 l[i]=l[i]+l[i-1]
for _ in range(m):
 i,j=map(int,input().split())
 print(l[j]-l[i-1])