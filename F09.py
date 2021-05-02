"""
Mengembalikan Gadget
Akses: User

Prosedur ini digunakan untuk mengembalikan gadget secara seutuhnya. Selain itu,
karena Doraemonangis memiliki mesin waktu, tanggal pengembalian tidak harus lebih
besar dari tanggal peminjaman (abaikan tanggal, bukan faktor dalam peminjaman).
Namun, entry peminjaman harus ada untuk dapat mengembalikan sebuah gadget. Bila 
mengerjakan bonus, silahkan menyesuaikan input dan output.

Kontributor : Bostang Palaguna [16520090], Diffa' Shada 'Aqila [16520070], Muhammad Daris Nurhakim [16520170], Joshi Ryu Setiady [16520230]

"""

import datetime
from Basic_Procedure import *

# KAMUS
    # Variabel
        # arrayBarangPinjam : array of string { daftar barang di inventori user [yang telah dipinjam] }
        # arrayJumlahPinjam : array of integer { jumlah barang yang dipinjam }
        # userAktif : string { user yang sedang sedang login ke program utama }
        # kondisiLanjut : boolean { kondisi yang menyatakan input telah valid [barang BISA dipinjam] }
        # idPengembalian : string { id barang yang ingin dipinjam }
        # tanggalPengembalian: string { tanggal peminjaman }
        # jumlahPengembalian : integer { jumlah barang yang dipinjam }
    # Fungsi / Prosedur
        # procedure modify_datas(input array: array of ..., idx : integer, col : integer, value : ...)
            # melakukan modifikasi pada suatu nilai array
            # I.S. nilai elemen suatu array terdefinisi ; F.S. nilai elemen array tersebut telah berubah
        # function locIDinArray(array of ..., string) -> integer
            # mencari lokasi / index item dalam suatu array arr
        # procedure convert_datas_to_string( input code : character)
            # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
            # I.S. database terdefinisi dalam bentuk array
            # F.S. database dalam bentuk string terbentuk dan siap untuk di-overwrite ke file csv
        # procedure overwrite_database(input code : character)
            # melakukan overwrite terhadap konten database [digunakan dalam skema penggantian jumlah item pada file csv]
            # I.S. belum ada perubahan pada database
            # F.S. database telah ditulis ulang dengan perubahan salah satu jumlah item
        # procedure convert_line_to_data( input line : string)
            # menulis data per baris dalam csv ke dalam bentuk array
            # I.S. belum ada array database ; F.S. array database sudah bisa digunakan
        # function isUserinDatabase(string, array of array of string) -> boolean
            # memeriksa apakah user ada di array _user apa tidak
        # function infoBarang(id : string ,spek : string) -> string / integer
            # mendapatkan informasi barang dari database
        # function infoUser(string, stiring) -> string
            # mendapatkan informasi user (nama atau id saja) dari database
        # procedure inventory(input user: string)
            # prosedur untuk menampilkan barang-barang apa saja yang sudah dipinjam (inventory)
            # I.S. telah tersedia barang-barang yang telah dipinjam
            # F.S. barang-barang yang telah dipinjam beserta jumlahnya ditampilkan pada layar
        # procedure kembaliGadget()
            # prosedur mengembalikan gadget ke gadget.csv dan mendata riwayatnya ke gadget_return_history.csv
            # I.S. input barang yang ingin dikembalikan telah divalidasi
            # F.S. jumlah barang pada gadget.csv telah berubah, riwayat pengembalian telah ditambahkan ke gadget_return_history.csv

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

def InventoryUser(user_aktif, _gadgetBorrow, _gadget):
    # prosedur untuk menampilkan barang-barang apa saja yang sudah dipinjam (inventory)
    # KAMUS LOKAL
        # Variabel
            # riwayat : array of string { baris pada _gadgetBorrowHistory }
            # k : integer { variabel iterasi }
    # ALGORITMA

    # ide umum :
        #traversing array _gadgetBorrowHistory, jika id sama, tambahkan
        #traversing array _gadgetReturnHistory, jika id sama, kurangi

        # misalkan suatu barang dipinjam lebih dari satu kali, maka jumlah barang pinjam akan ditambahkan
        # perhatikan bahwa id peminjam terdapat pada indeks = 1

    inventory = []

    # Memasukkan daftar gadget yang belum dibalikkan
    for riwayat in _gadgetBorrow: # jumlah positif
        if riwayat[1] == user_aktif[0]:
            if riwayat[6] == "False":
                data_inven = [riwayat[0],riwayat[2],riwayat[5]]
                inventory.append(data_inven)

    # menampilkan barang-barang yang telah dipinjam dalam bentuk list:
    k = 1
    for jenis in inventory:
        print(f"{k}. {infoBarang(jenis[1],'nama',_gadget)}          || jumlah : {jenis[2]}")
        k += 1
    
    return inventory

def change_quantity_in_database(idUbah,jumlahUbah,array,x,sisa_dipinjam):
    # melakukan skema pengubahan jumlah barang pada array _consumable atau _gadget
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of integer,string { array yang mau diproses }
            # baris : array of integer, string { untuk pencarian baris dengan id yang mau diubah jumlah itemnya }
    # ALGORITMA
    arrayProcess = array
    # mengubah jumlah item yang mau diubah
    for baris in arrayProcess:
        if baris[0] == idUbah:
            if x == 3:
                baris[x] = int(baris[x])
                baris[x] += jumlahUbah
                baris[x] = str(baris[x])
            elif x == 5:
                baris[x] = int(baris[x])
                baris[x] -= jumlahUbah
                baris[x] = str(baris[x])
                if sisa_dipinjam == 0:
                    baris[6] = "True"
    return arrayProcess

# ALGORITMA UTAMA
def kembalikanGadget(_gadget,_gadgetBorrow,_gadgetReturn,user_aktif):
    clear_screen()
    # skema pengembalian barang
    print(">>> Mengembalikan Gadget\n")

    # menampilkan inventori [ daftar barang yang telah dipinjam ]
    inventory = InventoryUser(user_aktif, _gadgetBorrow, _gadget)
    print("")

    # validasi input pengembalian
    loop = True
    while loop:
        try:
            nomorPengembalian = int(input("Masukan nomor peminjaman: "))
            if nomorPengembalian > 0 and nomorPengembalian <= len(inventory):
                loop = False
                array_pengembalian = inventory[nomorPengembalian-1]
                idBarang = array_pengembalian[1]
                jumlah_sisa = int(array_pengembalian[2])
                tanggal = str(datetime.datetime.now().strftime("%d/%m/%Y"))
                print("Tanggal pengembalian:",tanggal)
                jumlahPengembalian = int(input(f"Masukkan jumlah {infoBarang(idBarang,'nama',_gadget)} yang mau dikembalikan: "))
                if jumlahPengembalian > jumlah_sisa: 
                    print("Pengembalian item gagal! Jumlah barang yang ingin dikembalikan lebih dari yang dipinjam")
                elif jumlahPengembalian <= 0:
                    print("Pengembalian item gagal! Jumlah barang yang ingin dikembalikan tidak valid!")
                else: # input valid
                    # prosedur mengembalikan gadget ke gadget.csv dan mendata riwayatnya ke gadget_return_history.csv
                    # menambahkan riwayat pengembalian ke gadget_return_history.csv
                    database = _gadgetReturn
                    if database[-1][0] == 'id':
                        id_pengembalian = 1
                    else:
                        id_pengembalian = int(database[-1][0]) + 1
                    id_peminjaman = array_pengembalian[0]
                    sisa_inventory = jumlah_sisa - jumlahPengembalian
                    data_baru = [str(id_pengembalian),id_peminjaman,idBarang,tanggal,str(jumlahPengembalian)]
                    _gadgetReturn.append(data_baru)

                    # mengubah jumlah barang yang tersedia [bertambah setelah pengembalian] pada gadget.csv
                    _gadget = change_quantity_in_database(idBarang, jumlahPengembalian, _gadget, 3, sisa_inventory)

                    # mengubah jumlah sisa_dipinjam pada gadget_borrow_history.csv
                    _gadgetBorrow = change_quantity_in_database(id_peminjaman, jumlahPengembalian, _gadgetBorrow, 5, sisa_inventory)

                    print(f"\nItem {infoBarang(idBarang,'nama',_gadget)} (x{jumlahPengembalian}) telah dikembalikan. Sisa di inventory berjumlah {sisa_inventory}.")
            else:
                print("Nomor barang yang ingin dikembalikan tidak sesuai!")
                os.system('pause')
        except ValueError:
            print("Nomor barang yang ingin dikembalikan tidak sesuai!")
            os.system('pause')
    os.system('pause')
