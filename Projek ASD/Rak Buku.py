##Khairul Noviyanti (L200170178)
##Dewi Rahmawati (L200170188)

import mysql.connector


class Stack:

    #Contructor
    def __init__(self):
        #buat list 2D
        self.items = [[],[],[]]
       
    # Memeriksa apakah stack kosong
    def isEmpty(self,x):
        if len(self.items[x]) != 0:
            return True
        else:
            return False

        
    # Mengeluarkan data dari stack
    def keluar(self,x):
        return self.items[x].pop(-1)

    # Menambah data ke dalam stack
    def tambah(self, item, x):
        self.items[x].append(item)

    #Pencarian
    def lnrSch(self, target):
        n = len (self.target)
        for i in range (n):
            if self.target[i] == target:
                return True
            return False
        
    # Menampilkan objek terakhir dari stack
    def tampilatas(self):
        print("Buku Terakhir pada Rak Komputer")
        print("    Buku "+self.items[0][len(self.items[0])-1])
        print("Buku Terakhir pada Rak Matematika")
        print("    Buku "+self.items[1][len(self.items[1])-1])
        print("Buku Terakhir pada Rak Sejarah")
        print("    Buku "+self.items[2][len(self.items[2])-1])
    
    # Mehitung panjang stack
    def size(self):
        print("Jumlah Buku pada Rak Komputer")
        print("    "+str(len(self.items[0]))+" Buku")
        print("Jumlah Buku pada Rak Matematika")
        print("    "+str(len(self.items[1]))+" Buku")
        print("Jumlah Buku pada Rak Sejarah")
        print("    "+str(len(self.items[2]))+" Buku")


    #mengurutkan
    def bubbleSort(self, x):
        
        n = len(self.items[x])
        for i in range(n):
            for j in range(0, n-i-1):
                if self.items[x][j] > self.items[x][j+1] :
                    self.items[x][j], self.items[x][j+1] = self.items[x][j+1], self.items[x][j]

                    
    # Menu dari aplikasi
    def mainmenu(self):


        #=====================================masukkan database ke list===========================#
        cnx = mysql.connector.connect(user='root', password='',database='rakbuku')
        cursor = cnx.cursor()
        query = ("select nomor,nama from komputer")
        cursor.execute(query)
        for nomor,nama in cursor:
            self.items[0].append(nama)

        cursor = cnx.cursor()
        query = ("select nomor,nama from matematika")
        cursor.execute(query)
        for nomor,nama in cursor:
            self.items[1].append(nama) 

        cursor = cnx.cursor()
        query = ("select nomor,nama from sejarah")
        cursor.execute(query)
        for nomor,nama in cursor:
            self.items[2].append(nama) 
        #==========================================================================================#

            
        while True:
            print(" ")
            print("|  Cari Buku  |")
            print("=========================")
            print("1. Cek Rak Buku")
            print("2. Hapus isi Buku Dari Akhir")
            print("3. Tambah buku")
            print("4. Menampilkan Buku Terakhir ")
            print("5. Jumlah Buku")
            print("6. Pencarian Buku ")
            print("7. Tampilkan Buku secara Urut")
            print("8. Keluar")
            print("=========================")
            
            pilihan=str(input(("Silakan masukan pilihan anda: ")))



            #=====================================menambahkan buku===========================#
            if(pilihan=="3"):
                print("1. Rak Komputer")
                print("2. Rak Matematika")
                print("3. Rak Sejarah")
                x = input("Pilih rak yang akan ditambah ")

                
                if x=="1":
                    #=============menambahkan isi list============================#
                    obj = str(input("Masukan judul buku yang ingin anda tambahkan: "))
                    self.tambah(obj,int(x)-1)
                    print("Buku "+obj+" telah ditambahkan")
                    print()
                    #==============menambahkan isi database=======================#                        
                    cursor = cnx.cursor()
                    query = ("insert into komputer (nama) values('{}')".format(obj))
                    cursor.execute(query)
                    cnx.commit()
                        
                elif x=="2":
                    #=============menambahkan isi list============================#
                    obj = str(input("Masukan judul buku yang ingin anda tambahkan: "))
                    self.tambah(obj,int(x)-1)
                    print("Buku "+obj+" telah ditambahkan")
                    print()
                    #==============menambahkan isi database=======================#                        
                    cursor = cnx.cursor()
                    query = ("insert into matematika (nama) values('{}')".format(obj))
                    cursor.execute(query)
                    cnx.commit()
                        
                elif x=="3":
                    #=============menambahkan isi list============================#
                    obj = str(input("Masukan judul buku yang ingin anda tambahkan: "))
                    self.tambah(obj,int(x)-1)
                    print("Buku "+obj+" telah ditambahkan")
                    print()
                    #==============menambahkan isi database=======================#                        
                    cursor = cnx.cursor()
                    query = ("insert into sejarah (nama) values('{}')".format(obj))
                    cursor.execute(query)
                    cnx.commit()
            #================================================================================#

                    
            #=====================================hapus buku=================================#
            elif(pilihan=="2"):
                print("1. Rak Komputer")
                print("2. Rak Matematika")
                print("3. Rak Sejarah")
                x = input("Pilih rak yang akan dihapus ")
                
                if x=="1":
                    if self.isEmpty(int(x)-1) == True :
                        #==============hapus database=======================#                        
                        cursor = cnx.cursor()
                        a = len(self.items[int(x)-1]) - 1
                        query = ("delete from komputer where nama = '{}'".format(self.items[int(x)-1][a]))
                        cursor.execute(query)
                        cnx.commit()

                        #=============hapus list============================#
                        print("Buku "+self.items[int(x)-1][a]+" dihapus")
                        self.keluar(int(x)-1)
                        print()
                    else :
                        print("raknya udah kosong, tidak bisa diambil lagi")

                        
                elif x=="2":
                    if self.isEmpty(int(x)-1) == True :
                        #==============hapus database=======================#
                        cursor = cnx.cursor()
                        a = len(self.items[int(x)-1]) - 1
                        query = ("delete from matematika where nama = '{}'".format(self.items[int(x)-1][a]))
                        cursor.execute(query)
                        cnx.commit()
                        
                        #=============hapus list============================#
                        print("Buku "+self.items[int(x)-1][a]+" dihapus")
                        self.keluar(int(x)-1)
                        print()
                    else :
                        print("raknya udah kosong, tidak bisa diambil lagi")

                        
                elif x=="3":
                    if self.isEmpty(int(x)-1) == True :
                        #==============hapus database=======================#
                        cursor = cnx.cursor()
                        a = len(self.items[int(x)-1]) - 1
                        query = ("delete from sejarah where nama = '{}'".format(self.items[int(x)-1][a]))
                        cursor.execute(query)
                        cnx.commit()
                        
                        #=============hapus list============================#                       
                        print("Buku "+self.items[int(x)-1][a]+" dihapus")
                        self.keluar(int(x)-1)
                        print()
                    else :
                        print("raknya udah kosong, tidak bisa diambil lagi")
            #================================================================================#


            #=====================================menampilkan isi list=======================#
            elif(pilihan=="1"):
                for i in range(len(self.items)):
                    if i==0:
                        print("Rak Komputer")
                    elif i==1:
                        print("Rak Matematika")
                    elif i==2:
                        print("Rak Sejarah")
                    for j in range(len(self.items[i])):
                        print("    "+self.items[i][j])
                    print()
                print()
            #================================================================================#
                

            #======================menampilkan list yang terakhir============================#
            elif(pilihan=="4"):
                self.tampilatas()
                print()
            #================================================================================#


            #======================menampilkan jumlah buku===================================# 
            elif(pilihan=="5"):
                self.size()
                print()
            #================================================================================#


            #======================cari buku=================================================# 
            elif(pilihan=="6"):
                obj = str(input("Masukkan Buku yang anda cari : "))
                n = len(self.items)
                buku = []
                rak = []
                
                for i in range(len(self.items)):
                    for j in range(len(self.items[i])):
                        if obj.lower() in self.items[i][j].lower():
                            buku.append(self.items[i][j])
                            if i == 0:
                                rak.append("Rak Komputer")
                            elif i == 1:
                                rak.append("Rak Matematika")
                            elif i == 2:
                                rak.append("Rak Sejarah")
                if len(buku)==0:
                    print("buku tidak ada")
                else:
                    print("Buku ada di rak")
                    for i in range(len(buku)):
                        print("Kata Kunci "+obj+", Buku "+buku[i]+" ada di "+rak[i])
            #================================================================================#

                        
            #======================mengurutkan buku==========================================#
            elif(pilihan=="7"):
                self.bubbleSort(0)
                self.bubbleSort(1)
                self.bubbleSort(2)
                for i in range(len(self.items)):
                    if i==0:
                        print("Rak Komputer")
                    elif i==1:
                        print("Rak Matematika")
                    elif i==2:
                        print("Rak Sejarah")
                    for j in range(len(self.items[i])):
                        print("    "+self.items[i][j])
                    print()
                print()
            #================================================================================#


            #======================keluar====================================================#
            elif(pilihan=="8"):
                return False
            #================================================================================#


            #======================jika input salah==========================================#
            else:
                print("input salah")
            #================================================================================#



 
if __name__ == "__main__":
    s=Stack()
    s.mainmenu()
