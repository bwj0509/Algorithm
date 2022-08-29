import sys

N = list(map(str, sys.stdin.readline().rstrip()))

for i in range(len(N)):
    if(ord(N[i])>=65 and ord(N[i])<=90):
        N[i] = N[i].lower()
    else:
        N[i] = N[i].upper()
        
for i in N:
    print(i, end='') 