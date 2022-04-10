def save(user,game,riwayat,kepemilikan):
    
    def array_to_string(arr):
        converted_data = ''
        for line in arr:
            for elmt in line:
                converted_data += str(elmt)
                if elmt != line[-1]:
                    converted_data += ';'
            converted_data += '\n'
        return converted_data

    import os

    dir = input('Masukkan nama folder penyimpanan: ')

    if os.path.isdir(dir):
        os.rmdir(dir)

    os.makedirs(dir)

    var_pointer = [user, game, riwayat, kepemilikan]
    str_pointer = ['user', 'game', 'riwayat', 'kepemilikan']
    for i in range(4):
        f = open(fr'{dir}\{str_pointer[i]}', 'w')
        f.write(array_to_string(var_pointer[i]))
        f.close()


