def csv_to_array(dir, type):
    f = open(dir, 'r')
    raw_data = f.readlines()
    f.close()

    matrix_data = []

    for line in raw_data:

        array_data = ['']
        index = 0
        for c in line:
            if c == ';': 
                array_data += ['']; index += 1
            elif c != '\n': 
                array_data[index] += c
        
        if type == 'user':
            if array_data[0] != 'id':
                array_data[0] = int(array_data[0])
                array_data[5] = int(array_data[5])
        elif type == 'game':
            if array_data[0] != 'id':
                array_data[4] = int(array_data[4])
                array_data[5] = int(array_data[5])

        matrix_data += [array_data]

    return matrix_data

def print_data_game(array_data):

    def panjang(elmt):
        ln = 0
        for i in elmt:
            ln += 1
        return ln

    panjang_maks = [0,0,0,0,0]
    nama_maks = 0; ktgr_maks = 0; hrga_maks = 0

    for line in array_data:
        if line[0] != 'id':
            n = panjang(line[1]); k = panjang(line[2]); h = panjang(line[4])
            if n > nama_maks: nama_maks = n
            if k > ktgr_maks: ktgr_maks = k
            if h > hrga_maks: hrga_maks = h   

    indeks = 1
    for line in array_data:
        if line[0] != 'id':
            print(f'{indeks}. ', end='')
            for i in range(5):
                if i == 1:  print(line[i], ' '*(nama_maks-panjang(line[i])), '|  ', end='')
                elif i == 2:  print(line[i], ' '*(ktgr_maks-panjang(line[i])), '|  ', end='')
                elif i == 4:  print(line[i], ' '*(hrga_maks-panjang(line[i])), '|  ', end='')
                else: print(line[i], ' |  ', end='')
            print(line[5])
            indeks += 1

print_data_game([['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], ['GAME001', 'TUBES RUSH', 'Horror', '2022', '1000', '1'], ['GAME002', 'Call of Tubes', 'Casual', '1922', '0', '99'], ['GAME003', 'Tetris', 'Casual', '1900', '0', '1']])
