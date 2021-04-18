import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def isRarityinDatabase(rarity,database):
    # memeriksa apakah rarity item ada di suatu array database apa tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if rarity == element[4]: # lokasi rarity ada di kolom keempat
            return True
    return False

def convert_line_to_data(line): # [ *** SUDAH ADA DI F05 *** ]
    # menulis data per baris dalam csv ke dalam bentuk array
    # KAMUS LOKAL
        # Variabel
            # raw_array_of_data : array of string { array sementara [masih kotor oleh \n] }
            # array_data : array of string { array hasil berisi data-data dari csv}
    # ALGORITMA
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def infoBarang(rarity,spek): # [ *** SUDAH ADA DI F06 *** ]
    # mendapatkan informasi barang dari database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
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

    # mengakses database dalam bentuk array
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