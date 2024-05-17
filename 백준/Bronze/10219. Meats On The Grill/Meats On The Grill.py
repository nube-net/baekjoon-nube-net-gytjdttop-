t =int(input())
for _ in range(t):
    r,c = map(int, input().split())
    arr = [input().rstrip() for _ in range(r)]
    for i in arr:
        print(i[::-1])