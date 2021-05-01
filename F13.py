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
        # function bersih
            # membuat efek clear screen pada Python
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

def infoUser(id_ambil,spek):
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

def infoBarang(id_ambil,spek):
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

def infoAmbil(spek):
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

# membaca file database .csv
c = open("consumable.csv","r")
u = open("user.csv","r")
ch = open("consumable_history.csv","r")

raw_lines_c = c.readlines()
raw_lines_u = u.readlines()
raw_lines_ch = ch.readlines()

c.close()
u.close()
ch.close()

lines_c = [raw_line.replace("\n", "") for raw_line in raw_lines_c]
lines_u = [raw_line.replace("\n", "") for raw_line in raw_lines_u]
lines_ch = [raw_line.replace("\n", "") for raw_line in raw_lines_ch]

# mengakses database dalam bentuk array
_consumable = []
_user = []
_consumableHistory = []

for line in lines_c:
    array_of_data = splitList(line)
    _consumable.append(array_of_data)
for line in lines_u:
    array_of_data = splitList(line)
    _user.append(array_of_data)
for line in lines_ch:
    array_of_data = splitList(line)
    _consumableHistory.append(array_of_data)

clear_screen()

# melakukan skema untuk melihat riwayat peminjaman barang
print(">>> Riwayat Kembali")
database = _consumableHistory
if (len(database) < 6):
    m = 1    
else: 
    m = len(database) - 5
n = len(database)
for baris in reversed(database[m:n]):
    print(f"\nID Pengambilan      : {infoAmbil('id')}")
    idPengambil = infoAmbil('id_pengambil')
    if isUserinDatabase(idPengambil,_user) and infoUser(idPengambil,'id'):
        print(f"Nama Pengambil      : {infoUser(idPengambil,'nama')}")
    idConsumable = infoAmbil('id_consumable')
    if isIDinDatabase(idConsumable,_consumable) and infoBarang(idConsumable,'id'):
        print(f"Nama Consumable     : {infoBarang(idConsumable,'nama')}")
    print(f"Tanggal Peminjaman  : {infoAmbil('tanggal_pengambilan')}")
    print(f"Jumlah              : {infoAmbil('jumlah')}")

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
        for baris in reversed(database[m:n]):
            print(f"\nID Pengambilan      : {infoAmbil('id')}")
        idPengambil = infoAmbil('id_pengambil')
        if isUserinDatabase(idPengambil,_user) and infoUser(idPengambil,'id'):
            print(f"Nama Pengambil      : {infoUser(idPengambil,'nama')}")
        idConsumable = infoAmbil('id_consumable')
        if isIDinDatabase(idConsumable,_consumable) and infoBarang(idConsumable,'id'):
            print(f"Nama Consumable     : {infoBarang(idConsumable,'nama')}")
        print(f"Tanggal Pengambilan  : {infoAmbil('tanggal_pengambilan')}")
        print(f"Jumlah              : {infoAmbil('jumlah')}")
    else:
        break
else:
    print("\nSemua riwayat sudah ditampilkan")
print("")
os.system('pause')