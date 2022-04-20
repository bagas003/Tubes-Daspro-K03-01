import time
import tools


def beli_game(id_user, data_user, data_game, data_riwayat, data_kepemilikan):

    id_game = input('Masukkan ID Game: ')
    index_user = int(id_user)
    index_game = int(tools.get_index(id_game))

    if id_game < data_game[1][0] or id_game > data_game[-1][0]:
        print('\nGame tidak ditemukan!')
        return data_user, data_game, data_riwayat, data_kepemilikan

    if int(data_game[index_game][4]) > int(data_user[index_user][5]):
        print('\nSaldo anda tidak cukup untuk membeli Game tersebut!')
        return data_user, data_game, data_riwayat, data_kepemilikan

    for data in data_kepemilikan:
        if data[0] == id_game and data[1] == id_user:
            print('\nAnda sudah memiliki Game tersebut!')
            return data_user, data_game, data_riwayat, data_kepemilikan
    
    if int(data_game[index_game][5]) < 1:
        print('\nStok Game tersebut sedang habis!')
        return data_user, data_game, data_riwayat, data_kepemilikan

    year = time.asctime()[-4] + time.asctime()[-3] + time.asctime()[-2] + time.asctime()[-1]
    
    data_user[index_user][5] = str(int(data_user[index_user][5]) - int(data_game[index_game][4]))
    data_game[index_game][5] = str(int(data_game[index_game][5]) - 1)
    data_riwayat += [[id_game, data_game[index_game][1], data_game[index_game][4], id_user, year]]
    data_kepemilikan += [[id_game, id_user]]
    
    print('\nGame “' + data_game[index_game][1] + '” berhasil dibeli!')

    return data_user, data_game, data_riwayat, data_kepemilikan
    
