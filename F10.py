import tools

def _cari_data(x, key, matriks_data):
  # Menerima input x, key, dan matriks lalu menghasilkan matriks yang berisi data-data yang
  # sesuai dengan nilai x
  temp = []
  for data in matriks_data:
    if data[key] == x:
      temp += [data]
  return temp

def buat_kepemilikan(user_id, data_kepemilikan, data_game):
  # Menerima input user id, data kepemilikan, dan data game di toko, lalu menghasilkan
  # data lengkap dari game yang dimiliki oleh sebuah user
  game_kepemilikan = _cari_data(user_id, 1, data_kepemilikan)

  temp = []
  for game in game_kepemilikan:
    temp += _cari_data(game[0], 0, data_game)
  return temp

def search_my_game(user_id, data_kepemilikan, data_game):
  # Akses : user
  # Menerima input data game dari sebuah user lalu mencari game dengan id dan input yang
  # dimasukkan lalu menampilkannya ke layar

  data_game_user = buat_kepemilikan(user_id, data_kepemilikan, data_game)
  id = input("Masukkan ID Game: ")
  tahun = input("Masukkan Tahun Rilis Game: ")

  if id == tahun == '':                                                    # ini pengecekan ditambahi kalo keduanya kosong atau tahunnya doang yg kosong
    data_hasil = data_game_user
  elif id == '':
    data_hasil = _cari_data(tahun, 3, data_game_user)
  elif tahun == '':
    data_hasil = _cari_data(id, 0, data_game_user)
  else:
    data_hasil = _cari_data(id, 0, _cari_data(tahun, 3, data_game_user))

  print("Daftar game pada inventory yang memenuhi kriteria:")
  if tools.panjang(data_hasil) == 0:
    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
  else:
    tools.print_data(data_hasil)
