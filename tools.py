def csv_to_array(dir):
    f = open(dir, 'r')
    raw_data = f.readlines()
    f.close()

    matrix_data = [['']]
    index_matrix = 0

    for line in raw_data:
        index_array = 0

        for c in line:
            if c == ';': 
                matrix_data[index_matrix] += ['']
                index_array += 1
            elif c != '\n': 
                matrix_data[index_matrix][index_array] += c
        
        if line != raw_data[-1]: matrix_data += [['']]
        index_matrix += 1

    return matrix_data

def print_data_game(array_data):

    def panjang(elmt):
        ln = 0
        for i in elmt:
            ln += 1
        return ln

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

def array_to_string(arr):
    converted_data = ''
    for line in arr:
        for elmt in line:
            converted_data += str(elmt)
            if elmt != line[-1]:
                converted_data += ';'
        converted_data += '\n'
    return converted_data

def get_index(game_id):
    return int(game_id[4])*100 + int(game_id[5])*10 + int(game_id[6])
