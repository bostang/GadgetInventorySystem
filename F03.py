"""
Pencari gadget berdasarkan rarity
Akses: Admin, User

Pengguna dapat mencari gadget dengan rarity tertentu. Pengguna akan memasukkan 
rarity(C,B,A,S), kemudian aplikasi akan menampilkan Gadget dengan rarity tersebut.

Catatan: Jenis rarity yang di input pasti valid(C,B,A,S).

Kontributor : Muhammad Daris Nurhakim [16520170], Diffa' Shada 'Aqila [16520070]

"""

# mengimport file dari Python
import os
from Basic_Procedure import *

# KAMUS
    # Variabel
        # _gadget : array database gadget.csv
        # rarityItem : string { rarity item yang mau dicari }
    # Fungsi/Prosedur
        # function isRarityinDatabase(rarity : string, database: array of array of string) -> boolean
            # memeriksa apakah rarity barang sudah ada di database atau belum
        # function infoBarang_rarity(id : string ,spek : string) -> string / integer
            # mendapatkan informasi barang dari database


# REALISASI FUNGSI/PROSEDUR
def isRarityinDatabase(rarity,database):
    # mengecek apakah rarity yang diinginkan ada di database atau tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if rarity == element[4]: # element[4] berisi rarity yang ada di database
            return True
    return False

def infoBarang_rarity(rarity,spek,_gadget,baris):
    # mendapatkan informasi mengenai barang yang ada di database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    if (rarity == 'S') or (rarity == 'A') or (rarity == 'B') or (rarity == 'C'): # jika rarity valid
        arrayProcess = _gadget
    else:
        arrayProcess = []
    
    # mengecek apakah rarity yang diinginkan ada di database atau tidak
    if isRarityinDatabase(rarity,arrayProcess):
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


# ALGORITMA UTAMA
def cariRarity(_gadget):
    # melakukan skema pencarian berdasarkan rarity
    clear_screen()
    database = _gadget
    print(">>> Pencarian Gadget berdasarkan rarity\n")
    rarityItem = input("Masukkan rarity: ").upper()

    # jika inputan salah, maka akan diulang
    while (rarityItem != 'S') and (rarityItem != 'A') and (rarityItem != 'B') and (rarityItem != 'C'):
        print("\nMasukan Anda salah!\n")
        rarityItem = input("Masukkan rarity: ").upper()
    
    print("\nHasil pencarian:")
    # mengecek apakah rarity ada di database atau tidak
    if isRarityinDatabase(rarityItem,database): 
        for baris in database:
            if baris[4] == rarityItem: # baris[4] berisi data tentang rarity
                print(f"\nNama            : {infoBarang_rarity(rarityItem,'nama',_gadget,baris)}")
                print(f"Deskripsi       : {infoBarang_rarity(rarityItem,'deskripsi',_gadget,baris)}")
                print(f"Jumlah          : {infoBarang_rarity(rarityItem,'jumlah',_gadget,baris)}")
                print(f"Rarity          : {infoBarang_rarity(rarityItem,'rarity',_gadget,baris)}")
                print(f"Tahun ditemukan : {infoBarang_rarity(rarityItem,'tahun_ditemukan',_gadget,baris)}")
        print("\nSemua data telah ditampilkan")            
    else:
        print("\nTidak ada")

    print('')
    os.system('pause')