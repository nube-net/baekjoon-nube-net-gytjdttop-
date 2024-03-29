import sys
input = sys.stdin.readline

n = int(input()) 
arr = list(map(int, input().split()))
cnt_arr = [0]*1003  # 개수 저장
S = set() # 종류 저장
for i in arr:
    cnt_arr[i] += 1
    S.add(i)
a = list(S)
a.sort()  # 종류 저장
ans = []  # 정답 출력용
for i in a:
    if cnt_arr[i]:
        if cnt_arr[i+1]:
            k = False
            for j in range(i+2,1001):
                if cnt_arr[j]:
                    while cnt_arr[i]:
                        cnt_arr[i] -= 1
                        ans.append(i)
                    cnt_arr[j] -= 1
                    ans.append(j)
                    k = True
                    break
            if k:
                continue
            while cnt_arr[i+1]:
                cnt_arr[i+1] -= 1
                ans.append(i+1)
            while cnt_arr[i]:
                cnt_arr[i] -= 1
                ans.append(i)
        else:
            while cnt_arr[i]:
                cnt_arr[i] -= 1
                ans.append(i)
print(*ans)