while(1):
    n = int(input())
    if(n== -1):
        break
    L = [1]
    for i in range(2,n):
        if(n%i==0):
            L.append(i)
            
    if(sum(L)==n):
        L = map(str, L)
        result = " + ".join(L)
        print(n,'=', result)
    else:
        print('%d is NOT perfect.'%n)   
    
    