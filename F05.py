# F05 - Ubah Game
import tools

def ubah_game(data_game):
    # Mengubah data game yang sudah ada
    # I.S. admin memasukkan id game dan data yang akan diubah
    # F.S. mengubah data game pada database

    # KAMUS
    # data_game : array of Game
    # ubah_data : Game
    # id, nama, kategori, tahun, harga : string
    # i : integer

    # ALGORITMA UTAMA
    # input data
    id = input('Masukkan ID game: ')
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')

    id = tools.get_index(id)
    ubah_data = [nama, kategori, tahun, harga]

    # validasi id game
    if id < 1 or id > tools.get_index(data_game[-1][0]):
        print('\nTidak ada game dengan ID tersebut!')
    else:
        # mengubah database jika input tidak kosong
        for i in range(4):
            if ubah_data[i] != '':
                data_game[id][i+1] = ubah_data[i]
        print('\nSelamat! Berhasil mengubah game', data_game[id][1])

    # mengembalikan data_game yang sudah diupdate
    return data_game
