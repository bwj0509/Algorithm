import sys
import copy

while(1):
    S = int(sys.stdin.readline())
    if(S == 0):
        break
    S = list(str(S))

    S_re = copy.deepcopy(S)
    S_re.reverse()

    if(S == S_re):
        print('yes')
    else:
        print('no')
