import sys


N = int(sys.stdin.readline())
have_List = list(map(int, sys.stdin.readline().split()))
have_List.sort()
M = int(sys.stdin.readline())
want_List = list(map(int, sys.stdin.readline().split()))


dic = dict()

for i in have_List:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


for i in range(M):
    if(want_List[i] in dic):
        print(dic[want_List[i]], end=' ')
    else:
        print('0', end=' ')
