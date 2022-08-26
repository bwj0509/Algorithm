import sys

M = int(sys.stdin.readline())
locate = 1

for i in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    if(X == locate):
        locate = Y
    elif(Y == locate):
        locate = X

print(locate)
