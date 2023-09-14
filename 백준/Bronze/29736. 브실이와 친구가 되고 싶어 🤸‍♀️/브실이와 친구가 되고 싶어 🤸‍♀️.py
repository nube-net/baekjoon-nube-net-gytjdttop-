a, b = map(int, input().split())
k, x = map(int, input().split())
ans = min(b,k+x)-max(a,k-x)+1
if ans >0:
    print(ans)
else:
    print('IMPOSSIBLE')