import sys
N = int(sys.stdin.readline())

krain_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

boxweight_list = list(map(int, sys.stdin.readline().split()))


boxweight_list.sort(reverse=True)
krain_list.sort(reverse=True)

time = 0

if(max(boxweight_list)> max(krain_list)):
    time = -1
else:
    while(len(boxweight_list)>0):
        time +=1
        for i in range(len(krain_list)):
            for j in range(len(boxweight_list)):
                if(krain_list[i]>= boxweight_list[j]):
                    boxweight_list.pop(j)
                    break
print(time)
        