import sys
import math

A, B = map(int,(sys.stdin.readline().split(':')))
gcd_num = math.gcd(A,B)
A= int(A/gcd_num)
B= int(B/gcd_num)

print('%d:%d'%(int(A),int(B)))