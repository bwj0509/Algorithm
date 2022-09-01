#N이 1일때부터 6까지 규칙파악
import sys

N = int(sys.stdin.readline())

if(N%2==0):
    print('SK')
else:
    print('CY')