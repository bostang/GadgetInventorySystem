import os
from Basic_Procedure import *

# Fungsi - fungsi tambahan
def user_list(nama_user,_user):
    # Cek data username
    for element in _user:
        if nama_user == element[1]:
            return True
    return False    

def password_list(password,_user):
    # Cek data password
    for element in _user:
        if password == element[4]:
            return True
    return False    

def id_user(nama_user,_user):
    # Cek data username
    for element in _user:
        if nama_user == element[1]:
            return element

# Procedure login
# User memasukkan input berupa username dan password kemudian diproses dalam database
#Apabila username dan password sesuai maka output login berhasil
def login(_user):
    loop = True
    while loop:
        clear_screen()
        username = input('Masukkan username:')
        password = input('Masukkan password:')
        if user_list(username,_user) == True and password_list(password,_user) == True: # Cek username dan password dalam database
            print('Halo', username,'! Selamat datang di Kantong Ajaib.')
            user_aktif = id_user(username,_user)
            loop = False
            os.system('pause')
            return user_aktif
        else:
            print('Username atau password anda salah. Gagal login!') 
            os.system('pause')