import  sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
if K >= N:
    print(0)
else:
    sensor  = list(map(int,  sys.stdin.readline().split()))
    
    sensor.sort()
    
    longs=[]
    for  i  in  range(N-1):
        longs.append(sensor[i+1]-sensor[i])
    
    longs.sort()
    for k in range(K-1):
        longs.pop()
    
    print(sum(longs))