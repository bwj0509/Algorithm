t = int(input())


for i in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)

    for i in range(len(s)):
        for ii in range(r):
            print(s[i], end='')

    print('')
