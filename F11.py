def search_game_at_store(data_game):
    array_input = ['','','','','']
    array_input[0] = input('Masukkan ID Game: ')
    array_input[1] = input('Masukkan Nama Game: ')
    array_input[4] = input('Masukkan Harga Game: ')
    array_input[2] = input('Masukkan Kategori Game: ')
    array_input[3] = input('Masukkan Tahun Rilis Game: ')

    indeks = 1
    for data in data_game:
        if data[0] != 'id':
            matched = True
            for i in range(5):
                if array_input[i] != '' and array_input[i] != data[i]:
                    matched = False
            if matched:
                print(f'{indeks}. {data[0]:5s} | {data[1]:20s} | {data[4]:7s} | {data[2]:10s} | {data[3]:4s} | {data[5]:1s}')
                indeks += 1
