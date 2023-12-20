# kmp 알고리즘 학습용
import sys
from itertools import permutations
def kmp_table(pattern):  # 실패 함수, 파이 배열
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

def kmp_search(text, pattern):
    table = kmp_table(pattern)
    indices = []  # 패턴이 텍스트에서 발견된 위치의 인덱스
    j = 0  # 패턴의 인덱스

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]

        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                indices.append(i - len(pattern) + 1)
                j = table[j]
            else:
                j += 1
    Tmp = 0
    for i in indices:
        if i < len(pattern):
            Tmp +=1
    return Tmp


# 입출력
n = int(sys.stdin.readline().rstrip())
S = []
ans = 0
for _ in range(n):
    S.append(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
P = list(permutations(S,n))
Set = set(P)
for i in P:
    pattern = "".join(i)
    text = pattern*2
    result = kmp_search(text, pattern)
    if result == k:
        ans +=1
print(ans)


