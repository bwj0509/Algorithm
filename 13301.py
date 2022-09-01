import sys

N = int(sys.stdin.readline())

size_list = [4, 6]

for i in range(2, 81):
    size_list.append(size_list[i-1]+size_list[i-2])
    
print(size_list[N-1])