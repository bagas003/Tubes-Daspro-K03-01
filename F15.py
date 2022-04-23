import argparse
from tools import csv_to_array

def load():
  # Memasukkan data CSV ke dalam program utama dalam bentuk sebuah matriks
  # I.S. Terdapat 4 data csv yang tersimpan dalam sebuah folder
  # F.S. Dihasilkan 4 matriks yang berisi keempat data csv tersebut

  # KAMUS
  # data_user : array of User
  # data_game : array of Game
  # data_riwayat : array of Riwayat
  # data_kepemilikan : array of Kepemilikan

  parser = argparse.ArgumentParser()
  parser.add_argument("nama_folder", nargs='?', default=None)
  args = parser.parse_args()

  if not args.nama_folder:
    print("Tidak ada nama folder yang diberikan!")
    return (None, None, None, None)
  else:
    try:
      data_user = csv_to_array(rf"{args.nama_folder}\user.csv")
      data_game = csv_to_array(rf"{args.nama_folder}\game.csv")
      data_riwayat = csv_to_array(rf"{args.nama_folder}\riwayat.csv")
      data_kepemilikan = csv_to_array(rf"{args.nama_folder}\kepemilikan.csv")

      return (data_user, data_game, data_riwayat, data_kepemilikan)
    except FileNotFoundError:
      print(f'Folder "{args.nama_folder}" tidak ditemukan.')
      return (None, None, None, None)