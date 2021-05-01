import os
#Membaca file user.csv dan menutup file user.csv
f = open("user.csv", "r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

def bersih():
    # membuat efek clear screen pada Python
    os.system('cls' if os.name == 'nt' else 'clear')


def split(list):#Memisah tiap list dengan delimiter ;
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


def convert_from_line_to_data(line):#ubah baris menjadi data
    raw_array_from_data = split(line)
    array_from_data = [data.strip() for data in raw_array_from_data]
    return array_from_data

def convert_array_to_real_value(array_data):#ubah array data ke dalam nilai asli
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


def convert_data_to_string():#ubah nilai data ke dalam tipe string
    string_data = ",".join(data_initial) + "\n"
    for arr_data in data_data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def user_list(nama_user,data_data):#cek data username
    for element in data_data:
        if nama_user == element[1]:
            return True
    return False    

def password_list(password,data_data):#cek data password
    for element in data_data:
        if password == element[4]:
            return True
    return False    

#procedure login
# User memasukkan input berupa username dan password kemudian diproses dalam database
#Apabila username dan password sesuai maka output login berhasil

def login():
    username = input('Masukkan username:')
    password = input('Masukkan password:')
    if user_list(username,data_data) == True and password_list(password,data_data) == True:#Cek username dan password dalam database
        print('Halo', username,'! Selamat datang di Kantong Ajaib.')
    else:
        print('Username atau password anda salah. Gagal login!')   


print(login()) 