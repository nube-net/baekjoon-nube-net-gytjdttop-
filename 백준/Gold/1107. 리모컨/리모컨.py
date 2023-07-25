import sys
inputF = sys.stdin.readline

n = int(inputF())
m = int(inputF())
trash = set()
if m != 0:
    trash = set(map(int, inputF().split()))

result = abs(100-n)

for i in range(1000001):
    for j in range(len(str(i))):
        if int(str(i)[j]) in trash:
            break
        elif j == len(str(i))-1:
            result = min(result, len(str(i)) + abs(i-n))

print(result)



