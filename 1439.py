import sys
import math
L = list(map(int, sys.stdin.readline().rstrip()))
cnt = 0


for i in range(0,len(L)-1):
    if(L[i] != L[i+1]):
        cnt +=1
        
print(math.ceil(cnt/2))