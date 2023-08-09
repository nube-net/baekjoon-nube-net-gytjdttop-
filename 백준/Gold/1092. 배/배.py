import sys
inputF = sys.stdin.readline

n = int(inputF())
machines = list(map(int, inputF().split()))
m = int(inputF())
boxes = list(map(int, inputF().split()))

machines.sort(key=lambda x: -x)  # 제한 큰 크레인 우선
boxes.sort(key=lambda x: -x)

key = False
cnt = 0
while boxes:
    for i in range(len(machines)):
        for box in boxes:
            if machines[i] >= box:
                boxes.remove(box)
                break
            else:
                if i == 0:
                    key = True
                    break
    if key:
        break
    cnt += 1

if cnt == 0:
    print(-1)
else:
    print(cnt)