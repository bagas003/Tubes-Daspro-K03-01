# F09 - Melihat Game yang dimiliki
def listgame(game):
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
    return game
# referensi : https://www.semicolonworld.com/question/44245/python-format-output-string-right-alignment?msclkid=0e4d8a87b89911ecb9c76c8b7a60bae6
