import sys

S = sys.stdin.readline().rstrip()
S = S.replace('c=', '@')
S = S.replace('c-', '@')
S = S.replace('dz=', '@')
S = S.replace('d-', '@')
S = S.replace('lj', '@')
S = S.replace('nj', '@')
S = S.replace('s=', '@')
S = S.replace('z=', '@')
print(len(S))
