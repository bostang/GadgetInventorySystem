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
        # array_of_data : array of string { array sementara untuk menambah data dari file csv ke array database }
        # g : textIOWrapper
        # raw_lines_g : array of character { array sementara berisi data gadget [banyak \n ] }
        # lines_g : array of character { array sementara sebelum mebuat _gadget }
        # _gadget : array database gadget.csv
        # rarityItem : string { rarity item yang mau dicari }
    # Fungsi/Prosedur
        # function bersih
            # membuat efek clear screen pada Python
        # procedure splitList
            # menulis data per baris dalam csv ke dalam bentuk array
        # function isRarityinDatabase(rarity : string, database: array of array of string) -> boolean
            # memeriksa apakah rarity barang sudah ada di database atau belum
        # function infoBarang(id : string ,spek : string) -> string / integer
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

def infoBarang(rarity,spek):
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
# membaca file database .csv
g = open("gadget.csv","r")
raw_lines_g = g.readlines()
g.close()
lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]

# mengakses database dalam bentuk array
_gadget = []
for line in lines_g:
    array_of_data = split(line)
    _gadget.append(array_of_data)

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
            print(f"\nNama            : {infoBarang(rarityItem,'nama')}")
            print(f"Deskripsi       : {infoBarang(rarityItem,'deskripsi')}")
            print(f"Jumlah          : {infoBarang(rarityItem,'jumlah')}")
            print(f"Rarity          : {infoBarang(rarityItem,'rarity')}")
            print(f"Tahun ditemukan : {infoBarang(rarityItem,'tahun_ditemukan')}")

    print("\nSemua data telah ditampilkan")            
else:
    print("\nTidak ada")

print('')
os.system('pause')