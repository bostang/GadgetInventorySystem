import os
#Membaca file user.csv dan menutup file user.csv
f = open("user.csv", "r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

def bersih():
    # membuat efek clear screen pada Python
    os.system('cls' if os.name == 'nt' else 'clear')


def split(list):
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


def convert_from_line_to_data(line):
    raw_array_from_data = split(line)
    array_from_data = [data.strip() for data in raw_array_from_data]
    return array_from_data

def convert_array_to_real_value(array_data):
    arr_cpy = array_data[:]
    for i in range(6):
        if(i == 0):
            arr_cpy[i] = int(arr_cpy[i])   
        else:
            arr_cpy[i] = str(arr_cpy[i])
    return arr_cpy

raw_initial = lines.pop(0)
data_initial = convert_from_line_to_data(raw_initial)
data_data = []

for line in lines:
    array_from_data = convert_from_line_to_data(line)
    real_value = convert_array_to_real_value(array_from_data)
    data_data.append(real_value)


def convert_data_to_string():
    string_data = ",".join(data_initial) + "\n"
    for arr_data in data_data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"
    return string_data


#procedure register (input: username,nama,alamat,password berupa string, output: string_data)
# I.S : User memeasukkan input nama, username, pasword, dan alamat lalu menyimpan hasil input ke dalam database
# F.S. : Program mengeluarkan output dengan perintah 

#KAMUS
#username, password, nama, alamat, : string
#output : string       

#FUMGSI-FUNGSI TAMBAHAN
def add_item_to_database(register_indeks,username,nama,alamat,password):
    data_baru = f"{register_indeks};{username};{nama};{alamat};{password};user\n"
    f = open('user.csv', 'a')
    f.write(data_baru)
    f.close()

def user_list(nama_user,data_data):
    for element in data_data:
        if nama_user == element[1]:
            return True
    return False    

#ALGORITMA
def register():
    nama = input("Masukkan nama:").title()
    username = input('Masukkan username:')
    if not user_list(username,data_data):#Cek username yang sama   
        password = input('Masukkan password:')
        alamat = input('Masukkan alamat:')
        register_indeks = data_data[-1][0] + 1
        add_item_to_database(register_indeks,username,nama,alamat,password)
        print('User',username, "telah berhasil register ke dalam Kantong Ajaib")#user telah berhasil register
           
    else:
        print('Username sama. Gagal register!')
        

print(register())#fungsi register dijalankan