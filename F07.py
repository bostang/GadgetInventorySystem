"""
Mengubah jumlah item
Akses: Admin

Admin dapat mengubah jumlah gadget atau consumable yang terdapat di dalam sistem.
Pastikan jumlah gadget atau consumable yang telah diupdate tetap valid(tidak negatif).
Bila consumable dan gadget menjadi 0, tidak perlu dihapus dari sistem.

Kontributor : Bostang Palaguna [16520090], Muhammad Daris Nurhakim [16520170]

"""

import os
from Basic_Procedure import *

# KAMUS
    # Variabel
        # idUbah : string { id item yang mau diubah jumlahnya }
        # jumlahUbah : integer { penambahan / pengurangan terhadap jumlah awal gadget }
        # kondisiLanjut : boolean { jika True, maka proses overwritting pada file csv akan dieksekusi }
    # Fungsi/Prosedur
        # function isIDinDatabase(id : string, database: array of array of string) -> boolean
            # memeriksa apakah id barang sudah ada di database atau belum
        # procedure convert_to_real(input code : character)
            # mengonversi data suatu array database supaya bisa dimanipulasi nilainya
            # I.S. data pada kolom 'jumlah' masih berupa string
            # F.S. data pada kolom 'jumlah' bertipe integer dan siap dimanipulasi
        # procedure convert_datas_to_string_ubahJumlah(input code : character)
            # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
            # I.S. database terdefinisi dalam bentuk array
            # F.S. database dalam bentuk string terbentuk dan siap untuk di-overwrite ke file csv
        # procedure overwrite_database(input code : character)
            # melakukan overwrite terhadap konten database [digunakan dalam skema penggantian jumlah item pada file csv]
            # I.S. belum ada perubahan pada database
            # F.S. database telah ditulis ulang dengan perubahan salah satu jumlah item
        # procedure change_quantity_in_database(input idUbah : string, jumlahUbah: integer ,code: character)
            # melakukan skema pengubahan jumlah barang pada array _consumable atau _gadget
            # I.S. atribut jumlah salah satu item pada array _consumable atau _gadget belum berubah
            # I.S. atribut jumlah salah satu item pada array _consumable atau _gadget sudah berubah
        # function infoBarang(id : string ,spek : string) -> string / integer
            # mendapatkan informasi barang dari database

# REALISASI FUNGSI/PROSEDUR
def change_quantity_in_database(idUbah,jumlahUbah,array):
    # melakukan skema pengubahan jumlah barang pada array _consumable atau _gadget
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of integer,string { array yang mau diproses }
            # baris : array of integer, string { untuk pencarian baris dengan id yang mau diubah jumlah itemnya }
    # ALGORITMA
    arrayProcess = array
    # mengubah jumlah item yang mau diubah
    for baris in arrayProcess:
        if baris[0] == idUbah:
            baris[3] = int(baris[3])
            baris[3] += jumlahUbah
            baris[3] = str(baris[3])
    return arrayProcess

# ALGORITMA UTAMA
def ubahJumlah(_consumable,_gadget):
    # skema pengubahan jumlah suatu item pada database
    clear_screen()
    print(">>> Mengubah Jumlah Gadget atau Consumable")
    idUbah = input("Masukkan ID: ").upper()

    if idUbah[0] == 'C':
        arrayProcess = _consumable
    elif idUbah[0] == 'G':
        arrayProcess = _gadget
    else:
        arrayProcess = []

    # melakukan pemeriksaan validitas input
    if (isIDinDatabase(idUbah,arrayProcess)):
        jumlahUbah = int(input("Masukkan jumlah: "))
        if (jumlahUbah + int(infoBarang(idUbah,'jumlah',_consumable,_gadget)) >= 0):
            kondisiLanjut = True
        else:
            print(f"\n{(-1)*jumlahUbah} {infoBarang(idUbah,'nama',_consumable,_gadget)} gagal dibuang karena stok kurang. Stok sekarang: {infoBarang(idUbah,'jumlah',_consumable,_gadget)} (<{(-1)*jumlahUbah})")
            kondisiLanjut = False
    else:
        print("\nTidak ada item dengan ID tersebut!")
        kondisiLanjut = False

    # melakukan overwrite perubahan data ke file csv
    if kondisiLanjut:
        if idUbah[0] == "C":
            _consumable = change_quantity_in_database(idUbah,jumlahUbah,_consumable)
        elif idUbah[0] == "G":
            _gadget = change_quantity_in_database(idUbah,jumlahUbah,_gadget)
        if (jumlahUbah >= 0):
            print(f"\n{jumlahUbah} {infoBarang(idUbah,'nama',_consumable,_gadget)} berhasil ditambahkan. Stok sekarang: {infoBarang(idUbah,'jumlah',_consumable,_gadget)}")
        else:
            print(f"\n{(-1)*jumlahUbah} {infoBarang(idUbah,'nama',_consumable,_gadget)} berhasil dibuang. Stok sekarang: {infoBarang(idUbah,'jumlah',_consumable,_gadget)}")
    print("")
    os.system('pause')