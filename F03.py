"""
Pencari gadget berdasarkan rarity
Akses: Admin, User

Pengguna dapat mencari gadget dengan rarity tertentu. Pengguna akan memasukkan 
rarity(C,B,A,S), kemudian aplikasi akan menampilkan Gadget dengan rarity tersebut.

Catatan: Jenis rarity yang di input pasti valid(C,B,A,S).

Desainer : 
1. Muhammad Daris Nurhakim (16520170)
2. 

Coder :
1. Muhammad Daris Nurhakim (16520170)
2. 

Tester :
1.
2.

Tentang cariRarity:
1. Sudah berjalan dengan baik
2. Masih menggunakan .split()
3. Belum di cek saat bergabung dengan semua fungsi

"""

# mengimport file dari Python
import os

def clear_screen():
    # fungsi ini digunakan untuk membuat efek clear screen pada Python
    os.system('cls' if os.name == 'nt' else 'clear')

def isRarityinDatabase(rarity,database):
    # fungsi ini digunakan untuk mengecek apakah rarity yang diinginkan ada di database atau tidak
    for element in database:
        if rarity == element[4]: # element[4] berisi rarity yang ada di database
            return True
    return False

def convert_line_to_data(line):
    # fungsi ini digunakan menulis data per baris dalam csv ke dalam bentuk array
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def infoBarang(rarity,spek):
    # fungsi ini digunakan untuk mendapatkan informasi mengenai barang yang ada di database
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

'''''''''''
'ALGORITMA'
'''''''''''
# membaca file database .csv
g = open("gadget.csv","r")
raw_lines_g = g.readlines()
g.close()
lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]

# mengakses database dalam bentuk array
_gadget = []
for line in lines_g:
    array_of_data = convert_line_to_data(line)
    _gadget.append(array_of_data)

# Melakukan skema pencarian berdasarkan rarity
clear_screen()
database = _gadget
print(">>> Pencarian Gadget berdasarkan rarity\n")
rarity = input("Masukkan rarity: ")

# jika inputan salah, maka akan diulang
while (rarity != 'S') and (rarity != 'A') and (rarity != 'B') and (rarity != 'C'):
    print("\nMasukan Anda salah!\n")
    rarity = input("Masukkan rarity: ")

print("\nHasil pencarian:")
# mengecek apakah rarity ada di database atau tidak
if isRarityinDatabase(rarity,database): 
    for baris in database:
        if baris[4] == rarity: # baris[4] berisi data tentang rarity
            print(f"\nNama            : {infoBarang(rarity,'nama')}")
            print(f"Deskripsi       : {infoBarang(rarity,'deskripsi')}")
            print(f"Jumlah          : {infoBarang(rarity,'jumlah')}")
            print(f"Rarity          : {infoBarang(rarity,'rarity')}")
            print(f"Tahun ditemukan : {infoBarang(rarity,'tahun_ditemukan')}")

    print("\nSemua data telah ditampilkan")
            
else:
    print("\nTidak ada")

print('')
os.system('pause')