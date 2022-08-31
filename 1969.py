from optparse import check_choice
import sys

N, M = map(int, sys.stdin.readline().split())
L = []
Hamming_Distance = 0

for _ in range(N):
    L.append(sys.stdin.readline().rstrip())

for i in range(M):
    for j in range(N):
        check_list = []
        check_list.append(L[i][j])
        check_list = list(set(check_list))
        Hamming_Distance += len(check_list)
        
    
print(Hamming_Distance)
