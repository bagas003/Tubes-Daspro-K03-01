# F04 - Tambah Game
import tools

def tambah_game(data_game):
    # menambah game baru ke database
    # I.S. admin memasukkan data game baru
    # F.S. data game baru yang telah divalidasi disimpan di database

    # KAMUS
    # data_game : array of Game
    # new_data_game : Game
    # id, nama, kategori, tahun, harga, stok : string

    # ALGORITMA UTAMA
    # input data
    id = 'GAME' + f"{tools.get_index(data_game[-1][0]) + 1:03d}"
    nama = input('Masukkan nama game: ')
    kategori = input('Masukkan kategori: ')
    tahun = input('Masukkan tahun rilis: ')
    harga = input('Masukkan harga: ')
    stok = input('Masukkan stok awal: ')

    while not (nama and kategori and tahun and harga and stok):
        # jika data ada yang kosong, maka pengguna diminta menginput kembali
        print('\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
        nama = input('Masukkan nama game: ')
        kategori = input('Masukkan kategori: ')
        tahun = input('Masukkan tahun rilis: ')
        harga = input('Masukkan harga: ')
        stok = input('Masukkan stok awal: ')
    
    # memasukkan data baru ke database
    new_game_data = [id, nama, kategori, tahun, harga, stok]
    data_game += [new_game_data]

    print('\nSelamat! Berhasil menambahkan game', nama)

    # mengembalikan data yang sudah ditambah
    return data_game
