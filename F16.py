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
def bantuan_luar():
    # bantuan sebelum login
    print("================== HELP =====================")
    print("login - untuk melakukan login ke dalam sistem")
    print("help  - untuk menampilkan keterangan menu")
    print("exit  - untuk keluar dari program")
    os.system('pause')

def bantuan_dalam(role):
    # Bantuan saat sudah login
    # ALGORITMA
    #Akses : admin
    if role == 'admin':
        print('COMMAND TEXT HELP UNTUK AKSES ADMIN')  
        print('======================================= HELP ===============================================') #tampilan help untuk akses admin
        print('register       - untuk melakukan registrasi user baru')
        print('carirarity     - untuk mencari item berdasarkan tingkat rarity suatu item')
        print('caritahun      - untuk mencari item berdasarkan input tahun yang diberikan')
        print('tambahitem     - untuk melakukan penambahan item')
        print('hapusitem      - untuk menghapus suatu item dari database')
        print('ubahjumlah     - untuk mengubah jumlah suatu item dalam database')
        print('riwayatpinjam  - untuk menampilkan riwayat peminjaman suatu item dalam gadget')
        print('riwayatkembali - untuk menampilkan riwayat pemngembalian suatu item dalam gadget')
        print('riwayatambil   - untuk menampilkan riwayat pengambilan consumable suatu item dalam database')
        print('save           - untuk menyimpan data ke dalam suatu file setelah diubah')
        print('help           - untuk menampilkan keterangan menu')
        print('exit           - untuk keluar dari program. Dapat sekaligus melakukan save')
        os.system('pause')
    #Akses : user
    elif role == 'user':
        print('COMMAND TEXT HELP UNTUK AKSES USER')   
        print('============================ HELP ===================================') #tampilan help untuk akses user
        print('carirarity - untuk mencari item berdasarkan tingkat rarity suatu item')
        print('caritahun  - untuk mencari item berdasarkan input tahun yang diberikan')
        print('pinjam     - untuk meminjam suatu item gadget dalam database')
        print('kembalikan - untuk mengembalikan suatu item gadget yang dipinjam')
        print('minta      - untuk memingta consumable yang tersedia dalam database')
        print('save       - untuk menyimpan data ke dalam suatu file setelah diubah')
        print('help       - untuk menampilkan keterangan menu')
        print('exit       - untuk keluar dari program. Dapat sekaligus melakukan save')
        os.system('pause')