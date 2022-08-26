import sys

L = []
cnt = []
for i in range(5):
    L.append(sys.stdin.readline().rstrip())

for i in range(5):
    if('FBI' in L[i]):
        cnt.append(i+1)

if(len(cnt) > 0):
    for i in cnt:
        print(i, end=' ')
else:
    print('HE GOT AWAY!')
