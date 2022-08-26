x = []
y = []
x_result = 0
y_result = 0

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if(x.count(x[i]) == 1):
        x_result = x[i]
    if(y.count(y[i]) == 1):
        y_result = y[i]

print(x_result, y_result)
