import sys

n = sys.stdin.readline().rstrip()  # 문자열 형태 입력

# 세팅
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 각 숫자 나온 횟수, 출력값
all0 = [0, 9, 189,2889,38889,488889,5888889, 68888889, 788888889, 8888888889, 98888888889,1088888888889]  # 0
all9 = [1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000, 10000000000]  # 자연수 나온 횟수

for i in range(len(n)):
    a = int(n[i])
    if i != len(n)-1:  # 마지막 인덱스 에러 뜰것 같으니 따로 조건
        if a !=0:
            num[a] += (int(n[i + 1:]) + 1)
            for k in range(1,a):
                num[k] += all9[len(n)-i-2]*a + 10**(len(n)-i-1)
            for j in range(a,10):
                num[j] += all9[len(n)-i-2]*a
    else:
        for o in range(1, a+1):
            num[o] += 1

num[0]+= all0[len(n)-1]
for i in range(len(n)-1):
    b=(9-int(n[i])) * all9[len(n)-2-i]
    num[0]-=b
    if int(n[i]) ==0:
        num[0]-= (10**(len(n)-i-1)-1)-(int(n[i+1:]))

print(*num)