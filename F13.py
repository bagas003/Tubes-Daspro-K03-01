# F13 - Melihat Riwayat Pembelian
def riwayat(data_history):
    # menampilkan daftar riwayat pembelian game 
    # I.S. pengguna sudah login dan matriks data file riwayat terdefinisi
    # F.S. database riwayat pembelian game tercetak ke layar

    # KAMUS LOKAL
    # input_user_id : int
    # isHistEmpty : boolean
    
    # ALGORITMA
    input_user_id = int(input("Masukan user_id: "))

    isHistEmpty = True
    for i in range(1,len(history)):
        if (history[i][3] == input_user_id):
            if isHistEmpty: # aksi ini pasti dilakukan 1x
                print("Daftar game:") 
            isHistEmpty = False
            print('{:<6} | {:<29} | {:<7} | {:<6}'.format(history[i][0],history[i][1],history[i][2],history[i][4]))
            
    if isHistEmpty:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    return data_history

# referensi : https://www.semicolonworld.com/question/44245/python-format-output-string-right-alignment?msclkid=0e4d8a87b89911ecb9c76c8b7a60bae6
