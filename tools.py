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
        
        if line != raw_data[-1]:
            matrix_data += [['']]

        index_matrix += 1

    return matrix_data
