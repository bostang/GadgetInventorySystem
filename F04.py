# Program cariTahun

# Kontributor : Muhammad Daris Nurhakim [16520170], ...

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def isTahuninDatabase(tahun_ditemukan,kategori,database):
    for element in database[1:]:
        if (kategori == '='):
            if tahun_ditemukan == int(element[5]):
                return True
        elif (kategori == '>'):
            if tahun_ditemukan > int(element[5]):
                return True
        elif (kategori == '<'):
            if tahun_ditemukan < int(element[5]):
                return True
        elif (kategori == '>='):
            if tahun_ditemukan > int(element[5]):
                return True
        elif (kategori == '<='):
            if tahun_ditemukan > int(element[5]):
                return True
    return False

def convert_line_to_data(line):
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def infoBarang(tahun_ditemukan,kategori,spek):
    if (kategori == '=') or (kategori == '>') or (kategori == '<') or (kategori == '>=') or (kategori == '<=') and (tahun_ditemukan > 0):
        arrayProcess = _gadget
    else:
        arrayProcess = []
    
    if isTahuninDatabase(tahun_ditemukan,kategori,arrayProcess):
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

g = open("gadget.csv","r")
raw_lines_g = g.readlines()
g.close()
lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]

_gadget = []

for line in lines_g:
    array_of_data = convert_line_to_data(line)
    _gadget.append(array_of_data)

clear_screen()
database = _gadget
print(">>> Pencarian Gadget berdasarkan rarity\n")

while True:
    try:
        tahun_ditemukan = int(input("Masukkan tahun: "))
        break
    except ValueError:
        print("\nMasukan tahun dalam bentuk angka!\n")

kategori = input("Masukkan kategori: ")
while (kategori != '=') and (kategori != '>') and (kategori != '<') and (kategori != '>=') and (kategori != '<='):
    print("Kategori salah!")
    kategori = input("Masukkan kategori: ")

print("\nHasil pencarian:")

if isTahuninDatabase(tahun_ditemukan,kategori,database): 
    for baris in database[1:]:
        if (kategori == '='):
            if int(baris[5]) == tahun_ditemukan: 
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")

        elif (kategori == '>'):
            if int(baris[5]) >= tahun_ditemukan+1: 
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")
        
        elif (kategori == '<'):
            if int(baris[5]) <= tahun_ditemukan-1: 
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")
            
        elif (kategori == '>='):
            if int(baris[5]) >= tahun_ditemukan: 
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")
        
        elif (kategori == '<='):
            if int(baris[5]) <= tahun_ditemukan: 
                print(f"\nNama            : {infoBarang(tahun_ditemukan,kategori,'nama')}")
                print(f"Deskripsi       : {infoBarang(tahun_ditemukan,kategori,'deskripsi')}")
                print(f"Jumlah          : {infoBarang(tahun_ditemukan,kategori,'jumlah')}")
                print(f"Rarity          : {infoBarang(tahun_ditemukan,kategori,'rarity')}")
                print(f"Tahun ditemukan : {infoBarang(tahun_ditemukan,kategori,'tahun_ditemukan')}")

    print("\nSemua data telah ditampilkan")
            
else:
    print("\nTidak ada")