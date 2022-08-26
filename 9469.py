import sys

P = int(sys.stdin.readline())

for i in range(P):
    N, D, A, B, F = map(float, sys.stdin.readline().split())

    result = D/(A+B) * F
    print('%d %.6f' % (i+1, result))
