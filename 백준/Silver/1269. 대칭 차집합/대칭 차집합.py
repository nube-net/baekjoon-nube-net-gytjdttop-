a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
aa = A-B
bb = B-A
aa.update(bb)
print(len(aa))