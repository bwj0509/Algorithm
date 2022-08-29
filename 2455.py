import sys
L = []
for i in range(4):
    A, B = list(map(int,sys.stdin.readline().split()))
    if(i==0):
        L.append(B)
    else:
        L.append(L[i-1]-A+B)
print(max(L))