#1
class Mahasiswa:
    def __init__(self,nama,NIM,alamat,Usaku):
        self.nama = nama
        self.NIM = NIM
        self.alamat = alamat
        self.Usaku = Usaku

    def __repr__(self):
        return "Mahasiswa({},{},{},{})".format(self.nama,self.NIM,self.alamat,self.Usaku)
    
    def getNIM(self):
        return self.NIM
    def getNama(self):
        return self.nama
    def getAlamat(self):
        return self.alamat
    def getUsaku(self):
        return self.Usaku
    
c0  = Mahasiswa("Ika",10,"Sukoharjo",240000)
c1  = Mahasiswa("Budi",51,"Sragen",235000)
c2  = Mahasiswa("Ahmad",2,"Surakarta",250000)
c3  = Mahasiswa("Chandra",18,"Surakarta",235000)
c4  = Mahasiswa("Eka",4,"Boyolali",240000)
c5  = Mahasiswa("Fandi",31,"Salatiga",250000)
c6  = Mahasiswa("Deni",13,"Klaten",245000)
c7  = Mahasiswa("Galuh",5,"Wonogiri",245000)
c8  = Mahasiswa("Janto",23,"Klaten",245000)
c9  = Mahasiswa("Hasan",64,"Karanganyar",270000)
c10 = Mahasiswa("Khalid",29,"Porwodadi",265000)

daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def urutkan(List):
    for i in range (len(List) - 1) :
        for i in range (len(List) - 1) :
            if List[i].getNIM() > List[i+1].getNIM() :
               List[i],List[i+1] = List[i+1],List[i]
    return List
anu = urutkan(daftar)
print(*anu,sep='\n')

#2
arr1 = [1,5,7,9,12,14]
arr2 = [2,4,6,8,10,18,20]
def gabungkanList(list1,list2):
    hasil = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2) :
        if list1[i] < list2[j]:
            hasil.append(list1[i])
            i += 1
        else:
            hasil.append(list2[j])
            j += 1
    if i < len(list1) :
        hasil += list1[i:]
    else:
        hasil += list2[j:]
    return hasil

#3

def penggabungan(List1,List2):
    hasil = []
    i = 0
    j = 0
    while i < len(List1) and j < len(List2):
        if List1[i] < List2[j] :
            hasil.append(List1[i])
            i+=1
        else :
            hasil.append(List2[j])
            j+=1
    if i < len(List1):
        hasil += List1[i:]
    else :
        hasil += List2[j:]
    return hasil
x = penggabungan(arr1,arr2)
print(x)


def bubblesort(a):
    n = len(a)
    for i in range(n-1):
        for j in range (n-i-1):
            if a[j] > a[j+i]:
                swap(a,j,j+1)

                
def selectionsort(a):
    n = len(a)
    for i in range(n-1):
        indekkecil = cariposisiterkecil(a, i,n)
        if indekkecil != 1:
            swap(a,i,indekkecil)

            
def insertionsort(a):
    n = len(a)
    for i in range(1,n):
        nilai = a[i]
        pos = i
        while pos > 0 and nilai < a[pos-1]:
            a[pos] = a[pos-1]
            pos = pos-1
        a[pos] = nilai

from time import time
from random import shuffle
k=list(range(1,6001))
shuffle(k)
k1=k[:]
k2=k[:]
k3=k[:]
print("================= Sorting {} data =====================".format(len(k)))
aw=time();bubblesort   (k1) ;ak=time()  ;print("Bubble sort    : ",(ak-aw),"s")
aw=time();insertionsort(k2) ;ak=time()  ;print("Insertion sort : ",(ak-aw),"s")
aw=time();selectionsort(k3) ;ak=time()  ;print("Selection sort : ",(ak-aw),"s")

























    
