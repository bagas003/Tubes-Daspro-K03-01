# F13 - Melihat Riwayat Pembelian
def riwayat(user_id, history):                                             # user_id dijadikan sebagai parameter dan bukan sbg input
    # menampilkan daftar riwayat pembelian game 
    # I.S. pengguna sudah login dan matriks data file riwayat terdefinisi
    # F.S. database riwayat pembelian game tercetak ke layar

    # KAMUS LOKAL
    # input_user_id : int
    # isHistEmpty : boolean
    
    # ALGORITMA
    isHistEmpty = True
    for i in range(1,len(history)):
        if (history[i][3] == user_id):
            if isHistEmpty: # aksi ini pasti dilakukan 1x
                print("Daftar game:") 
            isHistEmpty = False
            print('{:<6} | {:<29} | {:<7} | {:<6}'.format(history[i][0],history[i][1],history[i][2],history[i][4]))
            
    if isHistEmpty:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
