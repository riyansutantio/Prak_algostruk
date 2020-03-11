class Pesan(object):
    """
        Sebuah class bernama pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, x):
        if x in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        konsonan = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
        a = 0
        for i in self.teks:
            if i in konsonan:
                a += len(i)
            else:
                a += 0
        return a
    def hitungVokal(self):
        vokal = 'euioaEUIOA'
        a = 0
        for i in self.teks:
            if i in vokal:
                a += len(i)
            else:
                a += 0
        return a