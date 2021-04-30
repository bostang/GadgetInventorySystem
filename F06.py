"""
Menambah item
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
        # function bersih
            # membuat efek clear screen pada Python
        # procedure splitList
            # menulis data per baris dalam csv ke dalam bentuk array
        # procedure remove_item_from_database
            # I.S. id item yang ingin dihapus sudah divalidasi [dapat dihapus]
            # F.S. item dengan id bersangkutan telah dihapus dari file csv
        # function isIDinDatabase(id : string, database: array of array of string) -> boolean
            # memeriksa apakah id barang sudah ada di database atau belum
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
def isIDinDatabase(id,database):
    # memeriksa apakah iD item ada di suatu array database apa tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if id == element[0]: # lokasi id ada di kolom pertama
            return True
    return False

def infoBarang(id,spek):
    # mendapatkan informasi barang dari database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    if id[0] == 'C':
        arrayProcess = _consumable
    elif id[0] == 'G':
        arrayProcess = _gadget
    else:
        arrayProcess = []

    if isIDinDatabase(id,arrayProcess):
        for baris in arrayProcess:
            if baris[0] == id:
            # me-return informasi
                if spek == 'nama':
                    return baris[1]
                elif spek == 'deskripsi':
                    return baris[2]
                elif spek == 'jumlah':
                    return baris[3]
                elif spek == 'rarity':
                    return baris[4]
                elif spek == 'tahun_ditemukan' and id[0] == 'C':
                    return baris[5]
    else:
        return "\nbarang tidak ditemukan di database"

def hapusItem():
    # menerima input id barang yang ingin dihapuskan dan melakukan validasi
    # KAMUS LOKAL
        # Variabel
            # database : array of array of string
    # ALGORITMA
        # memeriksa huruf pertama
    if id_remove[0] == 'G':
        database = _gadget
    elif id_remove[0] == 'C':
        database = _consumable
    else:
        database = []

    kondisiLanjut = True
    if (isIDinDatabase(id_remove,database)):
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus {infoBarang(id_remove,'nama')}(Y/N)? ")
        while (konfirmasi != 'Y') and (konfirmasi != 'y') and (konfirmasi != 'N') and (konfirmasi != 'n'):
            print("\nHarap masukan dengan benar!\n")
        else:
            if (konfirmasi == 'Y') or (konfirmasi == 'y'):
                print("\nItem telah berhasil dihapus dari database")
            else:
                print("\nItem tidak dihapus dari database")
                kondisiLanjut = False
    else: # barang tidak ditemukan di database
        print("\nTidak ada item dengan id tersebut")
        kondisiLanjut = False
    
    if kondisiLanjut:
        overwrite_database(id_remove[0])

def convert_datas_to_string(code):
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
    elif code == 'G':
        arrayProcess = _gadget

    string_data = ""
    for arr_data in arrayProcess:
        if arr_data[0] == id_remove : # kita tidak akan mendaftarkan id yang ingin kita hapus
            continue
        arr_data_all_string = [var for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def overwrite_database(code):
    # melakukan overwrite terhadap konten database [digunakan dalam skema penghapusan item dari csv]
    # KAMUS LOKAL
        # datas_as_string : string { untain informasi dari database [lokal] }
    # ALGORITMA
    datas_as_string = convert_datas_to_string(id_remove[0])
    if code == 'C':
        f = open("consumable.csv","w")
    elif code == 'G':
        f = open("gadget.csv","w")
    f.write(datas_as_string) # melakukan overwrite terhadap isi database
    f.close()

# ALGORITMA UTAMA

    # membaca file database.csv
g = open("gadget.csv","r")
c = open("consumable.csv","r")
raw_lines_g = g.readlines()
raw_lines_c = c.readlines()
g.close()
c.close()
lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]
lines_c = [raw_line.replace("\n", "") for raw_line in raw_lines_c]

    # mengakses database dalam bentuk array
_gadget = []
_consumable = []

for line in lines_g:
    array_of_data = split(line)
    _gadget.append(array_of_data)
for line in lines_c:
    array_of_data = split(line)
    _consumable.append(array_of_data)

    # melakukan skema penghapusan
clear_screen()
print(">>> Menghapus Item")
id_remove = input("Masukkan ID item: ")
hapusItem()
print("")
os.system('pause')