

V = int(input())
L = list(input())

if(L.count('A')>L.count('B')):
    print('A')
elif(L.count('A')==L.count('B')):
    print('Tie')
else:
    print('B')