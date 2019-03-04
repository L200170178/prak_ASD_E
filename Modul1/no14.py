def formatRupiah(x):
    y = str(x)
    if len(y) <= 3:
        return 'Rp '+y
    else:
        a = y[-3:]
        b = y[:-3]
        return formatRupiah(b)+ "."+a
        print ('Rp ' + formatRupiah(b) +"."+a)

