a,b,c = map(int, input().split())

m = abs(a)+abs(b)

if m<=c and (c-m)%2 ==0:
    print("YES")
else:
    print("NO")