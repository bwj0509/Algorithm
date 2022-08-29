import copy

S = list(input())
RE_S = copy.deepcopy(S)
RE_S.reverse()

if(S == RE_S):
    print('1')
else:
    print('0')