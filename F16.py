# Procedure help
# untuk menampilkan command input dari user/admin kemudian 
# mereturn print sesuai command yang user/admin butuhkan
# User/admin tidak perlu login untuk menggunakan fitur ini

from Basic_Procedure import *
import os

# KAMUS
    # Fungsi/Prosedur
        # procedure help(role : string)
            # menampilkan pesan bantuan berdasarkan role user
            # I.S. pesan bantuan belum ditampilkan
            # F.S. pesan bantuan telah ditampilkan
            
# REALISASI FUNGI/PROSEDUR
def bantuan():
    # KAMUS LOKAL
    # ALGORITMA
    loop = True
    while loop:
        role = str(input("Masukkan help untuk role apa (admin / user) : "))
    #Akses : admin
        if role == 'admin':
            print('COMMAND TEXT HELP UNTUK AKSES ADMIN')  
            print('======================================= HELP ===============================================') #tampilan help untuk akses admin
            print('register       - untuk melakukan registrasi user baru')
            print('login          - untuk melakukan login ke dalam sistem')
            print('tambahitem     - untuk melakukan penambahan item')
            print('carirarity     - untuk mencari item berdasarkan tingkat rarity suatu item')
            print('caritahun      - untuk mencari item berdasarkan input tahun yang diberikan')
            print('hapusitem      - untuk menghapus suatu item dari database')
            print('ubahjumlah     - untuk mengubah jumlah suatu item dalam database')
            print('riwayatpinjam  - untuk menampilkan riwayat peminjaman suatu item dalam gadget')
            print('riwayatkembali - untuk menampilkan riwayat pemngembalian suatu item dalam gadget')
            print('riwayatambil   - untuk menampilkan riwayat pengambilan consumable suatu item dalam database')
            print('save           - untuk menyimpan data ke dalam suatu file setelah diubah')
            print('help           - untuk menampilkan command sesuai kebutuhan user/admin')
            loop = False
            os.system('pause')
    #Akses : user
        elif role == 'user':
            print('COMMAND TEXT HELP UNTUK AKSES USER')   
            print('============================ HELP ===================================') #tampilan help untuk akses user
            print('login      - untuk melakukan login ke dalam sistem')
            print('carirarity - untuk mencari item berdasarkan tingkat rarity suatu item')
            print('caritahun  - untuk mencari item berdasarkan input tahun yang diberikan')
            print('pinjam     - untuk meminjam suatu item gadget dalam database')
            print('kembalikan - untuk mengembalikan suatu item gadget yang dipinjam')
            print('minta      - untuk memingta consumable yang tersedia dalam database')
            print('save       - untuk menyimpan data ke dalam suatu file setelah diubah')
            print('help       - untuk menampilkan command sesuai kebutuhan user/admin')  
            loop = False
            os.system('pause')

def bantuan_admin():
    print('COMMAND TEXT HELP UNTUK AKSES ADMIN')  
    print('======================================= HELP ===============================================') # tampilan help untuk akses admin
    print('register       - untuk melakukan registrasi user baru')
    print('login          - untuk melakukan login ke dalam sistem')
    print('tambahitem     - untuk melakukan penambahan item')
    print('carirarity     - untuk mencari item berdasarkan tingkat rarity suatu item')
    print('caritahun      - untuk mencari item berdasarkan input tahun yang diberikan')
    print('hapusitem      - untuk menghapus suatu item dari database')
    print('ubahjumlah     - untuk mengubah jumlah suatu item dalam database')
    print('riwayatpinjam  - untuk menampilkan riwayat peminjaman suatu item dalam gadget')
    print('riwayatkembali - untuk menampilkan riwayat pemngembalian suatu item dalam gadget')
    print('riwayatambil   - untuk menampilkan riwayat pengambilan consumable suatu item dalam database')
    print('save           - untuk menyimpan data ke dalam suatu file setelah diubah')
    print('help           - untuk menampilkan command sesuai kebutuhan user/admin')
    os.system('pause')

def bantuan_user():
    print('COMMAND TEXT HELP UNTUK AKSES USER')   
    print('============================ HELP ===================================') #tampilan help untuk akses user
    print('login      - untuk melakukan login ke dalam sistem')
    print('carirarity - untuk mencari item berdasarkan tingkat rarity suatu item')
    print('caritahun  - untuk mencari item berdasarkan input tahun yang diberikan')
    print('pinjam     - untuk meminjam suatu item gadget dalam database')
    print('kembalikan - untuk mengembalikan suatu item gadget yang dipinjam')
    print('minta      - untuk memingta consumable yang tersedia dalam database')
    print('save       - untuk menyimpan data ke dalam suatu file setelah diubah')
    print('help       - untuk menampilkan command sesuai kebutuhan user/admin')  
    os.system('pause')