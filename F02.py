# F02 - Register
import B01

def register(data_user):
    # Registrasi akun user baru ke dalam data
    # I.S. admin memasukkan data user baru
    # F.S. data user baru disimpan dan dimunculkan pesan

    # KAMUS
    # function username_valid(username: string) -> bool
    # function username_exist(username: string) -> bool
    # data_user : array of User
    # line : User
    # u, id, nama, username, password : string
    # char : char
    # a : int

    # Realisasi fungsi
    def username_valid(u):
        # validasi username
        # Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9
        for char in u:
            a = ord(char)
            if not (64 < a < 91 or 96 < a < 123 or 47 < a < 58 or a == 45 or a == 95):
                return False
        return True

    def username_exist(u):
        # validasi apakah ada username yang sama
        for line in data_user:
            if line[1] == u: return True
        return False

    # ALGORITMA UTAMA
    # input data user baru
    id = str(int(data_user[-1][0]) + 1)
    nama = input('Masukkan nama: ')
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')

    # validasi data user baru
    if not username_valid(username):
        print('\nUsername', username, 'tidak valid.')
        print('Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9.')
    elif username_exist(username):
        print('\nUsername', username, 'sudah terpakai, silakan menggunakan username lain.')
    else:
        data_user += [[id, username, nama, B01.encrypt(password), 'user', 0]]
        print('\nUsername', username, 'telah berhasil register ke dalam “Binomo”.')
    
    # mengembalikan data_user yang sudah diupdate
    return data_user
