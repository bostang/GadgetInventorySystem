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

# KAMUS
    # Variabel
        # array_of_data : array of string { array sementara untuk menambah data dari file csv ke array database }
        # g : textIOWrapper
        # raw_lines_g : array of character { array sementara berisi data gadget [banyak \n ] }
        # lines_g : array of character { array sementara sebelum mebuat _gadget }
        # _gadget : array database gadget.csv
        # tahun : integer { tahun ditemukannya item yang mau dicari }
        # kategori : string { untuk memperjelas pencarian berdasarkan tahun ditemukan }
    # Fungsi/Prosedur
        # function clear_screen
            # membuat efek clear screen pada Python
        # function isTahuninDatabase(tahun_ditemukan : integer, kategori : string, database: array of array of string) -> boolean
            # mengecek apakah tahun yang diinginkan ada di database atau tidak, sesuai dengan kategori
        # procedure convert_line_to_data(input line: string)
            # menulis data per baris dalam csv ke dalam bentuk array
            # I.S. belum ada array database ; F.S. array database sudah bisa digunakan
        # function infoBarang(id : string ,spek : string) -> string / integer
            # mendapatkan informasi barang dari database

# REALISASI FUNGSI/PROSEDUR
def clear_screen():
    # membuat efek clear screen pada Python
    os.system('cls' if os.name == 'nt' else 'clear')

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

def splitList(database):
    # menulis data per baris dalam csv ke dalam bentuk array
    # KAMUS LOKAL
        # Variabel
            # database : array of string { array sementara [masih kotor oleh \n] }
            # aplit_list : array of string { array hasil berisi data-data dari csv}
    # ALGORITMA
    database = ''.join(line)
    split_list = []
    tmp = ''
    for s in database:
        if s == ';':
            split_list.append(tmp)
            tmp = ''
        else:
            tmp += s
    if tmp:
        split_list.append(tmp)
    return split_list

def infoBarang(tahun_ditemukan,kategori,spek):
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

# ALGORITMA UTAMA

# membaca file database .csv
g = open("gadget.csv","r")
raw_lines_g = g.readlines()
g.close()
lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]

# mengakses database dalam bentuk array
_gadget = []
for line in lines_g:
    array_of_data = splitList(line)
    _gadget.append(array_of_data)

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
                print(f"\nNama            : {infoBarang(tahun,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun,kategori,'tahun_ditemukan')}")
        elif (kategori == '>'):
            if int(baris[5]) >= tahun+1: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun,kategori,'tahun_ditemukan')}")        
        elif (kategori == '<'):
            if int(baris[5]) <= tahun-1: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun,kategori,'tahun_ditemukan')}")            
        elif (kategori == '>='):
            if int(baris[5]) >= tahun: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun,kategori,'tahun_ditemukan')}")        
        elif (kategori == '<='):
            if int(baris[5]) <= tahun: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun,kategori,'tahun_ditemukan')}")

    print("\nSemua data telah ditampilkan")
            
else:
    print("\nTidak ada gadget yang ditemukan")

print('')
os.system('pause')