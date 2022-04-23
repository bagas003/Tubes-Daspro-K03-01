import tools

def _urutkan_data(data, skema):
  # Mengurutkan data berdasarkan skema pengurutan
  # I.S. Data terdefinisi dan belum terurut
  # F.S. Data dalam keadaan terurut sesuai dengan skema pengurutan yang dipilih

  # KAMUS
  # n, key : integer
  # temp : array of Game

  n = tools.panjang(data)
  if skema == "harga+" or skema == "harga-":
    key = 4
  elif skema == "tahun+" or skema == "tahun-":
    key = 3
  elif skema == "id+":
    key = 0

  temp = [data[i] for i in range(1,n)]
  i = 1
  while i < n:
    j = i - 2
    while j >= 0 and data[i][key] < temp[j][key]:
      temp[j+1] = temp[j]
      j -= 1
    temp[j+1] = data[i]
    i += 1

  return temp

def _balikkan_data(data):
  # Membuat matriks yang berurut terbalik
  # I.S. Data game dalam keadaan terurut
  # F.S. Data game dalam keadaan terurut terbalik

  # KAMUS
  # temp : array of Game

  temp = []
  for i in range((tools.panjang(data)-1), -1, -1):
    temp += data[i]
  return temp

def list_game_toko(data_game):
  # Menampilkan game di toko secara terurut
  # I.S. Data game tersedia di toko
  # F.S. Data game ditampilkan di layar berdasarkan skema pengurutan yang dipilih

  # KAMUS
  # skema : string
  # data_terurut : array of Game

  skema = input("Skema sorting : ")

  if skema == "tahun-" or skema == "tahun+" or skema == "harga-" or skema == "harga+" or skema == '':
    skema = "id+" if skema == '' else skema
    
    data_terurut = _urutkan_data(data_game, skema)
    if skema[-1] == '-':
      data_terurut = _balikkan_data(data_terurut)
    
    tools.print_data(data_terurut)

  else:
    print("Skema sorting tidak valid!")
