import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = [1, 1, 2, 4]
    n = int(sys.stdin.readline())
    for i in range(4, 70):
        K.append(K[i-4]+K[i-3]+K[i-2]+K[i-1])
    print(K[n])