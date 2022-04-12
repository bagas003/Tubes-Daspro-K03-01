import os
import tools

def save(user,game,riwayat,kepemilikan):
    dir = input('Masukkan nama folder penyimpanan: ')

    if os.path.isdir(dir):
        os.rmdir(dir)

    os.makedirs(dir)

    var_pointer = [user, game, riwayat, kepemilikan]
    str_pointer = ['user', 'game', 'riwayat', 'kepemilikan']
    for i in range(4):
        f = open(fr'{dir}\{str_pointer[i]}', 'w')
        f.write(tools.array_to_string(var_pointer[i]))
        f.close()
