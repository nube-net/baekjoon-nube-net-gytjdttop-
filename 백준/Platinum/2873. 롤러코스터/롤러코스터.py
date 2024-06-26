import sys
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(r)]

val = 1001
R, C = 0, 0
if r%2 == 0 and c%2 == 0:
    for i in range(r):
        for j in range(c):
            if j%2^i%2:
                if arr[i][j] < val:
                    R, C = i, j
                    val = arr[i][j]

if r%2:
    for i in range(r):
        if i%2:
            print("L" * (c - 1) + "D", end="")
        else:
            if i == r-1:
                print("R" * (c - 1), end="")
            else:
                print("R"*(c-1)+"D", end="")
elif c%2:
    for i in range(c):
        if i%2:
            print("U" * (r - 1) + "R", end="")
        else:
            if i == c-1:
                print("D" * (r - 1), end="")
            else:
                print("D" * (r - 1) + "R", end="")
else:
    S = []
    if R%2:
        S = [R-1, R]
    else:
        S = [R, R+1]

    # top
    for i in range(S[0]):
        if i%2:
            print("L" * (c - 1) + "D", end="")
        else:
            print("R"*(c-1)+"D", end="")
    # mid
    flag = True
    for i in range(c):
        if flag:
            if i%2:
                if C== i:
                    if i == c-1:
                        if S[1] ==r-1:
                            continue
                        print("D", end="")
                    else:
                        print("R",end="")
                    flag = False
                    continue
                print("UR",end="")
            else:
                if C== i:
                    print("R",end="")
                    flag =False
                    continue
                print("DR",end="")
        else:
            if i%2 == 0:
                print("UR",end="")
            else:
                if i == c-1:
                    if S[1] == r-1:
                        print("D",end="")
                    else:
                        print("DD",end="")
                else:
                    print("DR",end="")
    # bottom
    for i in range(S[1]+1,r):
        if i%2:
            if i == r - 1:
                print("R" * (c - 1), end="")
            else:
                print("R" * (c - 1) + "D", end="")
        else:
            print("L"*(c-1)+"D", end="")