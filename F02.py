import B01

def register(data_user):
    def username_valid(u):
        for char in u:
            a = ord(char)
            if not (64 < a < 91 or 96 < a < 123 or 47 < a < 58 or a == 45 or a == 95):
                return False
        return True

    def username_exist(u):
        for line in data_user:
            if line[1] == u: return True
        return False

    id = str(int(data_user[-1][0]) + 1)
    nama = input('\nnama: ')
    username = input('username: ')
    password = input('password: ')

    if not username_valid(username):
        print('Username', username, 'tidak valid.')
        print('Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9.')
    elif username_exist(username):
        print('Username', username, 'sudah terpakai, silakan menggunakan username lain.')
    else:
        data_user += [[id, username, nama, B01.encrypt(password, "daspro"), 'user', 0]]
        print('Username', username, 'telah berhasil register ke dalam “Binomo”.')
    
    return data_user


