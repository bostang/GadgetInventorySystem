"""
Melihat Riwayat Peminjaman Gadget
Akses: Admin

Prosedur ini digunakan oleh Admin sebagai bantuan untuk melihat riwayat peminjaman gadget.
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
        # idPeminjam : string { id user yang meminjam barang }
        # idGadget : string { id barang yang dipinjam }
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
        # function infoPinjam(string, stiring) -> string
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

def infoUser(id_pinjam,spek):
    # mendapatkan informasi user (nama atau id saja) dari database
    # KAMUS LOKAL
        # Variabel
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _user
    # mengecek baris per baris
    for baris in arrayProcess[1:]:
        if id_pinjam == baris[0]:
        # me-return informasi
            if spek == 'id':
                return baris[0]
            elif spek == 'nama':
                return baris[2]
    else:
        return "user tidak ada pada database."

def infoBarang(id_pinjam,spek):
    # mendapatkan informasi mengenai barang yang ada di database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _gadget
    # mengecek baris per baris
    for baris in arrayProcess[1:]:
        if id_pinjam == baris[0]:
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
    else:
        return "\nbarang tidak ditemukan di database"

def infoPinjam(spek):
    # mendapatkan informasi mengenai barang yang dipinjam
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _gadgetBorrowHistory
    # mengecek baris per baris
    i = 0
    while arrayProcess[i]:
        if spek == 'id':
            return baris[0]
        elif spek == 'id_peminjam':
            return baris[1]
        elif spek == 'id_gadget':
            return baris[2]
        elif spek == 'tanggal_peminjaman':
            return baris[3]
        elif spek == 'jumlah_pinjam':
            return baris[4]          
        i += 1
    else:
        return "\nbarang tidak ditemukan di database"

# ALGORITMA UTAMA

# membaca file database .csv
g = open("gadget.csv","r")
u = open("user.csv","r")
gb = open("gadget_borrow_history.csv","r")

raw_lines_g = g.readlines()
raw_lines_u = u.readlines()
raw_lines_gb = gb.readlines()

g.close()
u.close()
gb.close()

lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]
lines_u = [raw_line.replace("\n", "") for raw_line in raw_lines_u]
lines_gb = [raw_line.replace("\n", "") for raw_line in raw_lines_gb]

# mengakses database dalam bentuk array
_gadget = []
_user = []
_gadgetBorrowHistory = []

for line in lines_g:
    array_of_data = splitList(line)
    _gadget.append(array_of_data)
for line in lines_u:
    array_of_data = splitList(line)
    _user.append(array_of_data)
for line in lines_gb:
    array_of_data = splitList(line)
    _gadgetBorrowHistory.append(array_of_data)

clear_screen()

# melakukan skema untuk melihat riwayat peminjaman barang
print(">>> Riwayat Kembali")
database = _gadgetBorrowHistory
if (len(database) < 6):
    m = 1    
else: 
    m = len(database) - 5
n = len(database)
for baris in reversed(database[m:n]):
    print(f"\nID Peminjaman       : {infoPinjam('id')}")
    idPeminjam = infoPinjam('id_peminjam')
    if isUserinDatabase(idPeminjam,_user) and infoUser(idPeminjam,'id'):
        print(f"Nama Pengambil      : {infoUser(idPeminjam,'nama')}")
    idGadget = infoPinjam('id_gadget')
    if isIDinDatabase(idGadget,_gadget) and infoBarang(idGadget,'id'):
        print(f"Nama Gadget         : {infoBarang(idGadget,'nama')}")
    print(f"Tanggal Peminjaman  : {infoPinjam('tanggal_peminjaman')}")
    print(f"Jumlah              : {infoPinjam('jumlah_pinjam')}")

while (m > 1):
    lanjut = input("\nApakah Anda mau ke halaman selanjutnya?(Y/N)")
    while (lanjut != 'Y') and (lanjut != 'y') and (lanjut != 'N') and (lanjut != 'n'):
        print("Masukan Anda salah!")
        lanjut = input("\nApakah Anda mau ke halaman selanjutnya?(Y/N)")
    if (lanjut == 'Y') or (lanjut == 'y'):
        if (m > 6):
            m -= 5
        else:
            m = 1
        n -= 5
        for baris in reversed(database[m:n]):
            bersih()
            print(">>> Riwayat Kembali")
            print(f"\nID Peminjaman       : {infoPinjam('id')}")
        idPeminjam = infoPinjam('id_peminjam')
        if isUserinDatabase(idPeminjam,_user) and infoUser(idPeminjam,'id'):
            print(f"Nama Pengambil      : {infoUser(idPeminjam,'nama')}")
        idGadget = infoPinjam('id_gadget')
        if isIDinDatabase(idGadget,_gadget) and infoBarang(idGadget,'id'):
            print(f"Nama Gadget         : {infoBarang(idGadget,'nama')}")
        print(f"Tanggal Peminjaman  : {infoPinjam('tanggal_peminjaman')}")
        print(f"Jumlah              : {infoPinjam('jumlah_pinjam')}")
    else:
        break
else:
    print("\nSemua riwayat sudah ditampilkan")
print("")
os.system('pause')