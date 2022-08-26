import sys

S = sys.stdin.readline().rstrip()
T_list = list(map(str, sys.stdin.readline().rstrip()))
result = []

while(len(T_list) != 1):
    if(T_list[-1] == 'A'):
        T_list.pop()
        a = ''
        for i in T_list:
            a += i
        result.append(a)

    elif(T_list[-1]) == 'B':
        T_list.pop()
        T_list.reverse()
        a = ''
        for i in T_list:
            a += i
        result.append(a)


cnt = 0
for i in result:
    if(i == S):
        cnt += 1

if(cnt >= 1):
    print('1')
else:
    print('0')
