import tools

def ubah_game(data_game):
    id = input('Masukkan ID game: ')
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')

    id = tools.get_index(id)
    ubah_data = [nama, kategori, tahun, harga]

    if id < 1 or id > tools.get_index(data_game[-1][0]):
        print('\nTidak ada game dengan ID tersebut!')
    else:
        for i in range(4):
            if ubah_data[i] != '':
                data_game[id][i+1] = ubah_data[i]
        print('\nSelamat! Berhasil mengubah game', data_game[id][1])

    return data_game
