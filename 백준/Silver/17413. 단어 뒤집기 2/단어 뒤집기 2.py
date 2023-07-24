import sys
inputF = sys.stdin.readline

s = inputF().rstrip()
a = ''
tmp = ''
k = False
for i in range(len(s)):

    if s[i] == '<':
        a += tmp[::-1]
        tmp = ''
        tmp += s[i]
        k = True
    elif s[i] == '>':
        tmp+= s[i]
        a += tmp
        tmp=''
        k=False
    else:
        if k:
            tmp+=s[i]
        else:
            if s[i] == ' ':
                a += tmp[::-1]
                a += s[i]
                tmp = ''
            else:
                tmp += s[i]
                if i == len(s)-1:
                    a += tmp[::-1]

print(a)