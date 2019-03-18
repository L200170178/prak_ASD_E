class Matrix(list):
    def __init__(self,baris,kolom):
        self.baris=baris
        self.kolom=kolom
        self.data=[[0 for j in range(kolom)]for i in range(baris)]
    """def __int__(self,bariskolom):
        assert len(bariskolom)==2,"harus sama dengan 2"
        self.baris = bariskolom[0]
        self.kolom = bariskolom[1]
        self.data = [[0 for j in range(self.kolom)] for i in range(self.baris)]"""
    def __str__(self):
        a=""
        for i in range(0,self.baris):
            a+=(str(self[i])+"\n")
        return a
    def __getitem__(self, value):
        return self.data[value]
    def __setitem__(self, key, value):
        assert isinstance(value,list),"harus mengunakan list"
        assert len(value)==self.kolom,"kolom harus sama"
        for i in range (0,len(value)):
            assert isinstance(value[i],int),"semua harus integer"
        self.data[key]=value
    # 1
    def ukuran(self):
        return [self.baris,self.kolom]
    def __add__(self, other):
        assert isinstance(other, Matrix),"harus matrix"
        assert other.kolom==self.kolom,"kolom harus sama"
        assert other.baris == self.baris, "baris harus sama"
        hasil=Matrix(self.baris,self.kolom)
        for b in range(0,hasil.baris):
            for k in range(0,hasil.kolom):
                hasil[b][k]=self[b][k]+other[b][k]
        return hasil
    def __mul__(self, other):
        if isinstance(other,Matrix):
            assert self.kolom==other.baris,"baris terkali harus sama dengan pengali"
            hasil = Matrix(self.baris,other.kolom)
            for b in range(0, hasil.baris):
                for k in range(0, hasil.kolom):
                    for i in range(0,self.kolom):
                        hasil[b][k]+=(self[b][i]*other[i][k])
        elif isinstance(other,int):
            hasil = Matrix(self.baris,self.kolom)
            for b in range(0, hasil.baris):
                for k in range(0, hasil.kolom):
                    hasil[b][k]= self[b][k] * other
        return hasil
    def det(self):
        hasil=0
        for b in range(0,self.baris):
            tambah = 1
            kurang= 1
            for i in range(0,self.baris):
                tambah*=self[i][(i+b)%self.baris]
                kurang*=self[-i-1][(i+b)%self.baris]
            hasil+=tambah
            hasil-=kurang
        return hasil
    #2
    @staticmethod
    def zero(**kwargs):
        assert len(kwargs)<=2,"error out of range argument"
        if len(kwargs)==2:
            hasil=Matrix(kwargs[0],kwargs[1])
        elif len(kwargs)==1:
            hasil = Matrix(kwargs[0], kwargs[0])
        return hasil
    @staticmethod
    def identity(value):
        #assert self.baris==self.kolom,"baris dan kolom ini tidak sama"
        hasil=Matrix(value,value)
        for i in range(0,hasil.baris):
            hasil[i][i]=1
        return hasil
#3
class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def cari(self, dicari):
        curnode = self
        while curnode.data != dicari:
            curnode = curnode.next
        return curnode
    def kunjungi(self):
        curnode = self
        while curnode is not None:
            print(curnode.data)
            curnode = curnode.next
    def tambahdepan(self):
        return Node(0, self)
    def tambahbelakang(self):
        curnode = self
        while curnode.next != None:
            curnode = curnode.next
        curnode.next = Node(0)
    def tambah(self, posisi):
        if (posisi==0):
            return Node(0, self)
        else:
            curnode=self
            i=1
            while i < posisi:
                curnode = curnode.next
                i += 1
            inserted=Node(0,curnode.next)
            curnode.next = inserted
    def hapus(self,posisi):
        if (posisi==0):
            return self.next
        else:
            curnode=self
            i=1
            while i < (posisi-1):
                curnode = curnode.next
                i += 1
            deleted=curnode.next
            curnode.next=deleted.next
#4
class DNode(object):
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def cetakkedepan(mulai):
    current=soal
    while(current.prev!=None):
        print(current)
        current=current.next
def cetakkebelakang(mulai):
    current=soal
    while(current.prev!=None):
        print(current)
        current=current.prev
def tambahdepan(soal,penambah):
    current=soal
    while(current.prev!=None):
        current=current.prev
    current.prev=penambah
def tambahbelakang(soal,penambah):
    current=soal
    while(current.prev!=None):
        current=current.next
    current.next=penambah
a=Matrix(2,2)
a[0]=[3,5]
a[1]=[-1,6]
g=Matrix(4,4)
g[0]=[2,1,5,4]
g[1]=[2,3,2,5]
g[2]=[1,6,3,9]
g[3]=[7,3,2,5]
b=Matrix(2,2)
b[0]=[6,1]
b[1]=[1,9]
c=a+b
d=a*b
e=Matrix.identity(4)
f=Matrix.identity(3)
print(f.det())
print(b.det())
print(g.det())
print(c)
print(d)
print(e)
a=Node(10,Node(20,Node(30,Node(40,Node(50)))))
a.tambah(4)
#a=tambahdepan(a)
a.kunjungi()
