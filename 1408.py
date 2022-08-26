import sys

H, M, S = map(int, sys.stdin.readline().split(':'))
H_2, M_2, S_2 = map(int, sys.stdin.readline().split(':'))

if(S_2-S < 0):
    M_2 -= 1
    S_2 = 60 + S_2 - S
else:
    S_2 -= S


if(M_2-M < 0):
    H_2 -= 1
    M_2 = 60+M_2-M
else:
    M_2 -= M

if(H_2-H < 0):
    H_2 = 24+H_2 - H
else:
    H_2 -= H

H_2 = str(H_2)
M_2 = str(M_2)
S_2 = str(S_2)

print('%s:%s:%s' % (H_2.zfill(2), M_2.zfill(2), S_2.zfill(2)))
