"""
Melihat Riwayat Pengambilan Consumable
Akses: Admin

Prosedur ini digunakan oleh Admin sebagai bantuan untuk melihat riwayat pengambilan consumable.
Data bisa dibaca dari file yang tersedia. Bila terdapat lebih dari 5 entry. Keluarkan 5 entry
paling baru, dan pengguna dapat mengeluarkan 5 entry tambahan bila diinginkan. Keluaran minimal
memiliki field seperti contoh dan harus sorted descending berdasarkan tanggal.

Kontributor : Muhammad Daris Nurhakim [16520170], Joshi Ryu Setiady [16520230]

"""

# mengimport file dari Python
import os
from Basic_Procedure import *

# KAMUS
    # Variabel
        # idPengambil : string { id user yang meminjam barang }
        # idConsumable : string { id barang yang dipinjam }
        # lanjut : string { kondisi untuk menentukan apakah mengeluarkan 5 entry setelahnya }
    # Fungsi / Prosedur
        # procedure splitList
            # menulis data per baris dalam csv ke dalam bentuk array
        # function isIDinDatabase(string, array of array of string) -> boolean
            # memeriksa apakah ID item ada di suatu array database apa tidak
        # function isUserinDatabase(string, array of array of string) -> boolean
            # memeriksa apakah user ada di array _user apa tidak
        # function infoBarang(id : string ,spek : string) -> string / integer
            # mendapatkan informasi barang dari database
        # function infoUser(string, string) -> string
            # mendapatkan informasi user (nama atau id saja) dari database
        # function infoPinjam(string, string) -> string
            # mendapatkan informasi mengenai barang yang dipinjam

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

def isUserinDatabase(user,database):
    # memeriksa apakah user ada di array _user atau tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if user == element[0]: # lokasi username ada di kolom kedua
            return True
    return False

def infoUser(id_ambil,spek,_user,baris):
    # mendapatkan informasi user (nama atau id saja) dari database
    # KAMUS LOKAL
        # Variabel
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _user
    # mengecek baris per baris
    for baris in arrayProcess[1:]:
        if id_ambil == baris[0]:
        # me-return informasi
            if spek == 'id':
                return baris[0]
            elif spek == 'nama':
                return baris[2]
    else:
        return "user tidak ada pada database."

def infoBarang(id_ambil,spek,_consumable,baris):
    # mendapatkan informasi mengenai barang yang ada di database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _consumable
    # mengecek baris per baris
    for baris in arrayProcess[1:]:
        if id_ambil == baris[0]:
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
    else:
        return "\nbarang tidak ditemukan di database"

def infoAmbil(spek,_consumableHistory,baris):
    # mendapatkan informasi mengenai barang yang diambil
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _consumableHistory
    # mengecek baris per baris
    i = 0
    while arrayProcess[i]:
        if spek == 'id':
            return baris[0]
        elif spek == 'id_pengambil':
            return baris[1]
        elif spek == 'id_consumable':
            return baris[2]
        elif spek == 'tanggal_pengambilan':
            return baris[3]
        elif spek == 'jumlah':
            return baris[4]          
        i += 1
    else:
        return "\nbarang tidak ditemukan di database"

# ALGORITMA UTAMA
# melakukan skema untuk melihat riwayat peminjaman barang
def riwayatMinta(_consumableHistory,_consumable,_user):
    print(">>> Riwayat Ambil")
    database = _consumableHistory
    if (len(database) < 6):
        m = 1    
    else: 
        m = len(database) - 5
    n = len(database)
    for baris in reversed(database[m:n]):
        print(f"\nID Pengambilan      : {infoAmbil('id',_consumableHistory,baris)}")
        idPengambil = infoAmbil('id_pengambil',_consumableHistory,baris)
        if isUserinDatabase(idPengambil,_user) and infoUser(idPengambil,'id',_user,baris):
            print(f"Nama Pengambil      : {infoUser(idPengambil,'nama',_user,baris)}")
        idConsumable = infoAmbil('id_consumable',_consumableHistory,baris)
        if isIDinDatabase(idConsumable,_consumable) and infoBarang(idConsumable,'id',_consumable,baris):
            print(f"Nama Consumable     : {infoBarang(idConsumable,'nama',_consumable,baris)}")
        print(f"Tanggal Peminjaman  : {infoAmbil('tanggal_pengambilan',_consumableHistory,baris)}")
        print(f"Jumlah              : {infoAmbil('jumlah',_consumableHistory,baris)}")

    while (m > 1):
        lanjut = input("\nApakah Anda mau ke halaman selanjutnya?(Y/N)")
        while lanjut not in 'YyNn':
            print("Masukan Anda salah!")
            lanjut = input("\nApakah Anda mau ke halaman selanjutnya?(Y/N)")
        if (lanjut == 'Y') or (lanjut == 'y'):
            if (m > 6):
                m -= 5
            else:
                m = 1
            n -= 5

            clear_screen()

            for baris in reversed(database[m:n]):
                clear_screen()
                print(">>> Riwayat Ambil")
                print(f"\nID Pengambilan      : {infoAmbil('id',_consumableHistory,baris)}")
                idPengambil = infoAmbil('id_pengambil',_consumableHistory,baris)
                if isUserinDatabase(idPengambil,_user) and infoUser(idPengambil,'id',_user,baris):
                    print(f"Nama Pengambil      : {infoUser(idPengambil,'nama',_user,baris)}")
                idConsumable = infoAmbil('id_consumable',_consumableHistory,baris)
                if isIDinDatabase(idConsumable,_consumable) and infoBarang(idConsumable,'id',_consumable,baris):
                    print(f"Nama Consumable     : {infoBarang(idConsumable,'nama',_consumable,baris)}")
                print(f"Tanggal Peminjaman  : {infoAmbil('tanggal_pengambilan',_consumableHistory,baris)}")
                print(f"Jumlah              : {infoAmbil('jumlah',_consumableHistory,baris)}")               
        else:
            break
    else:
        print("\nSemua riwayat sudah ditampilkan\n")
        os.system('pause')