import sys
inputF = sys.stdin.readline

s = inputF().rstrip()

tmp = []
num = 0
for i in range(len(s)):
    if s[i] == 'X':
        num += 1
    else:
        if num > 0:
            tmp.append(num)
            num = 0
        tmp.append(0)
if num > 0:
    tmp.append(num)

result = ''
for i in tmp:
    if i == 0:
        result += '.'
    else:
        if i % 2 == 1:
            result = -1
            break
        else:
            while i > 0:
                if i >= 4:
                    i -= 4
                    result += 'AAAA'
                else:
                    result += 'BB'
                    i -= 2

print(result)