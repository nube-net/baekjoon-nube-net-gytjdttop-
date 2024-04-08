s = input()

a = [0]*26
for i in s:
    a[ord(i)-ord("a")] +=1
print(*a)