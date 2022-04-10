# F09 - Melihat Game yang dimiliki
def listgame():
    # menampilkan daftar game yang dimiliki pengguna ke layar
    # I.S. pengguna sudah login dan matriks data file game terdefinisi
    # F.S. database game tercetak ke layar

    # KAMUS LOKAL

    # ALGORITMA
    if len(game) == 1:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else: 
        print("Daftar game:")
        for i in range(1,len(game)):
            print('{:<6} | {:<29} | {:<9} | {:<4} | {:<6}'.format(*game[i]))

# referensi : https://www.semicolonworld.com/question/44245/python-format-output-string-right-alignment?msclkid=0e4d8a87b89911ecb9c76c8b7a60bae6

# PROGRAM UTAMA

# KAMUS GLOBAL
# type data_game : <id:string, nama: string; kategori: string; tahun_rilis: int; harga: float; stok: int>
# game : array of data_game
# isProgramValid : boolean
# menu : string 

# INISIALISASI
# Note : data dibawah ini hanya digunakan untuk mengetes jalannya program
# ketika nanti digabung, abaikan saja.
game = [['id','nama','kategori','tahun_rilis','harga','stok'],
        ['GAME001','BNMO - Play Along With Crypto','Adventure',2022,100000,1],
        ['GAME002','Dasar Pemrograman','Coding',2022,0,10],
        ['GAME003','Python Gemink','Coding',1991,69000,999]]

# ALGORITMA
isProgramValid = True
while isProgramValid:
    menu = input()
    if menu == "list_game":
        listgame()
    else:
        exit()
