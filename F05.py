def ubah_game(data_game):
    id = input('ID game: ')
    nama = input('nama game: ')
    kategori = input('kategori: ')
    tahun = input('tahun rilis: ')
    harga = input('harga: ')

    id = int(id[-3:])
    ubah_data = [nama, kategori, tahun, harga]

    if id < 1 or id > int(data_game[-1][0][-3:]):
        print('Tidak ada game dengan ID tersebut!')
    else:
        for i in range(4):
            if ubah_data[i] != '':
                data_game[id][i+1] = ubah_data[i]

    return data_game
