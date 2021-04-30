import os
from Basic_Procedure import *
#Membaca file user.csv dan menutup file user.csv
f = open("user.csv", "r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

raw_initial = lines.pop(0)
data_initial = convert_line_to_data(raw_initial)
data_data = []

for line in lines:
    array_from_data = convert_line_to_data(line)
    real_value = convert_array_to_real_value(array_from_data)
    data_data.append(real_value)

def user_list(nama_user,data_data):
    # Cek data username
    for element in data_data:
        if nama_user == element[1]:
            return True
    return False    

def password_list(password,data_data):
    # Cek data password
    for element in data_data:
        if password == element[4]:
            return True
    return False    

# Procedure login
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