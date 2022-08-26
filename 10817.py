A, B, C, = input().split()
A = int(A)
B = int(B)
C = int(C)

L = list()
L.append(A)
L.append(B)
L.append(C)
L.sort()

print(L[1])
