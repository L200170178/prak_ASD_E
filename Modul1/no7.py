def faktorPrima(x):
    faktor = []
    a = 2
    while a <= x:
        if x% a ==0:
            x/=a
            faktor.append(a)
        else:
            a+=1
    return faktor


