import os
import sys
import argparse
import datetime
import time

def bersih():
    os.system('cls' if os.name == 'nt' else 'clear')

def infoAkun(spek):
    # mendapatkan informasi barang dari database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    for baris in _user:
        # return informasi
        if spek == 'username':
            return baris[1]
        elif spek == 'nama':
            return baris[2]
        elif spek == 'alamat':
            return baris[3]
        elif spek == 'password':
            return baris[4]
        elif spek == 'rule':
            return baris[5]

def menu_awal():
    bersih()
    print("-----------------------------------")
    print("  Selamat datang di Kantong Ajaib  ")
    print("-----------------------------------")
    print("[1] Login")
    print("[2] Register")
    print("[3] Exit\n")   

    while True:
        try:
            pilihan = int(input("Masukan pilihan: "))
            while (pilihan < 1) or (pilihan > 3):
                print("\nMasukan Anda salah!\n")
                pilihan = int(input("Masukan pilihan: "))
            break
        except ValueError:
            print("\nMasukan pilihan dalam bentuk angka!\n")
    
    return pilihan
        
def menu_user():
    clear_screen()
    print("Daftar Menu:")
    print("[1] Pencarian gadget berdasarkan rarity")
    print("[2] Pencarian gadget berdasarkan tahun ditemukan")
    print("[3] Meminjam gadget")
    print("[4] Mengembalikan gadget")
    print("[5] Meminta consumable")
    print("[6] Save data")
    print("[7] Petunjuk")
    print("[0] Keluar")

    pilihan = int(input("Silahkan pilih menu: "))
    while (pilihan < 0) or (pilihan > 7):
        print("Masukan Anda salah! Ulangi")
        pilihan = input("Silahkan pilih menu: ")
    else:
        if (pilihan == 1):
            #cariRarity
        elif (pilihan == 2):
            #cariTahun
        elif (pilihan == 3):
            #pinjam
        elif (pilihan == 4):
            #kembali
        elif (pilihan == 5):
            #minta
        elif (pilihan == 6):
            #save
        elif (pilihan == 7):
            #petunjuk
        else:
            #exit

def menu_admin():
    clear_screen()
    print("Daftar Menu:")
    print("[1] Pencarian gadget berdasarkan rarity")
    print("[2] Pencarian gadget berdasarkan tahun ditemukan")
    print("[3] Menambah item")
    print("[4] Menghapus gadget atau consumable")
    print("[5] Mengubah jumlah gadget atau consumable pada inventory")
    print("[6] Melihat riwayat peminjaman gadget")
    print("[7] Melihat riwayat pengembalian gadget")
    print("[8] Melihat riwayat pengambilan consumable")
    print("[9] Save data")
    print("[10]Petunjuk")
    print("[0] Keluar")

    pilihan = int(input("Silahkan pilih menu: "))
    while (pilihan < 0) or (pilihan > 10):
        print("Masukan Anda salah! Ulangi")
        pilihan = input("Silahkan pilih menu: ")
    else:
        if (pilihan == 1):
            #cariRarity
        elif (pilihan == 2):
            #cariTahun
        elif (pilihan == 3):
            from F05 import * # menjalankan fungsi tambahItem
        elif (pilihan == 4):
            from F06 import * # menjalankan fungsi hapusItem
        elif (pilihan == 5):
            from F07 import * # menjalankan fungsi ubahJumlah
        elif (pilihan == 6):
            #riwayatPinjam
        elif (pilihan == 7):
            #riwayatKembali
        elif (pilihan == 8):
            #riwayatAmbil
        elif (pilihan == 9):
            #save
        elif (pilihan == 10):
            #petunjuk
        else:
            #exit

pilihan = menu_awal()
if (pilihan == 1):
    print("")
    os.system("pause")
    print("")
    bersih()
    #login()
elif (pilihan == 2):
    print("")
    os.system("pause")
    print("")
    bersih()
    from F01 import * # menjalankan fungsi registrasi
else: # pilihan == 3
    os.system("cls")

# mengecek rule akun
if ({infoAkun('rule')} == 'admin'):
    menu_admin()
else:
    menu_user()