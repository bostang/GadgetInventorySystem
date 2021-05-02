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

def infoUser(id_pinjam,spek,_user,baris):
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

def infoBarang(id_pinjam,spek,_gadget,baris):
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

def infoPinjam(spek,_gadgetBorrow,baris):
    # mendapatkan informasi mengenai barang yang dipinjam
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _gadgetBorrow
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
# melakukan skema untuk melihat riwayat peminjaman barang
def riwayatPinjam(_gadget,_gadgetBorrow,_user):
    print(">>> Riwayat Pinjam")
    database = _gadgetBorrow
    if (len(database) < 6):
        m = 1    
    else: 
        m = len(database) - 5
    n = len(database)
    for baris in reversed(database[m:n]):
        print(f"\nID Peminjaman       : {infoPinjam('id',_gadgetBorrow,baris)}")
        idPeminjam = infoPinjam('id_peminjam',_gadgetBorrow,baris)
        if isUserinDatabase(idPeminjam,_user) and infoUser(idPeminjam,'id',_user,baris):
            print(f"Nama Pengambil      : {infoUser(idPeminjam,'nama',_user,baris)}")
        idGadget = infoPinjam('id_gadget',_gadgetBorrow,baris)
        if isIDinDatabase(idGadget,_gadget) and infoBarang(idGadget,'id',_gadget,baris):
            print(f"Nama Gadget         : {infoBarang(idGadget,'nama',_gadget,baris)}")
        print(f"Tanggal Peminjaman  : {infoPinjam('tanggal_peminjaman',_gadgetBorrow,baris)}")
        print(f"Jumlah              : {infoPinjam('jumlah_pinjam',_gadgetBorrow,baris)}")

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
                clear_screen()
                print(">>> Riwayat Pinjam")
                print(f"\nID Peminjaman       : {infoPinjam('id',_gadgetBorrow,baris)}")
            idPeminjam = infoPinjam('id_peminjam',_gadgetBorrow,baris)
            if isUserinDatabase(idPeminjam,_user) and infoUser(idPeminjam,'id',_user,baris):
                print(f"Nama Pengambil      : {infoUser(idPeminjam,'nama',_user,baris)}")
            idGadget = infoPinjam('id_gadget',_gadgetBorrow,baris)
            if isIDinDatabase(idGadget,_gadget) and infoBarang(idGadget,'id',_gadget,baris):
                print(f"Nama Gadget         : {infoBarang(idGadget,'nama',_gadget,baris)}")
                print(f"Tanggal Peminjaman  : {infoPinjam('tanggal_peminjaman',_gadgetBorrow,baris)}")
                print(f"Jumlah              : {infoPinjam('jumlah_pinjam',_gadgetBorrow,baris)}")

        else:
            break
    else:
        print("\nSemua riwayat sudah ditampilkan\n")
        os.system("pause")