import tools

def tambah_game(data_game):
    id = 'GAME' + f"{tools.get_index(data_game[-1][0]) + 1:03d}"
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')
    stok = input('Masukkan stok awal: ')
    new_game_data = [id, nama, kategori, tahun, harga, stok]

    while not (nama and kategori and tahun and harga and stok):
        print('\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
        nama = input('Masukkan nama game: ')
        kategori = input('Masukkan kategori: ')
        tahun = input('Masukkan tahun rilis: ')
        harga = input('Masukkan harga: ')
        stok = input('Masukkan stok awal: ')
        new_game_data = [id, nama, kategori, tahun, harga, stok]

    data_game += [new_game_data]

    print('\nSelamat! Berhasil menambahkan game', nama)

    return data_game
