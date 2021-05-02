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
def modify_datas(array, idx, col, value):
    # melakukan modifikasi pada suatu nilai array
    # KAMUS LOKAL
    # ALGORITMA
    array[idx][col] = value

def convert_datas_to_string(_gadget): # [ *** SUDAH ADA DI F06 tetapi agak beda *** ]
    # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
    # KAMUS LOKAL
        # Variabel
            # arr_data : array { array yang merupakan elemen _gadget atau _consumable }
            # arr_data_all_string : array of string { untuk skema konversi array database menjadi string }
            # arrayProcess : array of array of string { array yang ingin diproses }
            # string_data : string { untain informasi dari database [lokal] }
    # ALGORITMA
    arrayProcess = _gadget

    string_data = ""
    for arr_data in arrayProcess:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"

    return string_data

def overwrite_database(idPinjam,_gadget):
    # melakukan overwrite terhadap konten database [digunakan dalam skema penggantian jumlah item pada csv]
    # KAMUS LOKAL
        # datas_as_string : string { untain informasi dari database [lokal] }
        # f : textIOWrapper
    # ALGORITMA
    datas_as_string = convert_datas_to_string(_gadget)
    f = open("gadget.csv","w")
    f.write(datas_as_string) # melakukan overwrite terhadap isi database
    f.close()

def isIDinDatabase(id,database): # [ *** SUDAH ADA DI F05 *** ]
    # memeriksa apakah ID item ada di suatu array database apa tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if id == element[0]: # lokasi id ada di kolom pertama
            return True
    return False

def isUserinDatabase(user_aktif,database):
    # memeriksa apakah user ada di array _user atau tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if user_aktif == element[1]: # lokasi username ada di kolom kedua
            return True
    return False

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

def locIDinArray(arr,id):
    # mencari lokasi / index item dalam suatu array arr
    # KAMUS LOKAL
        # Variabel
            # k : integer { indeks saat k ketemu di arr }
    # ALGORITMA
    k = 0
    while k <= len(arr):
        if arr[k][0] == id:
            return k
        k += 1
    return "NOT FOUND"

def infoUser(username,spek,_user,barisS):
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
    else:
        return "user tidak ada pada database."

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

def add_pinjam_to_database(user_aktif,_gadget,_gadgetBorrow,_user,baris,jumlahPinjam,idPinjam):
    # Prosedur untuk menuliskan informasi peminjaman gadget ke gadget_borrow_history.csv
    # proses ini dijalankan bila sudah divalidasi bahwa gadget BISA dipinjam
    # KAMUS LOKAL
    # ALGORITMA
    id_peminjam = infoUser(user_aktif,'id',_user,baris)
    database = _gadgetBorrow
    id_transaksi = int(database[-1][0]) + 1
    tanggalPinjam = datetime.datetime.now().strftime("%d/%m/%Y")
    if (jumlahPinjam > 0):
        is_returned = "False"
    elif (jumlahPinjam == 0):
        is_returned = "True"
        # menambahkan riwayat peminjaman ke gadget_borrow_history.csv
    dataPinjam = [id_transaksi,id_peminjam,idPinjam,tanggalPinjam,jumlahPinjam,is_returned]
    _gadgetBorrow = _gadgetBorrow.append(dataPinjam)

        # mengubah jumlah barang yang tersedia [berkurang setelah dipinjam] pada gadget.csv
    modify_datas(_gadget,locIDinArray(_gadget,idPinjam),3,int(infoBarang(idPinjam,'jumlah',_gadget,baris))-jumlahPinjam)
    overwrite_database(idPinjam,_gadget)

# ALGORITMA UTAMA
    # melakukan proses peminjaman barang
def pinjamGadget(_user,_gadget,_gadgetBorrow,user_aktif):
    clear_screen()
    print(">>> Meminjam Gadget\n")
    kondisiLanjut = True
    idPinjam = input("Masukkan ID item: ")
    for baris in (_gadgetBorrow):
        id_peminjam = infoUser(user_aktif,'id',_user,baris)
        if (id_peminjam == infoPinjam('id_peminjam',_gadgetBorrow,baris)) and (idPinjam == infoPinjam('id_gadget',_gadgetBorrow,baris)) and (infoPinjam('is_returned',_gadgetBorrow,baris) == 'False'):
            print("User tidak bisa meminjam lagi barang tersebut!")
            os.system('pause')
            kondisiLanjut = False
            
            break
        
    if kondisiLanjut:
        if isIDinDatabase(idPinjam, _gadget): # peminjaman barang HANYA DARI gadget.csv
            tanggal = str(datetime.datetime.now().strftime("%d/%m/%Y"))
            tanggalPinjam = print("Tanggal peminjaman:",tanggal)
            jumlahPinjam = int(input("Jumlah peminjaman: "))
            if (jumlahPinjam <= int(infoBarang(idPinjam,'jumlah',_gadget,baris))):
                namaBarangPinjam = infoBarang(idPinjam,"nama",_gadget,baris)
                print(f"Item {namaBarangPinjam} (x{jumlahPinjam}) berhasil dipinjam!")
            elif (jumlahPinjam <= 0):
                print("Peminjaman gagal! (jumlah pinjam harus > 0)")
                kondisiLanjut = False
            else:
                print("Peminjaman Gagal! jumlah barang di database kurang")
                kondisiLanjut = False
        else:
            print("Peminjaman Gagal! barang tidak ditemukan di database")
            kondisiLanjut = False

    if kondisiLanjut:
        add_pinjam_to_database(user_aktif,_gadget,_gadgetBorrow,_user,baris,jumlahPinjam,idPinjam)