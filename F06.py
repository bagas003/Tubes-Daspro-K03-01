# F06 - Mengubah Stok Game di Toko
def ubahstok(data_game):
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
    input_id = input("Masukkan ID game: ")

    # Validasi input_jumlah
    isjumlahValid = False
    while not isjumlahValid:
        input_jumlah = int(input("Masukkan jumlah: ")) 
        if (input_jumlah == 0): # Asumsi jumlah yg diinput != 0
            print ("Silahkan masukkan kembali angka yang benar ( min. 1 )")
        else:
            isjumlahValid = True
            
    found = False
    IX = -999
    if input_id[:4] == 'GAME':
        for i in range(1,len(data_game)):
            if data_game[i][0] == input_id:
                found = True
                IX = i
                break
        
    if IX == -999:
        print ("Tidak ada game dengan ID tersebut!")
    else: # IX != -999
        # Validasi stok game setelah pengubahan (tidak negatif)
        if ((data_game[IX][5] + input_jumlah) < 0):
            print("Stok game",data_game[IX][1],"gagal dikurangi karena stok kurang. Stok sekarang:",data_game[IX][5],"(<",str(abs(input_jumlah)) + ")")
        else: # (data_game[IX][5] + input_jumlah) >= 0
            data_game[IX][5] = data_game[IX][5] + input_jumlah
            if (input_jumlah < 0):
                print ("Stok game",data_game[IX][1],"berhasil dikurangi. Stok sekarang:",data_game[IX][5])
            elif (input_jumlah > 0):
                print ("Stok game",data_game[IX][1],"berhasil ditambahkan. Stok sekarang:",data_game[IX][5])
    return data_game
