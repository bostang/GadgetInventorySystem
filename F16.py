#Fungsi help untuk menampilkan command input dari user/admin
#kemudian mereturn print sesuai command yang user/admin butuhkan

#User/admin tidak perlu login untuk menggunakan fitur ini

from Basic_Procedure import *

# KAMUS
    # Variabel
        # userAktif : string { akan menyesuaikan dengan user yang login pada F02 }
    # Fungsi/Prosedur
        # procedure help(role : string)
            # menampilkan pesan bantuan berdasarkan role user
            # I.S. pesan bantuan belum ditampilkan
            # F.S. pesan bantuan telah ditampilkan
        # function isUserinDatabase(string, array of array of string) -> boolean
            # memeriksa apakah user ada di array _user apa tidak
        # function infoUser(string, stiring) -> string
            # mendapatkan informasi user (nama,id,atau role saja) dari database
      # procedure convert_line_to_data( input line : string)
            # menulis data per baris dalam csv ke dalam bentuk array
            # I.S. belum ada array database ; F.S. array database sudah bisa digunakan  
            
# REALISASI FUNGI/PROSEDUR
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

def isUserinDatabase(user,database):
    # memeriksa apakah user ada di array _user atau tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if user == element[1]: # lokasi username ada di kolom kedua
            return True
    return False

def infoUser(username,spek):
    # mendapatkan informasi user (nama atau id saja) dari database
    # KAMUS LOKAL
        # Variabel
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    if isUserinDatabase(username,_user): # id menyatakan id user
        for baris in _user:
            if baris[1] == username:
            # me-return informasi
                if spek == 'id':
                    return baris[0]
                elif spek == 'nama':
                    return baris[2]
                elif spek == 'role':
                    return baris[5]
    else:
        return "user tidak ada pada database."


def help(role):
    # KAMUS LOKAL
    # ALGORITMA
    #Akses : admin
    if role == 'admin':
        print('COMMAND TEXT HELP UNTUK AKSES ADMIN')  
        print('============= HELP ===========')#tampilan help untuk akses admin
        print('register - untuk melakukan registrasi user baru')
        print('login - untuk melakukan login ke dalam sistem')
        print('tambahitem - untuk melakukan penambahan item')
        print('carirarity - untuk mencari item berdasarkan tingkat rarity suatu item')
        print('caritahun - untuk mencari item berdasarkan input tahun yang diberikan')
        print('hapusitem - untuk menghapus suatu item dari database')
        print('ubahjumlah - untuk mengubah jumlah suatu item dalam database')
        print('riwayatpinjam - untuk menampilkan riwayat peminjaman suatu item dalam gadget')
        print('riwayatkembali - untuk menampilkan riwayat pemngembalian suatu item dalam gadget')
        print('riwayatambil - untuk menampilkan riwayat pengambilan consumable suatu item dalam database')
        print('save - untuk menyimpan data ke dalam suatu file setelah diubah')
        print('help - untuk menampilkan command sesuai kebutuhan user/admin')
    
    #Akses : user
    elif role == 'user':
        print('COMMAND TEXT HELP UNTUK AKSES USER')   
        print('============= HELP ===========')#tampilan help untuk akses user
        print('login - untuk melakukan login ke dalam sistem')
        print('carirarity - untuk mencari item berdasarkan tingkat rarity suatu item')
        print('caritahun - untuk mencari item berdasarkan input tahun yang diberikan')
        print('pinjam - untuk meminjam suatu item gadget dalam database')
        print('kembalikan - untuk mengembalikan suatu item gadget yang dipinjam')
        print('minta - untuk memingta consumable yang tersedia dalam database')
        print('save - untuk menyimpan data ke dalam suatu file setelah diubah')
        print('help - untuk menampilkan command sesuai kebutuhan user/admin')  

# ALGORITMA UTAMA

user_aktif = input() ### harus disesuaikan dengan pengguna aktif di F02

    # mengakses database user
u = open("user.csv","r")
raw_lines_u = u.readlines()
u.close()
lines_u = [raw_line.replace("\n", "") for raw_line in raw_lines_u]
_user = []
for line in lines_u:
    array_of_data = convert_line_to_data(line)
    _user.append(array_of_data)
    
   

help(infoUser(user_aktif,'role')) 
