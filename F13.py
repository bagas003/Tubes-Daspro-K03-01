# F13 - Melihat Riwayat Pembelian
def riwayat():
    # menampilkan daftar riwayat pembelian game 
    # I.S. pengguna sudah login dan matriks data file riwayat terdefinisi
    # F.S. database riwayat pembelian game tercetak ke layar

    # KAMUS LOKAL

    # ALGORITMA
    if (len(history) == 1):
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        print("Daftar game:")
        for i in range(1,len(history)):
            print('{:<6} | {:<29} | {:<7} | {:<6}'.format(history[i][0],history[i][1],history[i][2],history[i][4]))

# referensi : https://www.semicolonworld.com/question/44245/python-format-output-string-right-alignment?msclkid=0e4d8a87b89911ecb9c76c8b7a60bae6

# PROGRAM UTAMA

# KAMUS GLOBAL
# type data_history : <game_id: string, nama: string, harga: int, user_id: string, tahun_beli: int>
# history : array of data_history
# isProgramValid : boolean
# menu : string

# INISIALISASI
# Note : data dibawah ini hanya digunakan untuk mengetes jalannya program
# ketika nanti digabung, abaikan saja.
history = [['game_id','nama','harga','user_id','tahun_beli'],
        ['GAME001','BNMO - Play Along With Crypto',100000,1,2022],
        ['GAME002','Python Gemink',100000,2,2001],
        ['GAME003','Hehehe',100000,3,2021]]

# ALGORITMA
isProgramValid = True
while isProgramValid:
    menu = input()
    if menu == "riwayat":
        riwayat()
    else:
        exit()