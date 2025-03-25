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
#print(table)
MAX = sys.maxsize
ans = [MAX,MAX]
for i in range(n):
    k = n-i
    p = i-table[i]
    
    if k+p < sum(ans):
        ans = [k-1,p+1]
        
print(*ans)
