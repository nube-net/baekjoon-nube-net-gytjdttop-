import sys
all9 = [(45 * (10 ** i)) * (i + 1) for i in range(-1,15)]
nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 46]


T = int(sys.stdin.readline())
for _ in range(T):
    a,b = map(str, sys.stdin.readline().split())

    result=0
    tmp = 0
    for i in range(len(a)):
        result+= int(a[i])
        if int(a[i]) != 0:
            if i == len(a)-1:
                tmp += nums[int(a[i])]
            else:
                tmp += int(a[i]) * (int(a[i + 1:]) + 1)
                tmp += int(a[i])*all9[len(a)-i-1]
                tmp += nums[int(a[i])-1]*(10**(len(a)-1-i))

    tmp1=0
    for i in range(len(b)):
        if int(b[i]) != 0:
            if i == len(b)-1:
                tmp1 += nums[int(b[i])]
            else:
                tmp1 += int(b[i]) * (int(b[i + 1:]) + 1)
                tmp1 += int(b[i])*all9[len(b)-i-1]
                tmp1 += nums[int(b[i])-1]*(10**(len(b)-1-i))
    result += tmp1 -tmp
    print(result)