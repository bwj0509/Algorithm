import sys

while(1):
    L = [0]*26
    S = sys.stdin.readline().rstrip()
    S = S.replace(' ', '')
    if(S == '*'):
        break
    S = list(map(str, S))

    for i in S:
        L[ord(i)-97] = 1

    if(sum(L) == len(L)):
        print('Y')
    else:
        print('N')
