import tools

def _cari_data(x, key, matriks_data):
  # Menghasilkan matriks dengan data-data yang sesuai dengan nilai x
  # I.S. Data tersimpan dalam sebuah matriks
  # F.S. Dihasilkan matriks baru dengan data-data yang sesuai dengan nilai x

  # KAMUS
  # temp : array of array of string

  temp = []
  for data in matriks_data:
    if data[key] == x:
      temp += [data]
  return temp

def _buat_kepemilikan(user_id, data_kepemilikan, data_game):
  # Menghasilkan data lengkap dari game yang dimiliki oleh sebuah user
  # I.S. Data kepemilikan dan data game terdefinisi
  # F.S. Dihasilkan data baru yang berisi data game oleh sebuah user

  # KAMUS
  # game_kepemilikan : array of string
  # temp : array of Game

  game_kepemilikan = _cari_data(user_id, 1, data_kepemilikan)

  temp = []
  for game in game_kepemilikan:
    temp += _cari_data(game[0], 0, data_game)
  return temp

def search_my_game(user_id, data_kepemilikan, data_game):
  # Menampilkan data game yang dimiliki oleh seorang user berdasarkan id dan tahun
  # I.S. Data game dan data kepemilikan terdefinisi
  # F.S. Data game yang dimiliki oleh seorang user yang sesuai dengan id dan tahun ditampilkan 
  # di layar

  # KAMUS
  # data_game_user, data_hasil : array of Game
  # id, tahun : string

  data_game_user = _buat_kepemilikan(user_id, data_kepemilikan, data_game)
  id = input("Masukkan ID Game: ")
  tahun = input("Masukkan Tahun Rilis Game: ")

  if id == tahun == '':
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
