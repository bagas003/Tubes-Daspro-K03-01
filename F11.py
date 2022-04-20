import tools

def search_game_at_store(data_game):
    array_input = ['','','','','']
    array_input[0] = input('Masukkan ID Game: ')
    array_input[1] = input('Masukkan Nama Game: ')
    array_input[4] = input('Masukkan Harga Game: ')
    array_input[2] = input('Masukkan Kategori Game: ')
    array_input[3] = input('Masukkan Tahun Rilis Game: ')

    ada = False
    matched_games = []

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
    
    if ada: tools.print_data(matched_games)
    else: print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
