
import sys

N, L = map(int, sys.stdin.readline().split())
location_list = list(map(int, sys.stdin.readline().rstrip().split()))
location_list.sort()

start = location_list[0]
count = 1

for i in location_list[1:]:
    if(i in range(start, start+L)):
        continue
    else:
        start = i
        count += 1
print(count)
    