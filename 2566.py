import sys

nine_by_nine = []
for i in range(9):
    L = list(sys.stdin.readline().split())
    nine_by_nine.append(L)
max = 0
X=0;Y=0

for i in range(9):
    for j in range(9):
        if(int(nine_by_nine[i][j])>=int(max)):
            max = nine_by_nine[i][j]
            X = i+1
            Y = j+1
            
print(max)
print(X, Y)