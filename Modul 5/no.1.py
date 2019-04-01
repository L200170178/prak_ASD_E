from b import Mahasiswa
import sys
ms1=Mahasiswa('aaa',420,'Solo',420000)
ms2=Mahasiswa('bbb',318,'Solo',420000)
ms3=Mahasiswa('ccc',732,'Solo',420000)
ms4=Mahasiswa('ddd',910,'Solo',420000)
ms5=Mahasiswa('eee',120,'Solo',420000)
ms6=Mahasiswa('fff',190,'Solo',420000)
ms7=Mahasiswa('ggg',107,'Solo',420000)
ms8=Mahasiswa('hhh',820,'Solo',420000)
ms9=Mahasiswa('iii',290,'Solo',420000)
ms10=Mahasiswa('jjj',624,'Solo',420000)


mhss = [ms1,ms2,ms3,ms4,ms5,ms6,ms7,ms8,ms9,ms10]

def urutkan(A):
    baru = {}
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key=lambda x: x[1])
    for elem in listofTuples :
        print(elem[0] , ":" , elem[1] )


urutkan(mhss)
