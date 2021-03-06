# F09 - Melihat Game yang dimiliki
import tools

def list_game(user_id, kepemilikan, game):
    # menampilkan daftar game yang dimiliki pengguna ke layar
    # I.S. pengguna sudah login dan matriks data file game dan kepemilikan terdefinisi
    # F.S. daftar game yang dimiliki user tercetak ke layar

    # KAMUS LOKAL
    # input_user_id,idx : int
    # Found : boolean
    
    # ALGORITMA
    Found = False
    kepemilikan_user = []
    for i in range(1, tools.panjang(kepemilikan)):
        if (user_id == kepemilikan[i][1]):
            if not Found: # Aksi ini pasti dilakukan 1x
                print("\nDaftar game:")
            Found = True
            idx = tools.get_index(kepemilikan[i][0])
            kepemilikan_user += [[game[idx][0],game[idx][1],game[idx][2],game[idx][3],game[idx][4]]]
    
    tools.print_data(kepemilikan_user)
            
    if not Found:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
