def csv_to_array(dir):
    # parser csv ke array data
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

def panjang(elmt):
    # mengembalikan panjang string
    ln = 0
    for i in elmt:
        ln += 1
    return ln

def print_data(array_data):
    # menampilkan array data ke layar dengan indentasi
    maks_panjang = [0 for i in array_data[0]]

    for lines in array_data:
        if lines[0] == 'id': continue
        for i in range(panjang(lines)):
            if panjang(lines[i]) > maks_panjang[i]: 
                maks_panjang[i] = panjang(lines[i])
    
    for i in range(panjang(array_data)):
        if array_data[i][0] == 'id': continue
        print(f'{i+1}. ', end='')
        for j in range(panjang(array_data[0])):
            print(f'{array_data[i][j]}' + ' '*(maks_panjang[j] - panjang(array_data[i][j])) + ' | ', end='')
        print()

def array_to_string(arr):
    # mengubah array ke string agar disimpan ke csv
    converted_data = ''
    for line in arr:
        for elmt in line:
            converted_data += str(elmt)
            if elmt != line[-1]:
                converted_data += ';'
        converted_data += '\n'
    return converted_data

def get_index(game_id):
    # mengembalikan integer index dari id game 'GAMEXXX'
    return int(game_id[4])*100 + int(game_id[5])*10 + int(game_id[6])
