import sys

N, want_num = map(int, (sys.stdin.readline().split()))
L = list(map(int, sys.stdin.readline().split()))
result = 0

for i in L:
    for j in L:
        for k in L:
            if(i != j and j != k and i != k):
                if(want_num-(i+j+k) >= 0):
                    if(result < i+j+k):
                        result = i+j+k

print(result)
