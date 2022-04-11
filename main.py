import tools
import F02
import F03
import F04
import F05
import F14
import F15
import F16
import F17
import B03

# Deklarasi variabel
isAdmin = False
# Lakukan load data secara otomatis
data_user, data_game, data_riwayat, data_kepemilikan = F15.load()

# Jika load berhasil dan data berhasil diterima maka input masukan perintah
if data_user and data_game and data_riwayat and data_kepemilikan:
    # input perintah
    perintah = input('>>> ')

    while perintah != 'login':
        print('Anda harus login terlebih dahulu!')
        perintah = input('>>> ')

    while perintah != 'exit':
        match perintah:
            case 'register': 
                if isAdmin: data_user = F02.register(data_user)
                else: print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')
            case 'login': 
                isAdmin, id = F03.login(data_user)
            case 'tambah_game':
                if isAdmin: data_game = F04.tambah_game(data_game)
                else: print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')
            case 'ubah_game':
                if isAdmin: data_game = F05.ubah_game(data_game)
                else: print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')
            
            case 'help':
                F14.help(isAdmin)
            case 'save':
                F16.save(data_user, data_game, data_riwayat, data_kepemilikan)
            case 'tictactoe': B03.tictactoe()

        perintah = input('>>> ')
    
    if F17.exit(): F16.save(data_user, data_game, data_riwayat, data_kepemilikan)
    
            