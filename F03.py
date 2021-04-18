# Program cariRarity

# Kontributor : Muhammad Daris Nurhakim [16520170], ...

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def isRarityinDatabase(rarity,database):
    for element in database:
        if rarity == element[4]:
            return True
    return False

def convert_line_to_data(line):
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def infoBarang(rarity,spek):
    if (rarity == 'S') or (rarity == 'A') or (rarity == 'B') or (rarity == 'C'):
        arrayProcess = _gadget
    else:
        arrayProcess = []
    
    if isRarityinDatabase(rarity,arrayProcess):
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
rarity = input("Masukkan rarity: ")

while (rarity != 'S') and (rarity != 'A') and (rarity != 'B') and (rarity != 'C'):
    print("\nMasukan Anda salah!\n")
    rarity = input("Masukkan rarity: ")

print("\nHasil pencarian:")
if isRarityinDatabase(rarity,database): 
    for baris in database:
        if baris[4] == rarity: 
            print(f"\nNama            : {infoBarang(rarity,'nama')}")
            print(f"Deskripsi       : {infoBarang(rarity,'deskripsi')}")
            print(f"Jumlah          : {infoBarang(rarity,'jumlah')}")
            print(f"Rarity          : {infoBarang(rarity,'rarity')}")
            print(f"Tahun ditemukan : {infoBarang(rarity,'tahun_ditemukan')}")

    print("\nSemua data telah ditampilkan")
            
else:
    print("\nTidak ada")