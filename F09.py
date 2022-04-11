# F09 - Melihat Game yang dimiliki
def listgame(data_game):
    # menampilkan daftar game yang dimiliki pengguna ke layar
    # I.S. pengguna sudah login dan matriks data file data_game terdefinisi
    # F.S. database game tercetak ke layar

    # KAMUS LOKAL

    # ALGORITMA
    if len(data_game) == 1:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else: 
        print("Daftar game:")
        for i in range(1,len(data_game)):
            print('{:<6} | {:<29} | {:<9} | {:<4} | {:<6}'.format(*data_game[i]))
    return data_game
# referensi : https://www.semicolonworld.com/question/44245/python-format-output-string-right-alignment?msclkid=0e4d8a87b89911ecb9c76c8b7a60bae6
