# F09 - Melihat Game yang dimiliki
import tools

def list_game(user_id, kepemilikan, game):
    # menampilkan daftar game yang dimiliki pengguna ke layar
    # I.S. pengguna sudah login dan matriks data file game dan kepemilikan terdefinisi
    # F.S. daftar game yang dimiliki user tercetak ke layar

    # KAMUS LOKAL
    # input_user_id : int
    # Found : boolean
    
    # ALGORITMA
    Found = False
    for i in range(1,len(kepemilikan)):
        if (user_id == kepemilikan[i][1]):
            if not Found: # Aksi ini pasti dilakukan 1x
                print("Daftar game:")
            Found = True
            print('{:<6} | {:<29} | {:<9} | {:<4} | {:<6}'.format(*game[tools.get_index(kepemilikan[i][0])]))
            
    if not Found:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
# referensi : https://www.semicolonworld.com/question/44245/python-format-output-string-right-alignment?msclkid=0e4d8a87b89911ecb9c76c8b7a60bae6
