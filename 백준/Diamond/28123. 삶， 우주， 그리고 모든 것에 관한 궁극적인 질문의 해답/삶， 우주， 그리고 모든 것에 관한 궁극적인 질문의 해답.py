import sys
input = sys.stdin.readline
n, k, x = map(int, input().split())
arr =[0,0,-1,-1,-1,-2,-2,-2,-2,-2]
if n==1:
    print(0)
elif 4<= x <=9:
    print(n%k + n//k +arr[x])
    
else:
    if n >=24:
        print(n%k + n//k +arr[x])
        exit()
    ans = 0
    tmp = 1
    for i in range(n):
        tmp *= 2
        if str(tmp)[0] == "4":
            ans += 1
    print(ans)