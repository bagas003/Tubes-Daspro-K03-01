# F06 - Mengubah Stok Game di Toko
def ubahstok():
    # Mengubah Stok Game di Toko
    # I.S. pengguna sudah login dan matriks data file game terdefinisi
    # F.S. stok item pada database berubah

    # KAMUS LOKAL
    # input_id : string
    # input_jumlah : int
    # isjumlahValid, found : boolean
    # i : int 
    # IX : int (Indeks dimana id ditemukan)

    # ALGORITMA
    # Mengecek apakah rolenya admin atau bukan
    if not isAdmin:
        print("Maaf, user tidak diizinkan untuk mengakses bagian ini.")
    else: # isAdmin = True
        input_id = input("Masukkan ID game: ")

        # Validasi input_jumlah
        isjumlahValid = False
        while not isjumlahValid:
            input_jumlah = int(input("Masukkan jumlah: ")) 
            if (input_jumlah == 0): # Asumsi jumlah yg diinput != 0
                print("Silahkan masukkan kembali angka yang benar ( min. 1 )")
            else:
                isjumlahValid = True
            
        found = False
        IX = -999
        if input_id[:4] == 'GAME':
            for i in range(1,len(game)):
                if game[i][0] == input_id:
                    found = True
                    IX = i
                    break
        
        if IX == -999:
            print("Tidak ada game dengan ID tersebut!")
        else: # IX != -999
            # Validasi stok game setelah pengubahan (tidak negatif)
            if ((game[IX][5] + input_jumlah) < 0):
                print("Stok game",game[IX][1],"gagal dikurangi karena stok kurang. Stok sekarang:",game[IX][5],"(<",str(abs(input_jumlah)) + ")")
            else: # (game[IX][5] + input_jumlah) >= 0
                game[IX][5] = game[IX][5] + input_jumlah
                if (input_jumlah < 0):
                    print("Stok game",game[IX][1],"berhasil dikurangi. Stok sekarang:",game[IX][5])
                elif (input_jumlah > 0):
                    print("Stok game",game[IX][1],"berhasil ditambahkan. Stok sekarang:",game[IX][5])

# PROGRAM UTAMA

# KAMUS GLOBAL
# type data_game : <id:string, nama: string; kategori: string; tahun_rilis: int; harga: float; stok: int>
# game : array of data_game
# isAdmin, isProgramValid : boolean
# menu : string 

# INISIALISASI
# Note : data dibawah ini hanya digunakan untuk mengetes jalannya program
# ketika nanti digabung, diabaikan saja.
game = [['id','nama','kategori','tahun_rilis','harga','stok'],
        ['GAME001','BNMO - Play Along With Crypto','Adventure',2022,100000,1],
        ['GAME002','Dasar Pemrograman','Coding',2022,0,10],
        ['GAME003','Python Gemink','Coding',1991,69000,999]]

# ALGORITMA
isProgramValid = True
# contohnya isAdmin merupakan variabel yang direturn dari fungsi login
isAdmin = True

while isProgramValid:
    menu = input()
    if menu == "ubah_stok":
        ubahstok()
    else:
        exit()


