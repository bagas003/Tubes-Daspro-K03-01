# F11 - Mencari Game di Toko
import tools

def search_game_at_store(data_game):
    # mencari game di toko dengan parameter id, nama, harga, kategori, dan tahun rilis
    # I.S. input data game dari pengguna
    # F.S. game yang sesuai dengan input pengguna

    # KAMUS
    # data_game, matched_games : array of Game
    # array_input, data : Game
    # ada, matched : bool
    # i : int

    # ALGORITMA UTAMA
    # inisiasi dan input pengguna
    array_input = ['','','','','']
    array_input[0] = input('Masukkan ID Game: ')
    array_input[1] = input('Masukkan Nama Game: ')
    array_input[4] = input('Masukkan Harga Game: ')
    array_input[2] = input('Masukkan Kategori Game: ')
    array_input[3] = input('Masukkan Tahun Rilis Game: ')

    ada = False
    matched_games = []

    # mengecek game yang cocok dan memasukkannya ke matched_games
    print('\nDaftar game pada toko yang memenuhi kriteria:')
    for data in data_game:
        if data[0] != 'id':
            matched = True
            for i in range(5):
                if array_input[i] != '' and array_input[i] != data[i]:
                    matched = False
            if matched:
                ada = True
                matched_games += [data]
    
    # menampilkan pesan atau data game yang cocok
    if ada: 
        tools.print_data(matched_games)
    else: 
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
