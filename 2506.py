import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
count = 1
score = 0

if(L[0]==1):
    score +=1

for i in range(1,N):
    if(L[i]==1 and L[i-1]==1):
        count += 1
        score += count
    elif(L[i]==1):
        score +=1
    elif(L[i]==0):
        count = 1

print(score)