class Manusia(object):
    """ Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)
    def makan(self,s):
        print("Saya beru saja makan", s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

p1 = Manusia('Fatimah')
p1.ucapkanSalam()

class SiswaSMA():
    def __init__(self,nama,kelas):
        self.namaSiswa = nama
        self.kelas = kelas
    def ambilNama(self):
        return self.namaSiswa
    def ambilKelas(self):
        return self.kelas
    def gantiNama(self,nama):
        self.nama = nama
    def gantiKelas(self,kelas):
        self.kelas = kelas