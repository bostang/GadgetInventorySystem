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

def isTahuninDatabase(tahun_ditemukan,kategori,database):
    # fungsi ini digunakan untuk mengecek apakah tahun yang diinginkan ada di database atau tidak, sesuai dengan kategori
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

def convert_line_to_data(line):
    # fungsi ini digunakan menulis data per baris dalam csv ke dalam bentuk array
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def infoBarang(tahun_ditemukan,kategori,spek):
    # fungsi ini digunakan untuk mendapatkan informasi mengenai barang yang ada di database
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

# Melakukan skema pencarian berdasarkan tahun_ditemukan dan kategori
clear_screen()
database = _gadget
print(">>> Pencarian Gadget berdasarkan rarity\n")

# untuk memastikan bahwa tahun yang di input dalam integer, jika tidak bertipe integer maka akan meminta input ulang
while True:
    try:
        tahun_ditemukan = int(input("Masukkan tahun: "))
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
if isTahuninDatabase(tahun_ditemukan,kategori,database): 
    for baris in database[1:]: # database dimulai pada baris ke 1(header tidak dihitung)
        if (kategori == '='):
            if int(baris[5]) == tahun_ditemukan: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")

        elif (kategori == '>'):
            if int(baris[5]) >= tahun_ditemukan+1: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")
        
        elif (kategori == '<'):
            if int(baris[5]) <= tahun_ditemukan-1: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")
            
        elif (kategori == '>='):
            if int(baris[5]) >= tahun_ditemukan: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")
        
        elif (kategori == '<='):
            if int(baris[5]) <= tahun_ditemukan: # baris[5] berisi data tentang tahun_ditemukan
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")

    print("\nSemua data telah ditampilkan")
            
else:
    print("\nTidak ada gadget yang ditemukan")

print('')
os.system('pause')