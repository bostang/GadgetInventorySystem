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
def isIDinDatabase(id,database):
    # memeriksa apakah ID item ada di suatu array database apa tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if id == element[0]: # lokasi id ada di kolom pertama
            return True
    return False

def convert_to_real(code):
    # mengonversi data suatu array database supaya bisa dimanipulasi nilainya
    # KAMUS LOKAL
        # Variabel
            # array_salinan : array of array of integer,string
            # kol_jumlah : integer { nomor kolom 'jumlah' }
            # baris : array of string,integer { baris pada array database yang mau diolah }
    # ALGORITMA
    kol_jumlah = 3
    if code == 'C':
        arrayProcess = _consumable
    elif code == 'G':
        arrayProcess = _gadget
    else:
        arrayProcess = []
    array_salinan = arrayProcess[:] # menyalin array untuk diproses lebih lanjut

        # melakukan type casting ke integer
    for baris in array_salinan:
        if baris[3] == 'jumlah': # men-skip kolom pertama ( header )
            continue
        else:
            baris[3] = int(baris[3])
    return array_salinan

def convert_datas_to_string_ubahJumlah(code):
    # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
    # KAMUS LOKAL
        # Variabel
            # arr_data : array { array yang merupakan elemen _gadget atau _consumable }
            # arr_data_all_string : array of string { untuk skema konversi array database menjadi string }
            # arrayProcess : array of array of string { array yang ingin diproses }
            # string_data : string { untain informasi dari database [lokal] }
    # ALGORITMA
    if code == 'C':
        arrayProcess = _consumable
    elif code == 'G':
        arrayProcess = _gadget

    string_data = ""
    for arr_data in arrayProcess:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"

    return string_data

def overwrite_database(code):
    # melakukan overwrite terhadap konten database [digunakan dalam skema penggantian jumlah item pada csv]
    # KAMUS LOKAL
        # datas_as_string : string { untain informasi dari database [lokal] }
        # f : textIOWrapper
    # ALGORITMA
    datas_as_string = convert_datas_to_string_ubahJumlah(idUbah[0])
    if code == 'C':
        f = open("consumable.csv","w")
    elif code == 'G':
        f = open("gadget.csv","w")
    f.write(datas_as_string) # melakukan overwrite terhadap isi database
    f.close()

def change_quantity_in_database(idUbah, jumlahUbah,code):
    # melakukan skema pengubahan jumlah barang pada array _consumable atau _gadget
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of integer,string { array yang mau diproses }
            # baris : array of integer, string { untuk pencarian baris dengan id yang mau diubah jumlah itemnya }
    # ALGORITMA
    arrayProcess = convert_to_real(code)
    # mengubah jumlah item yang mau diubah
    for baris in arrayProcess:
        if baris[0] == idUbah:
            baris[3] += jumlahUbah
    return arrayProcess

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
        return "barang tidak ditemukan di database"

# ALGORITMA UTAMA
def ubahJumlah(_consumable,_gadget):
    # skema pengubahan jumlah suatu item pada database
    clear_screen()
    print(">>> Mengubah Jumlah Gadget atau Consumable")
    idUbah = input("Masukkan ID: ")

    if idUbah[0] == 'C':
        arrayProcess = _consumable
    elif idUbah[0] == 'G':
        arrayProcess = _gadget
    else:
        arrayProcess = []

    # melakukan pemeriksaan validitas input
    if (isIDinDatabase(idUbah,arrayProcess)):
        jumlahUbah = int(input("Masukkan jumlah: "))
        if (jumlahUbah + int(infoBarang(idUbah,'jumlah')) >= 0):
            kondisiLanjut = True
        else:
            print(f"\n{(-1)*jumlahUbah} {infoBarang(idUbah,'nama')} gagal dibuang karena stok kurang. Stok sekarang: {infoBarang(idUbah,'jumlah')} (<{(-1)*jumlahUbah})")
            kondisiLanjut = False
    else:
        print("\nTidak ada item dengan ID tersebut!")
        kondisiLanjut = False

    # melakukan overwrite perubahan data ke file csv
    if kondisiLanjut:
        hasilUbah = change_quantity_in_database(idUbah,jumlahUbah,idUbah[0])
        overwrite_database(idUbah[0])
        if (jumlahUbah >= 0):
            print(f"\n{jumlahUbah} {infoBarang(idUbah,'nama')} berhasil ditambahkan. Stok sekarang: {infoBarang(idUbah,'jumlah')}")
        else:
            print(f"\n{(-1)*jumlahUbah} {infoBarang(idUbah,'nama')} berhasil dibuang. Stok sekarang: {infoBarang(idUbah,'jumlah')}")
    print("")
    os.system('pause')