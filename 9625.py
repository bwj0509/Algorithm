import sys

A_list = [1, 0, 1]
B_list = [0, 1, 1]

K = int(sys.stdin.readline())

for i in range(3,46):
    A_list.append(A_list[i-1] + A_list[i-2])
    B_list.append(B_list[i-1]+B_list[i-2])
print(A_list[K], B_list[K])
    