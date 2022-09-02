import sys
import math

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().rstrip().split()))

firstring = L[0]
bunmo = 0
bunja = 0

for i in range(1,len(L)):
    gcd = math.gcd(int(firstring), L[i])
    bunmo = firstring//gcd
    bunja = L[i] //gcd
    
    print('%d/%d'%(bunmo, bunja))