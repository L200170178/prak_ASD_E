def prima(x,y):
    for i in range(2,1000,1):
        d=2
        while i%d != 0:
            if d == i-1:
                print(i)
            d = d+1
            
prima(2,1000)
