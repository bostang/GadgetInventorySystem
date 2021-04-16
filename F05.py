# Program tambahGadget
# menambahkan gadget ke gadget.csv dan consumable.csv

# Kontributor : Bostang Palaguna [16520090], ...

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
        # procedure convert_line_to_data(input line: string)
            # menulis data per baris dalam csv ke dalam bentuk array
            # I.S. belum ada array database ; F.S. array database sudah bisa digunakan
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

def convert_line_to_data(line):
    # menulis data per baris dalam csv ke dalam bentuk array
    # KAMUS LOKAL
        # Variabel
            # raw_array_of_data : array of string { array sementara [masih kotor oleh \n] }
            # array_data : array of string { array hasil berisi data-data dari csv}
    # ALGORITMA
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def add_item_to_database(id,nama,deskripsi,jumlah,rarity,tahuntemu):
    # menambahkan item LANGSUNG ke gadget.csv atau consumable.csv
    # KAMUS LOKAL
        # Variabel
            # new_data : string { string data yang ingin ditulis ke file database.csv }
    # ALGORITMA
    if id[0] == 'G': # menambahkan ke gadget.csv bila id dimulai dari huruf G
        new_data = f"{id},{nama},{deskripsi},{jumlah},{rarity},{tahuntemu}\n"
        f = open("gadget.csv","a") # "a" : menambahkan konten pada database.csv
    elif id[0] == 'C': # menambahkan ke consumable.csv bila id dimulai dari huruf C
        new_data = f"{id},{nama},{deskripsi},{jumlah},{rarity}\n"
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
    kondisiLanjut = True
    id = input("Masukan ID: ")
    if id[0] == 'C':
        tempatData = _consumable
    elif id[0] == 'G':
        tempatData = _gadget
    else:
        print("Gagal menambahkan item karena ID tidak valid")
        kondisiLanjut = False

    if kondisiLanjut:
        if not isIDinDatabase(id,tempatData):
            nama = input("Masukan Nama: ")
            deskripsi = input("Masukan Deskripsi: ")
            jumlah = input("Masukan Jumlah: ")
            rarity = input("Masukan Rarity: ")

            if rarity in ['C','B','A','S']:
                if id[0] == 'G':
                    tahuntemu = input("Masukan tahun ditemukan: ")
                else: tahuntemu = 0 # nilai dummy
                add_item_to_database(id,nama,deskripsi,jumlah,rarity,tahuntemu)
            else:
                print("Input rarity tidak valid!")
        else:
            print("Gagal menambahkan item karena ID sudah ada")

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
    array_of_data = convert_line_to_data(line)
    _gadget.append(array_of_data)
for line in lines_c:
    array_of_data = convert_line_to_data(line)
    _consumable.append(array_of_data)

    # menambahkan gadget baru
tambahItem()
