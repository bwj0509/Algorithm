import sys

N = int(sys.stdin.readline())

L = []

for i in range(N):
    L.append(int(sys.stdin.readline()))

L.sort(reverse=True)

waitingNum= 1
tip = 0
sum_tip = 0

for i in range(len(L)):
    tip = L[i]-(waitingNum-1)
    if(tip>0):
        sum_tip += tip
    waitingNum +=1
        
print(sum_tip)

        
    