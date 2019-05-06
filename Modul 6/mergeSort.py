class Mahasiswa(object):
    def __init__ (self,nim) :
        self.nim = nim

nim1= "L200170123"
nim2= "L200170124"
nim3= "L200170125"
nim4= "L200170126"
nim5= "L200170127"

Daftar = [nim1,nim2,nim3,nim4,nim5]


def mergeSort(A):
    if len(A) > 1 :
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0 ; j=0 ; k=0
        while i < len (separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j] :
                A[k] = separuhKiri[i]
                i = i + 1
            else :
                A[k] = separuhKanan[j]
                j = j + 1
            k = k + 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j+1
            k = k+1

mergeSort(Daftar)
print(Daftar)
