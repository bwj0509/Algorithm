from itertools import count
import sys 
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    L = []
    for i in range(N):
        A, B = map(int, sys.stdin.readline().split())
        L.append([A, B])

    L.sort(key=lambda x:(x[1]))

    min = L[0][0]
    cnt = 1
    for i in range(1, N):
        if(L[i][0]<min):
            min = L[i][0]
            cnt +=1
            
    print(cnt)






