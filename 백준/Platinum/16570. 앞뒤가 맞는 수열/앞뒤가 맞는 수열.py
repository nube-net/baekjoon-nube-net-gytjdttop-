import sys
input = sys.stdin.readline


def pi(pattern):
    length = len(pattern)
    table = [0] * length
    j = 0
    
    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j
    
    return table


n = int(input())
a = list(map(int,input().split()))
a.reverse()
table = pi(a)
x = max(table)
if x:
    print(x,table.count(x))
else:
    print(-1)
