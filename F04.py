def tambah_game(data_game):
    id = 'GAME' + f"{int(data_game[-1][0][-3:]) + 1:03d}"
    nama = input('\nnama game: ')
    kategori = input('kategori: ')
    tahun = input('tahun rilis: ')
    harga = input('harga: ')
    stok = input('stok awal: ')
    new_game_data = [id, nama, kategori, tahun, harga, stok]

    while nama and kategori and tahun and harga and stok:
        print('\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
        nama = input('\nnama game: ')
        kategori = input('kategori: ')
        tahun = input('tahun rilis: ')
        harga = input('harga: ')
        stok = input('stok awal: ')
        new_game_data = [id, nama, kategori, tahun, harga, stok]

    data_game += [new_game_data]

    print('\nSelamat! Berhasil menambahkan game', nama)

    return data_game
