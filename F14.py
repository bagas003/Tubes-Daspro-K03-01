def help(isAdmin):
    if isAdmin: print('''
    ================================= HELP =================================
1.  register             - Untuk melakukan registrasi user baru
2.  login                - Untuk melakukan login ke dalam sistem
3.  tambah_game          - Untuk menambah game yang dijual pada toko
4.  ubah_game            - Untuk mengubah informasi game yang dijual pada toko
5.  ubah_stok            - Untuk mengubah stok game yang dijual pada toko
6.  list_game_toko       - Untuk melihat list game yang dijual pada toko
7.  search_game_at_store - Untuk mencari dan mendapatkan informasi game pada toko 
8.  topup                - Untuk menambahkan saldo kepada user
9.  help                 - Untuk memberikan panduan penggunaan sistem
10. save                 - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
11. exit                 - Untuk keluar dari aplikasi
    ''')

    else: print('''
    ================================= HELP =================================
1.  login                - Untuk melakukan login ke dalam sistem
2.  list_game_toko       - Untuk melihat list game yang dijual pada toko
3.  buy_game             - Untuk membeli game yang ada pada toko
4.  list_game            - Untuk melihat list game yang dimiliki pengguna
5.  search_my_game       - Untuk mencari dan mendapatkan informasi game yang dimiliki pengguna
6.  search_game_at_store - Untuk mencari dan mendapatkan informasi game pada toko 
7.  riwayat              - Untuk melihat riwayat pembelian game oleh pengguna
8.  help                 - Untuk memberikan panduan penggunaan sistem
9.  save                 - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
10. exit                 - Untuk keluar dari aplikasi
    ''')
