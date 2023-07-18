import sys
dic = {}
result = ''
a = sys.stdin.readline().rstrip()

for i in range(len(a)):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1

key = False
count = 0
tmp = ''
tmp1= ''
for k in dic:
    if dic[k]%2 == 1:  # 홀수 카운트
        count += 1
        tmp1 = k
        tmp += (dic[k] // 2) * k
    else:  # 짝수 문자 저장
        tmp += (dic[k]//2)*k

    if count > 1:
        key = True
        break
tmp = ''.join(sorted(tmp))
result+=tmp
result+=tmp1
result+= ''.join(reversed(tmp))
if key:
    print("I'm Sorry Hansoo")
else:
    print(result)