class Mahasiswa(object):
    def __init__ (self,nim) :
        self.nim = nim

nim1= "L200170123"
nim2= "L200170124"
nim3= "L200170125"
nim4= "L200170126"
nim5= "L200170127"

Daftar = [nim1,nim2,nim3,nim4,nim5]


def quickSort(A):
    quickSortBantu(A,0,len(A) - 1)

def quickSortBantu(A,awal,akhir):
    if awal < akhir :
        titikBelah = partisi (A, awal, akhir)
        quickSortBantu(A,awal,titikBelah - 1)
        quickSortBantu(A,titikBelah + 1, akhir)

def partisi(A,awal,akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and \
              A[penandaKiri] <= nilaiPivot :
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and \
              penandaKanan >= penandaKiri :
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri :
            selesai = True
        else :
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

quickSort(Daftar)
print(Daftar)
