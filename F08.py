# F08 - Beli Game
import time, tools

def beli_game(id_user, data_user, data_game, data_riwayat, data_kepemilikan):
    # membeli game baru oleh user
    # I.S. user memasukkan id game yang ingin dibeli
    # F.S. mengubah database jika game dapat dibeli atau menampilkan pesan jika game tidak dapat dibeli

    #KAMUS
    # data_user : array of User
    # data_game : array of Game
    # data_riwayat : array of Riwayat
    # data_kepemilikan : array of Kepemilikan
    # data : kepemilikan
    # id_user, id_game, year: string
    # indes_user, index_game : int

    # ALGORITMA UTAMA
    # input id_game dan validasi
    id_game = input('Masukkan ID Game: ')
    index_user = int(id_user)
    index_game = int(tools.get_index(id_game))

    if id_game < data_game[1][0] or id_game > data_game[-1][0]:
        # validasi id_game
        print('\nGame tidak ditemukan!')
        return data_user, data_game, data_riwayat, data_kepemilikan

    if int(data_game[index_game][4]) > int(data_user[index_user][5]):
        # validasi jumlah saldo
        print('\nSaldo anda tidak cukup untuk membeli Game tersebut!')
        return data_user, data_game, data_riwayat, data_kepemilikan

    for data in data_kepemilikan:
        # validasi kepemilikan
        if data[0] == id_game and data[1] == id_user:
            print('\nAnda sudah memiliki Game tersebut!')
            return data_user, data_game, data_riwayat, data_kepemilikan
    
    if int(data_game[index_game][5]) < 1:
        # validasi stok
        print('\nStok Game tersebut sedang habis!')
        return data_user, data_game, data_riwayat, data_kepemilikan

    # mengubah data-data saldo, stok, riwayat, dan kepemilikan
    year = time.strftime('%Y', time.gmtime())
    
    data_user[index_user][5] = str(int(data_user[index_user][5]) - int(data_game[index_game][4]))
    data_game[index_game][5] = str(int(data_game[index_game][5]) - 1)
    data_riwayat += [[id_game, data_game[index_game][1], data_game[index_game][4], id_user, year]]
    data_kepemilikan += [[id_game, id_user]]
    
    print('\nGame “' + data_game[index_game][1] + '” berhasil dibeli!')

    # mengembalikan database yang sudah diupdate
    return data_user, data_game, data_riwayat, data_kepemilikan
    
