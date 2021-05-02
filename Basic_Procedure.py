import os

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
