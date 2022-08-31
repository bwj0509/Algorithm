import sys
import statistics

N, M , B = map(int, sys.stdin.readline().split())
L=[]
for i in range(N):
    L += list(map(int, sys.stdin.readline().split()))
    
avg = round(statistics.mean(L))
time = 0

for i in L:
    if(i!=avg):
        if(avg-i>0):
            time += (avg-i)
            B -= (avg-i)
        else:
            time += abs((avg-i)*2)
            B += abs(avg-i)

print(time, avg, B)
            
    