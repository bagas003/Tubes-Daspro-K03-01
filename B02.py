# B02 - Magic Conch Shell aka Kerang Ajaib
import time

def kerangajaib():
    # Menerima masukan dari user lalu mengemberikan respon acak
    # Menggunakan algoritma Linear Congruential Generator untuk mendapatkan angka acak
    # I.S. menerima masukan pengguna
    # F.S. memberikan respon acak

    # KAMUS
    # function lcg() -> int
    # x, m, a, c, i : int
    # respon : array of string

    # Realisasi Fungsi
    def lcg():
        # algoritma Linear Congruential Generator
        # memiliki rumus X(n+1) = (a*X(n) + c) % m dengan X sebagai seed angka yang didapat dari time.time()
        m = 2**32; a = 53; c = 69
        x = int(time.time())

        for i in range(10):
            x = (a*x + c) % m
        
        return x % 10
    
    # ALGORITMA UTAMA
    respon = ['gatau','iya kyknya','gk','adadeh','wow','same...','iyh', 'mlz','boring bgt lu','terserah']

    input('\nKerangAjaib: apa?\nLu         : ')
    print('KerangAjaib: '+ respon[lcg()])
