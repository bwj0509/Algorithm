import sys

cnt = 1
for i in range(int(sys.stdin.readline())):
    L = list(map(int, sys.stdin.readline().rstrip().split()))
    L.pop(0)
    L.sort()
    gap_list = []
    for i in range(len(L)-1):
        gap_list.append(L[i+1]-L[i])

    print('Class %d' % cnt)
    cnt += 1
    print('Max %d, Min %d, Largest gap %d' % (max(L), min(L), max(gap_list)))
