import B01

def login(data):
  # Melakukan login untuk mengakses fitur-fitur yang terdapat pada program
  # I.S. Pengguna belum login dan hanya dapat mengakses fitur login, help, dan exit
  # F.S. Pengguna sudah login dan dapat mengakses semua fitur sesuai dengan role yang terdaftar

  # KAMUS
  # username, password : string
  # data : array of User
  # isAdmin : boolean

  username = input("Masukan username: ")
  password = input("Masukan password: ")

  for user in data:
    if user[1] == username and B01.decrypt(user[3], "daspro") == password:
      print(f'Halo {user[1]}! Selamat datang di "Binomo".')
      isAdmin = user[4] == 'admin'
      return True, isAdmin, user[0]
  
  print("Password atau username salah atau tidak ditemukan.")
  return False, False, 0

