# F06 - Mengubah Stok Game di Toko
import tools

def ubah_stok(data_game):
    # Mengubah Stok Game di Toko
    # I.S. pengguna sudah login dan matriks data file game terdefinisi
    # F.S. stok item pada database berubah

    # KAMUS LOKAL
    # input_id : string
    # input_jumlah : int
    # isjumlahValid : bool
    # i : int 
    # IX : int (Indeks dimana id ditemukan)

    # ALGORITMA
    input_id = input("Masukkan ID game: ")

    # Validasi ID Game
    IX = -999
    if input_id[:4] == 'GAME':
        for i in range(1,tools.panjang(data_game)):
            if data_game[i][0] == input_id:
                IX = i
                break

    if IX == -999:
        print ("Tidak ada game dengan ID tersebut!")
    else: # IX != -999
        # Validasi input_jumlah
        isjumlahValid = False
        while not isjumlahValid:
            input_jumlah = int(input("Masukkan jumlah: ")) 
            if (input_jumlah == 0): # Asumsi jumlah yg diinput != 0
                print ("Silahkan masukkan kembali angka yang benar ( min. 1 )")
            else:
                isjumlahValid = True
                
        # Validasi stok game setelah pengubahan (tidak negatif)
        if ((int(data_game[IX][5]) + input_jumlah) < 0):
            print(f'Stok game {data_game[IX][1]} gagal dikurangi karena stok kurang. Stok sekarang: {data_game[IX][5]} (< {0-input_jumlah})')
        else: # (data_game[IX][5] + input_jumlah) >= 0
            data_game[IX][5] = str(int(data_game[IX][5]) + input_jumlah)
            if (input_jumlah < 0):
                print (f'Stok game {data_game[IX][1]} berhasil dikurangi. Stok sekarang: {data_game[IX][5]}')
            elif (input_jumlah > 0):
                print (f'Stok game {data_game[IX][1]} berhasil ditambahkan. Stok sekarang: {data_game[IX][5]}')
    return data_game
