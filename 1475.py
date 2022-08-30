import sys
import math

num_list = [0]*10
L = list(map(int, str(sys.stdin.readline().rstrip())))

for i in L:
    num_list[i] +=1

avg = math.ceil((num_list[6] + num_list[9])/2)
num_list[6], num_list[9] = avg,avg

print(max(num_list))


