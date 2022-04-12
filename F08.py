def beli_game(id_user, data_user, data_game, data_riwayat, data_kepemilikan):

    id_game = input('Masukkan ID Game: ')
    index_user = int(id_user)
    index_game = int(id_game[-3:])

    if int(data_game[index_game][4]) > int(data_user[index_user][5]):
        print('Saldo anda tidak cukup untuk membeli Game tersebut!')
        return data_user, data_game, data_riwayat, data_kepemilikan

    for data in data_kepemilikan:
        if data[0] == id_game and data[1] == id_user:
            print('Anda sudah memiliki Game tersebut!')
            return data_user, data_game, data_riwayat, data_kepemilikan
    
    if int(data_game[index_game][5]) < 1:
        print('Stok Game tersebut sedang habis!')
        return data_user, data_game, data_riwayat, data_kepemilikan
    
    data_user[index_user][5] = str(int(data_user[index_user][5]) - int(data_game[index_game][4]))
    data_game[index_game][5] = str(int(data_game[index_game][5]) - 1)
    data_riwayat += [[id_game, data_game[index_game][1], data_game[index_game][4], id_user, 2022]]
    data_kepemilikan += [[id_game, id_user]]
    
    print('Game “' + data_game[index_game][1] + '” berhasil dibeli!')

    return data_user, data_game, data_riwayat, data_kepemilikan
    
