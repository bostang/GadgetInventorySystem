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
        # procedure ubahJumlah(input idUbah : string, jumlahUbah: integer)
            # program utama untuk mengubah jumlah item dalam database
        # procedure change_quantity_in_database(input idUbah : string, jumlahUbah: integer ,code: character)
            # melakukan skema pengubahan jumlah barang pada array _consumable atau _gadget
            # I.S. atribut jumlah salah satu item pada array _consumable atau _gadget belum berubah
            # I.S. atribut jumlah salah satu item pada array _consumable atau _gadget sudah berubah

# REALISASI FUNGSI/PROSEDUR
def infoBarang(id,spek,_consumable,_gadget):
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