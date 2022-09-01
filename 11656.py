import sys

S = sys.stdin.readline().rstrip()

L = []

while(len(S)!=0):
    L.append(S)
    S = S[1:]

L.sort()

for i in L:
    print(i)
        
    
