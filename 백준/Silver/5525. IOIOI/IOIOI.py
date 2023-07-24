import sys
inputF = sys.stdin.readline

n = int(inputF())  # O 개수
m = int(inputF())  # 문자열 길이
s = inputF().rstrip()  # 문자열

result = 0
st = True
c=0
for i in range(m):
    if st:
        if s[i] == 'I':
            st = False
            c = 1
    else:
        if s[i] == s[i-1]:
            st = True
            tmp = c//2
            if s[i] == 'O':
                tmp -= 1
            if tmp >= n:
                result += tmp - n + 1  ####
            if s[i] == 'I':
                st = False
                c =1
        else:
            c += 1
            if i == m-1:
                tmp = c // 2
                if s[i] == 'O':
                    tmp -= 1
                if tmp >= n:
                    result += tmp - n + 1  ####
print(result)