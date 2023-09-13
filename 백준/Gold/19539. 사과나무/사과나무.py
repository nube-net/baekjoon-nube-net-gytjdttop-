import sys

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
if sum(trees)%3 == 0:
    one = 0
    mod_two = 0
    for tree in trees:
        if tree == 1:
            one += 1
        else:
            mod_two += tree//2
            one += tree%2
    if one <= mod_two:
        print('YES')
    else:
        print('NO')

else:
    print('NO')