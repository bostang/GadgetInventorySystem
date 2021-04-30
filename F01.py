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

# Procedure register (input: username,nama,alamat,password berupa string, output: string_data)
# I.S : User memasukkan input nama, username, pasword, dan alamat lalu menyimpan hasil input ke dalam database
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
    # Cek data username
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