from Modul2.LatOOP3 import *

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,kota):
        self.kotaTinggal = kota
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self,us):
        self.uangSaku = self.uangSaku + us

    listKuliah = []
    def ambilKuliah(self,matkul):
        self.listKuliah.append(matkul)
    def hapusKuliah(self,matkul):
        self.listKuliah.remove(matkul)

print('Masukkan nama:')
nama = input()
print('Masukkan nim:')
nim = input()
print('Masukkan kota:')
kota = input()
print('Masukkan uang saku:')
us = input()
us = int(us)
m1 = Mahasiswa(nama,nim,kota,us)
