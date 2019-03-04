def itung(x):
    vocal='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    aa=0
    for i in x:
        if i in vocal:
            aa+=1
    return(len(x),aa)
print(itung('Surakarta'))
