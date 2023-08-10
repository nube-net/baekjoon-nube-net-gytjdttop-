import sys
# 최초 제출 시에는 너무 가볍게 파이 배열의 최대값을 출력해서 틀림.
# 하지만 광고 문자열은 양 끝으로 순회하기에 가장 마지막으로 확인된 접두사-접미사 길이를 기준으로 삼아야 옳음. 
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


n = int(sys.stdin.readline())
pattern = sys.stdin.readline().rstrip()

result = kmp_table(pattern)
print(n - result[-1])