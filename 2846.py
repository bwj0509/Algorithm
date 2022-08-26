import sys

N = int(sys.stdin.readline())
L = list(map(str, sys.stdin.readline().split()))

height_L = []
up_height = 0
active = 0
for i in range(N-1):
    if(int(L[i+1])-int(L[i]) > 0):
        active = 1
        up_height += int(L[i+1])-int(L[i])
    else:
        active = 0
        height_L.append(up_height)
        up_height = 0
height_L.append(up_height)
print(max(height_L))
