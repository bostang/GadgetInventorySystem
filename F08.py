"""
Meminjam Gadget
Akses: User

User dapat melakukan peminjaman gadget yang akan menambahkan entry pada file
history bila di-save. Pastikan bahwa masukan yang diberikan valid, misalnya peminjaman
tidak melebihi stok yang ada pada sistem. Bila gadget menjadi 0, tidak perlu dihapus
dari sistem. Tidak perlu membuat entry baru pada file history pengembalian gadget.
Seseorang tidak dapat meminjam jenis gadget yang sama ketika sedang meminjam gadget tersebut.

Kontributor : Bostang Palaguna [16520090], Diffa' Shada 'Aqila [16520070]

"""

import datetime
from Basic_Procedure import *

# KAMUS
    # Variabel
        # user_aktif : string { user yang sedang sedang login ke program utama }
        # kondisiLanjut : boolean { kondisi yang menyatakan input telah valid [barang BISA dipinjam] }
        # idPinjam : string { id barang yang ingin dipinjam }
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
        # function isIDinDatabase(string, array of array of string) -> boolean
            # memeriksa apakah ID item ada di suatu array database apa tidak
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
            # I.S. telah diterima input idPinjam,jumlahPinjam, tanggalPinjam
            # F.S. telah terdata informasi peminjaman di gadget_borrow_history.csv dan terdapat
              # perubahan jumlah item di gadget.csv

# REALISASI FUNGSI/PROSEDUR
def infoBarang(id,spek,_gadget,baris):
    # mendapatkan informasi barang dari database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _gadget

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

def infoPinjam(spek,_gadgetBorrow,baris):
    # mendapatkan informasi mengenai barang yang dipinjam
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    arrayProcess = _gadgetBorrow
    # mengecek baris per baris
    i = 0
    while arrayProcess[i]:
        if spek == 'id':
            return baris[0]
        elif spek == 'id_peminjam':
            return baris[1]
        elif spek == 'id_gadget':
            return baris[2]
        elif spek == 'tanggal_peminjaman':
            return baris[3]
        elif spek == 'jumlah_pinjam':
            return baris[4]
        elif spek == 'is_returned':
            return baris[5]       
        i += 1
    else:
        return "\nbarang tidak ditemukan di database"

def change_quantity_in_database(idUbah,jumlahUbah,array):
    # melakukan skema pengubahan jumlah barang pada array
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
    # melakukan proses peminjaman barang
def pinjamGadget(_user,_gadget,_gadgetBorrow,user_aktif):
    clear_screen()
    print(">>> Meminjam Gadget\n")
    kondisiLanjut = True
    idPinjam = input("Masukkan ID item: ").upper()
    # Cek apakah user ingin meminjam gadget yang sama
    for baris in (_gadgetBorrow):
        id_peminjam = user_aktif[0]
        if (id_peminjam == infoPinjam('id_peminjam',_gadgetBorrow,baris)) and (idPinjam == infoPinjam('id_gadget',_gadgetBorrow,baris)) and (infoPinjam('is_returned',_gadgetBorrow,baris) == 'False'):
            print("User tidak bisa meminjam lagi barang tersebut!")
            os.system('pause')
            kondisiLanjut = False
            break
        
    if kondisiLanjut:
        if isIDinDatabase(idPinjam, _gadget): # peminjaman barang HANYA DARI gadget.csv
            tanggal = str(datetime.datetime.now().strftime("%d/%m/%Y"))
            print("Tanggal peminjaman:",tanggal)
            jumlahPinjam = int(input("Jumlah peminjaman: "))
            if (jumlahPinjam <= int(infoBarang(idPinjam,'jumlah',_gadget,baris))):
                namaBarangPinjam = infoBarang(idPinjam,"nama",_gadget,baris)
                
                # Prosedur untuk menuliskan informasi peminjaman gadget ke gadget_borrow_history.csv
                database = _gadgetBorrow
                id_transaksi = int(database[-1][0]) + 1

                # menambahkan riwayat peminjaman ke gadget_borrow_history.csv
                dataPinjam = [id_transaksi,id_peminjam,idPinjam,str(tanggal),str(jumlahPinjam),"False"]
                _gadgetBorrow.append(dataPinjam)

                # mengubah jumlah barang yang tersedia [berkurang setelah dipinjam] pada gadget.csv
                _gadget = change_quantity_in_database(idPinjam, jumlahPinjam, _gadget)
                print(f"Item {namaBarangPinjam} (x{jumlahPinjam}) berhasil dipinjam!")
            elif (jumlahPinjam <= 0):
                print("Peminjaman gagal! (jumlah pinjam harus > 0)")
            else:
                print("Peminjaman Gagal! jumlah barang di database kurang")
        else:
            print("Peminjaman Gagal! barang tidak ditemukan di database")
    os.system('pause')