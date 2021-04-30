"""
Menambah item
Akses: Admin

Admin dapat menambahkan item ke dalam inventori. Admin memasukkan ID item yang akan 
ditambahkan(gadget atau consumable)
☑ Jika ID diawali dengan huruf G, maka admin akan memasukkan nama gadget, deskripsi gadget,
jumlah gadget yang tersedia, rarity gadget(C,B,A,S), serta tahun ditemukannya gadget.
☑ Jika ID diawali dengan huruf C, maka admin akan memasukkan nama consumable, deskripsi 
consumable, jumlah consumable yang tersedia, dan rarity consumable.
☑ Jika ID tidak diawali dengan huruf G atau C, maka fungsi akan mengeluarkan error

Catatan: Fungsi akan mengeluarkan error jika input user tidak valid, misal: ID sudah ada sebelumnya, dll

Kontributor : Bostang Palaguna [16520090], Muhammad Daris Nurhakim [16520170]

"""

# mengimport file dari Python
import os
from Basic_Procedure import *

# KAMUS
    # Variabel
        # array_of_data : array of string { array sementara untuk menambah data dari file csv ke array database }
        # g : textIOWrapper
        # c : textIOWrapper
        # raw_lines_g : array of character { array sementara berisi data gadget [banyak \n ] }
        # raw_lines_c : array of character { array sementara berisi data consumable [banyak \n ]}
        # lines_g : array of character { array sementara sebelum mebuat _gadget }
        # lines_c : array of character { array sementara sebelum mebuat _consumable }
        # _gadget : array database gadget.csv
        # _consumable : array database consumable.csv
    # Fungsi/Prosedur
        # function bersih
            # membuat efek clear screen pada Python
        # procedure splitList
            # menulis data per baris dalam csv ke dalam bentuk array
        # procedure add_item_to_database(input id, nama, deskripsi, jumlah, rarity, tahuntemu: string)
            # menambahkan item LANGSUNG ke gadget.csv atau consumable.csv
            # I.S. barang belum masuk ke file .csv ; F.S. barang telah ditambahkan ke file .csv
        # procedure tambahItem()
            # prosedur menerima input informasi barang dan menambahkan ke csv database
            # I.S. informasi barang belum di-ipnut ; F.S. barang telah divalidasi (ditampilkan pesan error / ditambahkan ke database)
        # function isIDinDatabase(id : string, database: array of array of string) -> boolean
            # memeriksa apakah id barang sudah ada di database atau belum

# REALISASI FUNGSI/PROSEDUR
def isIDinDatabase(id,database):
    # memeriksa apakah iD item ada di suatu array database apa tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if id == element[0]: # lokasi id ada di kolom pertama
            return True
    return False

def add_item_to_database(id,nama,deskripsi,jumlah,rarity,tahuntemu):
    # menambahkan item LANGSUNG ke gadget.csv atau consumable.csv
    # KAMUS LOKAL
        # Variabel
            # new_data : string { string data yang ingin ditulis ke file database.csv }
    # ALGORITMA
    if id[0] == 'G': # menambahkan ke gadget.csv bila id dimulai dari huruf G
        new_data = f"{id};{nama};{deskripsi};{jumlah};{rarity};{tahuntemu}\n"
        f = open("gadget.csv","a") # "a" : menambahkan konten pada database.csv
    elif id[0] == 'C': # menambahkan ke consumable.csv bila id dimulai dari huruf C
        new_data = f"{id};{nama};{deskripsi};{jumlah};{rarity}\n"
        f = open("consumable.csv","a")

    f.write(new_data)
    f.close()

def tambahItem():
    # prosedur menerima input informasi barang dan menambahkan ke csv database
    #KAMUS
        # Variabel
            # id : string
            # nama : string
            # deskripsi : string
            # jumlah : integer
            # rarity : character
            # tahuntemu : integer
            # tempatData : array of array of string
            # kondisiLanjut : boolean
    #ALGORITMA
    clear_screen()
    kondisiLanjut = True
    print(">>> Menambah Item")
    id = input("Masukan ID: ")
    if id[0] == 'C':
        tempatData = _consumable
    elif id[0] == 'G':
        tempatData = _gadget
    else:
        print("\nGagal menambahkan item karena ID tidak valid")
        kondisiLanjut = False

    if kondisiLanjut:
        if not isIDinDatabase(id,tempatData):
            nama = input("Masukan Nama: ")
            deskripsi = input("Masukan Deskripsi: ")

            while True:
                try:
                    jumlah = int(input("Masukan Jumlah: "))
                    break
                except ValueError:
                    print("\nMasukan jumlah dalam bentuk angka!\n")

            rarity = input("Masukan Rarity: ").upper()
            while (rarity != 'C') and (rarity != 'B') and (rarity != 'A') and (rarity != 'S'):
                print("\nInput rarity tidak valid!\n")
                rarity = input("Masukan Rarity: ")
            else:
                if id[0] == 'G':
                    while True:
                        try:
                            tahuntemu = int(input("Masukan tahun ditemukan: "))
                            break
                        except ValueError:
                            print("\nMasukan tahun dalam bentuk angka!\n")
                else: 
                    tahuntemu = 0 # nilai dummy
                add_item_to_database(id,nama,deskripsi,jumlah,rarity,tahuntemu)
                print("\nItem telah berhasil ditambahkan ke database")

        else:
            print("\nGagal menambahkan item karena ID sudah ada")

# ALGORITMA UTAMA
    # membaca file database.csv
g = open("gadget.csv","r")
c = open("consumable.csv","r")
raw_lines_g = g.readlines()
raw_lines_c = c.readlines()
g.close()
c.close()
lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]
lines_c = [raw_line.replace("\n", "") for raw_line in raw_lines_c]

    # mengakses database dalam bentuk array
_gadget = []
_consumable = []

for line in lines_g:
    array_of_data = split(line)
    _gadget.append(array_of_data)
for line in lines_c:
    array_of_data = split(line)
    _consumable.append(array_of_data)

    # menambahkan gadget baru
tambahItem()
print("")
os.system('pause')