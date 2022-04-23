# F16 - Save
import os
import tools

def save(user,game,riwayat,kepemilikan):
    # Menyimpan data yang sudah diubah pada folder yang diinginkan pengguna
    # I.S. pengguna memasukkan input folder penyimpanan
    # F.S. menyimpan data pada folder input

    # KAMUS
    # user : array of User
    # game : array of Game
    # riwayat : array of Riwayat
    # kepemilikan : array of Kepemilikan
    # dir : string
    # str_pointer : array of string
    # var_pointer : array of <array of User, array of Game, array of Riwayat, array of Kepemilikan>

    # ALGORITMA
    # input nama folder
    dir = input('Masukkan nama folder penyimpanan: ')
    print('\nsaving...')

    # membuat folder baru jika belum ada atau mereplace folder lama jika sudah ada
    if os.path.isdir(dir):
        os.replace(dir, dir)
    else:
        os.makedirs(dir)

    # menyimpan masing-masing data
    var_pointer = [user, game, riwayat, kepemilikan]
    str_pointer = ['user', 'game', 'riwayat', 'kepemilikan']
    for i in range(4):
        f = open(fr'{dir}\{str_pointer[i]}.csv', 'w')
        f.write(tools.array_to_string(var_pointer[i]))
        f.close()
    print('Data telah disimpan pada folder', dir)
