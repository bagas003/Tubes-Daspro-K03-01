import F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, B02, B03

# Deklarasi variabel
isAdmin = False
isLogin = False
# Lakukan load data secara otomatis
data_user, data_game, data_riwayat, data_kepemilikan = F15.load()


# Jika load berhasil dan data berhasil diterima maka input masukan perintah
if data_user and data_game and data_riwayat and data_kepemilikan:
    # input perintah
    perintah = input('\n>>> ')

    while not isLogin and perintah != 'exit':
        if perintah == 'login':
            isLogin, isAdmin, id = F03.login(data_user)
        elif perintah == 'help':
            F14.login_help()
        elif perintah != 'exit':
            print('\nAnda harus login terlebih dahulu.\nKetik perintah help untuk panduan penggunaan sistem.')
        perintah = input('\n>>> ')


    while perintah != 'exit':

        if perintah == 'register':
            if isAdmin: data_user = F02.register(data_user)
            else: print('\nMaaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')

        elif perintah == 'login': 
            isLogin, isAdmin, id = F03.login(data_user)

        elif perintah == 'tambah_game':
            if isAdmin: data_game = F04.tambah_game(data_game)
            else: print('\nMaaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')

        elif perintah == 'ubah_game':
            if isAdmin: data_game = F05.ubah_game(data_game)
            else: print('\nMaaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')

        elif perintah == 'ubah_stok':
            if isAdmin: data_game = F06.ubah_stok(data_game)
            else: print('\nMaaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')

        elif perintah == 'list_game_toko':
            F07.list_game_toko(data_game)  
        
        elif perintah == 'buy_game':
            if isAdmin: print('\nMaaf, anda harus menjadi user untuk melakukan hal tersebut.')
            else: data_user, data_game, data_riwayat, data_kepemilikan = F08.beli_game(id, data_user, data_game, data_riwayat, data_kepemilikan)
        
        elif perintah == 'list_game':
            if isAdmin: print('\nMaaf, anda harus menjadi user untuk melakukan hal tersebut.')
            else: F09.list_game(id, data_kepemilikan, data_game)
        
        elif perintah == 'search_my_game':
            if isAdmin: print('\nMaaf, anda harus menjadi user untuk melakukan hal tersebut.')
            else: F10.search_my_game(id, data_kepemilikan, data_game)
        
        elif perintah == 'search_game_at_store':
            F11.search_game_at_store(data_game)
        
        elif perintah == 'topup':
            if isAdmin: F12.topup(data_user)
            else: print('\nMaaf, anda tidak memiliki izin untuk menjalankan perintah berikut.')
        
        elif perintah == 'riwayat':
            if isAdmin: print('\nMaaf, anda harus menjadi user untuk melakukan hal tersebut.')
            else: F13.riwayat(id, data_riwayat)
        
        elif perintah == 'help':
            F14.help(isAdmin)
        
        elif perintah == 'save':
            F16.save(data_user, data_game, data_riwayat, data_kepemilikan)
        
        elif perintah == 'kerangajaib':
            B02.kerangajaib()
        
        elif perintah == 'tictactoe': 
            B03.tictactoe()
        
        else:
            print('\nPerintah yang dimasukkan tidak valid. Ketik perintah help untuk panduan penggunaan sistem.')

        perintah = input('\n>>> ')
    
    if F17.exit(): F16.save(data_user, data_game, data_riwayat, data_kepemilikan)
    
