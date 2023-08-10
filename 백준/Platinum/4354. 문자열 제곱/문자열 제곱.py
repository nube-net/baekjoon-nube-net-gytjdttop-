import sys
inputF = sys.stdin.readline

# 반복패턴 길이 : 문자열 길이 - 파이배열 마지막값
def kmp_table(s):  # 실패 함수
    pi = [0] * len(s)  # table
    j = 0

    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]

        if s[i] == s[j]:
            j += 1
            pi[i] = j

    return pi


while True:
    s = inputF().rstrip()  # pattern
    if s == '.':
        break
    else:
        a=len(s)
        b = (len(s) - kmp_table(s)[-1])
        # 직전까지 나누어 떨어지지 않는 가능성, 생각하지 못함 => 패턴 없는 경우 ex) abcaabc 끝인덱스값이 3이지만 중간은 포함안되서 오류 
        if a%b != 0:  
            print(1)
        else:
            print(a//b)


