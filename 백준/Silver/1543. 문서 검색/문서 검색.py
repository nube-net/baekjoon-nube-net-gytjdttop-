# kmp 알고리즘 학습용
import sys

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
    dx = len(pattern)-1
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]

        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                idx = i - len(pattern) + 1
                if indices:
                    if indices[-1]+dx < idx:
                        indices.append(idx)
                else:
                    indices.append(idx)
                j = table[j]
            else:
                j += 1

    return indices

# 입출력
text = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
result = kmp_search(text, pattern)

print(len(result))

