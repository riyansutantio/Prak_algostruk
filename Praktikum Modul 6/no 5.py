#5
class MhsTIF():
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.us = us

    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s

    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us

m0 = MhsTIF("Alfa", 76, "Banyuwangi", 249000)
m1 = MhsTIF("Pita", 53, "Purwokerto", 234000)
m2 = MhsTIF("Octa", 37, "Purworejo", 220000)
m3 = MhsTIF("Ila", 49, "Surakarta", 232000)
m4 = MhsTIF("Uni", 46, "Demak", 300000)
m5 = MhsTIF("Yeri", 31, "Cilacap", 250000)
m6 = MhsTIF("Tisa", 60, "Kutai", 245000)
m7 = MhsTIF("Roro", 91, "Lembang", 231000)
m8 = MhsTIF("Elvi", 15, "Bogor", 289000)
m9 = MhsTIF("Winda", 81, "Pontianak", 250000)
m10 = MhsTIF("Qina", 43, "Lombok", 550000)

daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

def cetak(A):
    for i in A:
        print (i)

def mergeSort2(A, awal, akhir):
    mid = (awal+akhir)//2
    if awal < akhir:
        mergeSort2(A, awal, mid)
        mergeSort2(A, mid+1, akhir)

    a, f, l = 0, awal, mid+1
    tmp = [None] * (akhir - awal + 1)
    while f <= mid and l <= akhir:
        if A[f].ambilUangSaku() < A[l].ambilUangSaku():
            tmp[a] = A[f]
            f += 1
        else:
            tmp[a] = A[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = A[f:mid+1]

    if l <= akhir:
        tmp[a:] = A[l:akhir+1]

    a = 0
    while awal <= akhir:
        A[awal] = tmp[a]
        awal += 1
        a += 1
        
def mergeSort(A):
    mergeSort2(A, 0, len(A)-1)
