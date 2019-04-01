class Manusia(object):
    """Class manusia dengan inisiasi 'nama'"""
    keadaan='lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapSalam(self):
        print("halo namaku: ", self.nama)
    def makan(self,s):
        print("saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olah(self,k):
        print('saya baru saja latihan', k)
        self.keadaan='lapar'
    def kali(self,n):
        return n*2
