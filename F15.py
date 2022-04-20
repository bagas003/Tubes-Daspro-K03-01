import argparse
from tools import csv_to_array

def load():
  # Fungsi untuk memasukkan data CSV ke dalam program utama dalam bentuk sebuah matriks
  # sehingga menghasilkan 4 matriks berupa data user, data game, data riwayat, dan data
  # kepemilikan
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