import copy
import sys

L = []
index_L = []
sum = 0
for i in range(8):
    L.append(int(sys.stdin.readline()))

select_L = copy.deepcopy(L)
select_L.sort()
select_L.reverse()

for i in range(5):
    sum += select_L[i]
    index_L.append(L.index(select_L[i])+1)
index_L.sort()

print(sum)
for i in index_L:
    print(i, end=' ')
