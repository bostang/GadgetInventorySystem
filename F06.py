"""
Menghapus item
Akses: Admin

Admin memiliki wewenang untuk menghapus suatu item pada database. Bila item sudah dihapus.
entry item akan hilang dari file bila di-save.

Kontributor : Bostang Palaguna [16520090], Muhammad Daris Nurhakim [16520170]

"""

# mengimport file dari Python
import os
from Basic_Procedure import *

# KAMUS
    # Variabel
        # id_remove : string { id yang ingin dihapus }
        # kondisiLanjut : boolean { jika bernilai True, maka penghapusan akan dilanjutkan }
    # Fungsi / Prosedur
        # procedure remove_item_from_database
            # I.S. id item yang ingin dihapus sudah divalidasi [dapat dihapus]
            # F.S. item dengan id bersangkutan telah dihapus dari file csv
        # procedure hapusItem
            # menerima input id barang yang ingin dihapuskan dan melakukan validasi
            # I.S. belum diterima barang yang mau dihapus
            # F.S. jika id item ada, maka skema penghapusan akan dilanjutkan, jika tidak ada, pesan error ditampilkan
        # procedure convert_datas_to_string
            # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
            # I.S. database terdefinisi dalam bentuk array # F.S. database dalam bentuk string terbentuk dan siap untuk di-overwrite ke file csv
        # procedure overwrite_database
            # melakukan overwrite terhadap konten database [digunakan dalam skema penghapusan item dari csv]
            # I.S. belum ada perubahan pada database ; F.S. database telah ditulis ulang tanpa mengikutkan item yang dihapus
# REALISASI FUNGSI/PROSEDUR
def overwrite_database(code,id_remove,_consumable,_gadget):
    # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
    # KAMUS LOKAL
        # Variabel
            # arr_data : array { array yang merupakan elemen _gadget atau _consumable }
            # arr_data_all_string : array of string { untuk skema konversi array database menjadi string }
            # arrayProcess : array of string { array yang ingin diproses }
            # string_data : string { untain informasi dari database [lokal] }
    # ALGORITMA
    if code == 'C':
        arrayProcess = _consumable
        _consumable = []
    elif code == 'G':
        arrayProcess = _gadget
        _gadget = []

    for arr_data in arrayProcess:
        if arr_data[0] == id_remove : # kita tidak akan mendaftarkan id yang ingin kita hapus
            continue
        if code == 'C':
            string = [arr_data[0],arr_data[1],arr_data[2],arr_data[3],arr_data[4]]
            _consumable.append(string)
        elif code == 'G':
            string = [arr_data[0],arr_data[1],arr_data[2],arr_data[3],arr_data[4],arr_data[5]]
            _gadget.append(string)
    return _consumable, _gadget

# ALGORITMA UTAMA
def hapusItem(_consumable,_gadget):
    # menerima input id barang yang ingin dihapuskan dan melakukan validasi
    # KAMUS LOKAL
        # Variabel
            # database : array of array of string
    # ALGORITMA
    clear_screen()
    print(">>> Menghapus Item")
    id_remove = input("Masukkan ID item: ").upper()
    # memeriksa huruf pertama
    if id_remove[0] == 'G':
        database = _gadget
    elif id_remove[0] == 'C':
        database = _consumable
    else:
        database = []

    if (isIDinDatabase(id_remove,database)):
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus {infoBarang(id_remove,'nama',_consumable,_gadget)}(Y/N)? ")
        while (konfirmasi != 'Y') and (konfirmasi != 'y') and (konfirmasi != 'N') and (konfirmasi != 'n'):
            print("\nHarap masukan dengan benar!\n")
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus {infoBarang(id_remove,'nama',_consumable,_gadget)}(Y/N)? ")
        else:
            if (konfirmasi == 'Y') or (konfirmasi == 'y'):
                _consumable, _gadget = overwrite_database(id_remove[0],id_remove,_consumable,_gadget)
                print("\nItem telah berhasil dihapus dari database")
                os.system('pause')
                return _consumable, _gadget
            else:
                print("\nItem tidak dihapus dari database")
    else: # barang tidak ditemukan di database
        print("\nTidak ada item dengan id tersebut")
    os.system('pause')