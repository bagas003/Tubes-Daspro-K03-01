# F13 - Melihat Riwayat Pembelian
import tools


def riwayat(user_id, history):                                             # user_id dijadikan sebagai parameter dan bukan sbg input
    # menampilkan daftar riwayat pembelian game 
    # I.S. pengguna sudah login dan matriks data file riwayat terdefinisi
    # F.S. database riwayat pembelian game tercetak ke layar

    # KAMUS LOKAL
    # input_user_id : int
    # isHistEmpty : boolean
    
    # ALGORITMA
    isHistEmpty = True
    user_history = []
    for i in range(1, tools.panjang(history)):
        if (history[i][3] == user_id):
            if isHistEmpty: # aksi ini pasti dilakukan 1x
                print("\nDaftar game:") 
            isHistEmpty = False
            user_history += [history[i]]
            
    if isHistEmpty:
        print("\nMaaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else:
        tools.print_data(user_history)
