"""
Pencari gadget berdasarkan tahun ditemukan 
Akses: Admin, User

Pengguna dan admin dapat melakukan pencarian gadget berdasarkan tahun ditemukan. 
Pengguna memasukkan sebuah tahun, misalnya yyyy, dan kategori pencarian yaitu: [=,<,>,>=,<=].
Penjelasan dari setiap kategori adalah sebagai berikut:
☑ = artinya gadget yang terbit pada tahun yyyy.
☑ > artinya gadget yang terbit setelah tahun yyyy.
☑ < artinya gadget yang terbit sebelum tahun yyyy.
☑ >= artinya gadget yang terbit pada atau setelah tahun yyyy.
☑ <= artinya gadget yang terbit sebelum atau pada tahun yyyy.

Catatan: Format tanggal dan jenis kategori yang diinput pasti valid

Kontributor : Muhammad Daris Nurhakim [16520170], Diffa' Shada 'Aqila [16520070]

"""

# mengimport file dari Python
import os
from Basic_Procedure import *

# KAMUS
    # Variabel
        # _gadget : array database gadget.csv
        # tahun : integer { tahun ditemukannya item yang mau dicari }
        # kategori : string { untuk memperjelas pencarian berdasarkan tahun ditemukan }
    # Fungsi/Prosedur
        # function isTahuninDatabase(tahun_ditemukan : integer, kategori : string, database: array of array of string) -> boolean
            # mengecek apakah tahun yang diinginkan ada di database atau tidak, sesuai dengan kategori
        # function infoBarang_tahun(id : string ,spek : string) -> string / integer
            # mendapatkan informasi barang dari database

# REALISASI FUNGSI/PROSEDUR
def isTahuninDatabase(tahun_ditemukan,kategori,database):
    # mengecek apakah tahun yang diinginkan ada di database atau tidak, sesuai dengan kategori
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database[1:]: # database dimulai pada baris ke 1(header tidak dihitung)
        if (kategori == '='):
            if tahun_ditemukan == int(element[5]): # element[5] berisi data tahun_ditemukan
                return True
        elif (kategori == '>'):
            if tahun_ditemukan-1 <= int(element[5]): # element[5] berisi data tahun_ditemukan
                return True
        elif (kategori == '<'):
            if tahun_ditemukan+1 >= int(element[5]): # element[5] berisi data tahun_ditemukan
                return True
        elif (kategori == '>='):
            if tahun_ditemukan <= int(element[5]): # element[5] berisi data tahun_ditemukan
                return True
        elif (kategori == '<='):
            if tahun_ditemukan >= int(element[5]): # element[5] berisi data tahun_ditemukan
                return True
    return False

def infoBarang_tahun(tahun_ditemukan,kategori,spek,_gadget,baris):
    # mendapatkan informasi mengenai barang yang ada di database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    if (kategori == '=') or (kategori == '>') or (kategori == '<') or (kategori == '>=') or (kategori == '<=') and (tahun_ditemukan > 0):
        arrayProcess = _gadget
    else:
        arrayProcess = []
    
    # mengecek apakah tahun yang diinginkan ada di database atau tidak, sesuai dengan kategori
    if isTahuninDatabase(tahun_ditemukan,kategori,arrayProcess):
        # mengecek baris per baris
        i = 0
        while arrayProcess[i]:
            if spek == 'id':
                return baris[0]
            elif spek == 'nama':
                return baris[1]
            elif spek == 'deskripsi':
                return baris[2]
            elif spek == 'jumlah':
                return baris[3]
            elif spek == 'rarity':
                return baris[4]
            elif spek == 'tahun_ditemukan':
                return baris[5]
            i += 1           
    else:
        return "\nbarang tidak ditemukan di database"

def hasil_pencarian(tahun,kategori,_gadget,baris):
    # untuk menghasilkan hasil pencarian
    print(f"\nNama            : {infoBarang_tahun(tahun,kategori,'nama',_gadget,baris)}")
    print(f"Deskripsi       : {infoBarang_tahun(tahun,kategori,'deskripsi',_gadget,baris)}")
    print(f"Jumlah          : {infoBarang_tahun(tahun,kategori,'jumlah',_gadget,baris)}")
    print(f"Rarity          : {infoBarang_tahun(tahun,kategori,'rarity',_gadget,baris)}")
    print(f"Tahun ditemukan : {infoBarang_tahun(tahun,kategori,'tahun_ditemukan',_gadget,baris)}")

# ALGORITMA UTAMA
def cariTahun(_gadget):
    # Melakukan skema pencarian berdasarkan tahun_ditemukan dan kategori
    clear_screen()
    database = _gadget
    print(">>> Pencarian Gadget berdasarkan rarity\n")
    # untuk memastikan bahwa tahun yang di input dalam integer, jika tidak bertipe integer maka akan meminta input ulang
    while True:
        try:
            tahun = int(input("Masukkan tahun: "))
            break
        except ValueError:
            print("\nMasukan tahun dalam bentuk angka!\n")
    kategori = input("Masukkan kategori: ")
    # mengecek kategori, jika tidak valid maka akan diminta input ulang
    while (kategori != '=') and (kategori != '>') and (kategori != '<') and (kategori != '>=') and (kategori != '<='):
        print("Kategori salah!")
        kategori = input("Masukkan kategori: ")
    print("\nHasil pencarian:")
    # mengecek apakah tahun ada di database atau tidak, sesuai kategori
    if isTahuninDatabase(tahun,kategori,database): 
        for baris in database[1:]: # database dimulai pada baris ke 1(header tidak dihitung)
            if (kategori == '='):
                if int(baris[5]) == tahun: # baris[5] berisi data tentang tahun_ditemukan
                    hasil_pencarian(tahun,kategori,_gadget,baris)
            elif (kategori == '>'):
                if int(baris[5]) >= tahun+1: # baris[5] berisi data tentang tahun_ditemukan
                    hasil_pencarian(tahun,kategori,_gadget,baris)    
            elif (kategori == '<'):
                if int(baris[5]) <= tahun-1: # baris[5] berisi data tentang tahun_ditemukan
                    hasil_pencarian(tahun,kategori,_gadget,baris)           
            elif (kategori == '>='):
                if int(baris[5]) >= tahun: # baris[5] berisi data tentang tahun_ditemukan
                    hasil_pencarian(tahun,kategori,_gadget,baris)       
            elif (kategori == '<='):
                if int(baris[5]) <= tahun: # baris[5] berisi data tentang tahun_ditemukan
                    hasil_pencarian(tahun,kategori,_gadget,baris)
        print("\nSemua data telah ditampilkan")
    else:
        print("\nTidak ada gadget yang ditemukan")
    print('')
    os.system('pause')