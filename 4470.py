import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    S = sys.stdin.readline().rstrip()
    print('%d. %s' % ((i+1), S))
