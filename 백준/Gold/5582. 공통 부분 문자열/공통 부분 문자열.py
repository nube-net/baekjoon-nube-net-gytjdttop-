import sys
inputF = sys.stdin.readline

s1 = inputF().rstrip()
s2 = inputF().rstrip()

dp1 = [0] * len(s1)  # 처음에는 dp 테이블 사용했으나 메모리초과로 수정함.
dp2 = [0] * len(s1)

result = 0
for i in range(len(s2)):
    for k in range(len(s1)):
        if s2[i] == s1[k]:
            if i == 0 or k == 0:
                dp1[k] = 1
            else:
                dp1[k] = dp2[k-1] + 1
            result = max(result, dp1[k])
        else:
            dp1[k] = 0
    dp1, dp2 = dp2, dp1

print(result)
