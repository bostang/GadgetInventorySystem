import os
from Basic_Procedure import *

# Procedure register (input: username,nama,alamat,password berupa string, output: string_data)
# I.S : User memasukkan input nama, username, pasword, dan alamat lalu menyimpan hasil input ke dalam database
# F.S. : Program mengeluarkan output dengan perintah 

#KAMUS
#username, password, nama, alamat, : string
#output : string       

# Fungsi - fungsi tambahan
def add_item_to_database(register_indeks,username,nama,alamat,password,_user):
    data_baru = [register_indeks,username,nama,alamat,password,'user']
    _user = _user.append(data_baru)

def user_list(nama_user,_user):
    # Cek data username
    for element in _user:
        if nama_user == element[1]:
            return True
    return False    

# Algoritma
def register(_user):
    print(">>> Register\n")
    nama = input("Masukkan nama: ").title()
    username = input('Masukkan username: ')
    if not user_list(username,_user):    # Cek username yang sama   
        password = input('Masukkan password: ')
        alamat = input('Masukkan alamat: ')
        register_indeks = str(int(_user[-1][0]) + 1)
        add_item_to_database(register_indeks,username,nama,alamat,password,_user)
        print('User',username, "telah berhasil register ke dalam Kantong Ajaib!")#user telah berhasil register
        os.system('pause')
    else:
        print('Username sama. Gagal register!')
        os.system('pause')
        