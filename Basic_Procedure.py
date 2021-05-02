import os

# Procedure yang sering dipakai
def clear_screen():
    # Membuat efek clear screen pada Python
    os.system('cls' if os.name == 'nt' else 'clear')

def splitList(list):
    # menulis data per baris dalam csv ke dalam bentuk array dengan delimiter ";"
    # KAMUS LOKAL
        # Variabel
            # database : array of string { array sementara [masih kotor oleh \n] }
            # aplit_list : array of string { array hasil berisi data-data dari csv}
    # ALGORITMA
    sentence = ''.join(list)
    split_list = []
    tmp = ''
    for s in sentence:
        if s == ';':
            split_list.append(tmp)
            tmp = ''
        else:
            tmp += s
    if tmp:
        split_list.append(tmp)
    return split_list

def convert_line_to_data(line):
    # Mengubah baris menjadi data
    raw_array_from_data = splitList(line)
    array_from_data = [data.strip() for data in raw_array_from_data]
    return array_from_data

def convert_array_to_real_value(array_data):
    # Mengubah array data ke dalam nilai asli
    arr_cpy = array_data[:]
    for i in range(6):
        if(i == 0):
            arr_cpy[i] = int(arr_cpy[i])   
        else:
            arr_cpy[i] = str(arr_cpy[i])
    return arr_cpy

def isIDinDatabase(id,database):
    # memeriksa apakah iD item ada di suatu array database apa tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if id == element[0]: # lokasi id ada di kolom pertama
            return True
    return False

def infoBarang(id,spek,_consumable,_gadget):
    # mendapatkan informasi barang dari database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    if id[0] == 'C':
        arrayProcess = _consumable
    elif id[0] == 'G':
        arrayProcess = _gadget
    else:
        arrayProcess = []

    if isIDinDatabase(id,arrayProcess):
        for baris in arrayProcess:
            if baris[0] == id:
            # me-return informasi
                if spek == 'nama':
                    return baris[1]
                elif spek == 'deskripsi':
                    return baris[2]
                elif spek == 'jumlah':
                    return baris[3]
                elif spek == 'rarity':
                    return baris[4]
                elif spek == 'tahun_ditemukan' and id[0] == 'C':
                    return baris[5]
    else:
        return "\nbarang tidak ditemukan di database"