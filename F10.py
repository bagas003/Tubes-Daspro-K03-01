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

def search_my_game(data_game_user):
  # Akses : user
  # Menerima input data game dari sebuah user lalu mencari game dengan id dan input yang
  # dimasukkan lalu menampilkannya ke layar
  id = input("Masukkan ID Game: ")
  tahun = int(input("Masukkan Tahun Rilis Game: "))

  if id == '':
    data_hasil = _cari_data(tahun, 3, data_game_user)
  else:
    data_hasil = _cari_data(id, 0, _cari_data(tahun, 3, data_game_user))

  print("Daftar game pada inventory yang memenuhi kriteria:")
  if len(data_hasil) == 0:
    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
  else:
    i = 1
    for game in data_hasil:
      print(f"{i}. {game[0]:5s} | {game[1]:20s} | {game[4]:7d} | {game[2]:10s} | {game[3]:4d}")
      i += 1