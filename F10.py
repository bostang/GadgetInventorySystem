"""
Meminta Consumable
Akses: User

Prosedur ini digunakan oleh pengguna untuk meminta consumable yang tersedia.
Pastikan masukan valid (contoh: jumlah tidak memiliki batas, item tersedia, dan 
lain-lain). Bila consumable menjadi 0, tidak perlu dihapus dari sistem.

Kontributor : Diffa' Shada 'Aqila [16520070], Joshi Ryu Setiady [16520230]

"""

import datetime
from Basic_Procedure import *

# KAMUS
    # Variabel
        # userAktif : string { user yang sedang sedang login ke program utama }
        # kondisiLanjut : boolean { kondisi yang menyatakan input telah valid [barang BISA dipinjam] }
        # id_barang_diminta : string { id barang yang ingin dipinjam }
        # tanggalPinjam : string { tanggal peminjaman }
        # jumlahPinjam : integer { jumlah barang yang dipinjam }
    # Fungsi / Prosedur
        # procedure modify_datas(input array: array of ..., idx : integer, col : integer, value : ...)
            # melakukan modifikasi pada suatu nilai array
            # I.S. nilai elemen suatu array terdefinisi ; F.S. nilai elemen array tersebut telah berubah
        # procedure convert_line_to_data( input line : string)
            # menulis data per baris dalam csv ke dalam bentuk array
            # I.S. belum ada array database ; F.S. array database sudah bisa digunakan
        # procedure convert_datas_to_string( input code : character)
            # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
            # I.S. database terdefinisi dalam bentuk array
            # F.S. database dalam bentuk string terbentuk dan siap untuk di-overwrite ke file csv
        # procedure overwrite_database(input code : character)
            # melakukan overwrite terhadap konten database [digunakan dalam skema penggantian jumlah item pada file csv]
            # I.S. belum ada perubahan pada database
            # F.S. database telah ditulis ulang dengan perubahan salah satu jumlah item
        # function isUserinDatabase(string, array of array of string) -> boolean
            # memeriksa apakah user ada di array _user apa tidak
        # function infoBarang(id : string ,spek : string) -> string / integer
            # mendapatkan informasi barang dari database
        # function locIDinArray(array of ..., string) -> integer
            # mencari lokasi / index item dalam suatu array arr
        # function infoUser(string, stiring) -> string
            # mendapatkan informasi user (nama atau id saja) dari database
        # procedure pinjamGadget()
            # Prosedur untuk menuliskan informasi peminjaman gadget ke gadget_borrow_history.csv
            # proses ini dijalankan bila sudah divalidasi bahwa gadget BISA dipinjam
            # I.S. telah diterima input id_barang_diminta,jumlahPinjam, tanggalPinjam
            # F.S. telah terdata informasi peminjaman di gadget_borrow_history.csv dan terdapat
              # perubahan jumlah item di gadget.csv

# REALISASI FUNGSI/PROSEDUR
def infoBarang(id,spek,array):
    # mendapatkan informasi barang dari database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = array
    if isIDinDatabase(id,arrayProcess):
        for baris in arrayProcess:
            if baris[0] == id:
            # me-return informasi
                if spek == 'nama':
                    return baris[1]
                elif spek == 'deskripsi':
                    return baris[2]
                elif spek == 'jumlah':
                    return baris[3]
                elif spek == 'rarity':
                    return baris[4]
                elif spek == 'tahun_ditemukan' and id[0] == 'C':
                    return baris[5]
    else:
        return "barang tidak ditemukan di database."

def change_quantity_in_database(idUbah,jumlahUbah,array):
    # melakukan skema pengubahan jumlah barang pada array _consumable
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of integer,string { array yang mau diproses }
            # baris : array of integer, string { untuk pencarian baris dengan id yang mau diubah jumlah itemnya }
    # ALGORITMA
    arrayProcess = array
    # mengubah jumlah item yang mau diubah
    for baris in arrayProcess:
        if baris[0] == idUbah:
            baris[3] = int(baris[3])
            baris[3] -= jumlahUbah
            baris[3] = str(baris[3])
    return arrayProcess

# ALGORITMA UTAMA
def mintaConsum(_consumable, _consumableHistory, user_aktif):
    # Prosedur untuk menuliskan informasi permintaan consumable ke data consumable_history.csv
    clear_screen()
    # melakukan proses peminjaman barang
    print(">>> Meminta Consumable")
    id_barang_diminta = input("Masukkan ID item: ").upper()

    if isIDinDatabase(id_barang_diminta, _consumable): # permintaan barang HANYA DARI consumable.csv
        jumlahPermintaan = int(input("Jumlah: "))
        tanggal = str(datetime.datetime.now().strftime("%d/%m/%Y"))
        print("Tanggal permintaan:",tanggal)

        if (jumlahPermintaan <= int(infoBarang(id_barang_diminta,'jumlah',_consumable))):
            namaBarangPermintaan = infoBarang(id_barang_diminta,"nama",_consumable)
            id_user_peminta = user_aktif[0]
            database = _consumableHistory
            id_minta = int(database[-1][0]) + 1

            # menambahkan riwayat peminjaman ke gadget_borrow_history.csv
            dataMinta = [id_minta,id_user_peminta,id_barang_diminta,str(tanggal),str(jumlahPermintaan)]
            _consumableHistory.append(dataMinta)

            # mengubah jumlah barang yang tersedia [berkurang setelah diminta] pada consumable.csv
            _consumable = change_quantity_in_database(id_barang_diminta, jumlahPermintaan, _consumable)
            print(f"Item {namaBarangPermintaan} (x{jumlahPermintaan}) telah berhasil diambil!")
        elif (jumlahPermintaan <= 0):
            print("Permintaan gagal! (jumlah pengambilan harus > 0)")
        else:
            print("Permintaan Gagal! jumlah barang di database kurang")
    else:
        print("Permintaan Gagal! barang tidak ditemukan di database")
    os.system('pause')

        