# F09 - Melihat Game yang dimiliki
def listgame(data_kepemilikan,data_game):
    # menampilkan daftar game yang dimiliki pengguna ke layar
    # I.S. pengguna sudah login dan matriks data file game dan kepemilikan terdefinisi
    # F.S. daftar game yang dimiliki user tercetak ke layar

    # KAMUS LOKAL
    # input_user_id : int
    # Found : boolean
    
    # ALGORITMA
    input_user_id = int(input("Masukkan user_id: "))
    Found = False
    for i in range(1,len(kepemilikan)):
        if (input_user_id == kepemilikan[i][1]):
            if (kepemilikan[i][0] == game[i][0]):
                if not Found: # Aksi ini pasti dilakukan 1x
                    print("Daftar game:")
                Found = True
                print('{:<6} | {:<29} | {:<9} | {:<4} | {:<6}'.format(*game[i]))
            
    if not Found:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    return data_kepemilikan
# referensi : https://www.semicolonworld.com/question/44245/python-format-output-string-right-alignment?msclkid=0e4d8a87b89911ecb9c76c8b7a60bae6
