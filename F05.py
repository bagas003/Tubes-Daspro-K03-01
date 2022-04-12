import tools

def ubah_game(data_game):
    id = input('ID game: ')
    nama = input('nama game: ')
    kategori = input('kategori: ')
    tahun = input('tahun rilis: ')
    harga = input('harga: ')

    id = tools.get_index(id)
    ubah_data = [nama, kategori, tahun, harga]

    if id < 1 or id > tools.get_index(data_game[-1][0]):
        print('Tidak ada game dengan ID tersebut!')
    else:
        for i in range(4):
            if ubah_data[i] != '':
                data_game[id][i+1] = ubah_data[i]

    return data_game
