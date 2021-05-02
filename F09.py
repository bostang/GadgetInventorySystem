# Program kembaliGadget
    # mengembalikan gadget ke gadget.csv dan menyimpan riwayatnya pada gadget_return_history.csv

# Kontributor : Bostang Palaguna [16520090]

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

def modify_datas(array, idx, col, value):
    # melakukan modifikasi pada suatu nilai array
    # KAMUS LOKAL
    # ALGORITMA
    array[idx][col] = value

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

def convert_datas_to_string(code): # [ *** SUDAH ADA DI F06 tetapi agak beda *** ]
    # mengubah konten array database menjadi untain string panjang sehingga bisa melakukan overwrite terhadap database
    # KAMUS LOKAL
        # Variabel
            # arr_data : array { array yang merupakan elemen _gadget atau _consumable }
            # arr_data_all_string : array of string { untuk skema konversi array database menjadi string }
            # arrayProcess : array of array of string { array yang ingin diproses }
            # string_data : string { untain informasi dari database [lokal] }
    # ALGORITMA
    if code == 'C':
        arrayProcess = _consumable
    elif code == 'G':
        arrayProcess = _gadget

    string_data = ""
    for arr_data in arrayProcess:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"

    return string_data

def overwrite_database(code): # [ *** SUDAH ADA DI F06 *** ] { sedikit berbeda dengan di F06 }
    # melakukan overwrite terhadap konten database [digunakan dalam skema penggantian jumlah item pada csv]
    # KAMUS LOKAL
        # datas_as_string : string { untain informasi dari database [lokal] }
        # f : textIOWrapper
    # ALGORITMA
    datas_as_string = convert_datas_to_string(idPengembalian[0])
    if code == 'C':
        f = open("consumable.csv","w")
    elif code == 'G':
        f = open("gadget.csv","w")
    f.write(datas_as_string) # melakukan overwrite terhadap isi database
    f.close()

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

def isIDinDatabase(id,database): # [ *** SUDAH ADA DI F05 *** ]
    # memeriksa apakah ID item ada di suatu array database apa tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if id == element[0]: # lokasi id ada di kolom pertama
            return True
    return False

def isUserinDatabase(user,database):
    # memeriksa apakah user ada di array _user atau tidak
    # KAMUS LOKAL
        # element : array of string { baris pada database }
    # ALGORITMA
    for element in database:
        if user == element[1]: # lokasi username ada di kolom kedua
            return True
    return False

def infoBarang(id,spek):
    # mendapatkan informasi barang dari database
    # KAMUS LOKAL
        # Variabel
            # arrayProcess : array of array of string { array tempat item berada }
            # baris : baris pada arrayProcess { untuk skema pencarian }
    # ALGORITMA
    if id[0] == 'C':
        arrayProcess = _consumable
    elif id[0] == 'G':
        arrayProcess = _gadget
    else:
        arrayProcess = []

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
    else:
        return "user tidak ada pada database."

def Inventory(user):
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

    for riwayat in _gadgetBorrowHistory: # jumlah positif
        if riwayat[1] == infoUser(user,'id'):
            if riwayat[2] not in arrayBarangPinjam:
                arrayBarangPinjam.append(riwayat[2])
                arrayJumlahPinjam.append(int(riwayat[4]))
            else:
                arrayJumlahPinjam[arrayBarangPinjam.index(riwayat[2])] += int(riwayat[4])

    for riwayat in _gadgetReturnHistory: # jumlah negatif
        # asumsi: total jumlah barang yang dikembalikan TELAH DIVALIDASI kurang dari sama dengan jumlah barang yang dipinjam
            # maka data jumlah barang pasti >= 0
        if riwayat[1] == infoUser(user,'id'):
            arrayJumlahPinjam[arrayBarangPinjam.index(riwayat[2])] -= int(riwayat[4])

    # menghapus yang neto jumlah sama dengan nol { berarti semua barang yang sempat dipinjam, telah dikembalikan }
    for data in arrayJumlahPinjam:
        if data == 0:
            arrayBarangPinjam.remove(arrayBarangPinjam[arrayJumlahPinjam.index(data)])
            arrayJumlahPinjam.remove(data)

    # menampilkan barang-barang yang telah dipinjam dalam bentuk list:
    for k in range(len(arrayBarangPinjam)):
        print(f"{k+1}. {infoBarang(arrayBarangPinjam[k],'nama')}     || jumlah : {arrayJumlahPinjam[k]}")

def kembalikanGadget():
    # prosedur mengembalikan gadget ke gadget.csv dan mendata riwayatnya ke gadget_return_history.csv
    # KAMUS LOKAL
        # Variabel
            # dataKembali : string { string data pengembalian [ yang akan ditulis ke gadget_return_history.csv ]}
    # ALGORITMA
        # menambahkan riwayat pengembalian ke gadget_return_history.csv
    id_pengembali = infoUser(userAktif,'id')
    id_transaksi = f"{id_pengembali}{idPengembalian}{tanggalPengembalian[0:2]}{tanggalPengembalian[3:5]}{tanggalPengembalian[6:]}"

    dataKembali = f"{id_transaksi},{id_pengembali},{idPengembalian},{tanggalPengembalian},{jumlahPengembalian}\n"
    gh = open("gadget_return_history.csv","a")
    gh.write(dataKembali)
    gh.close()

        # mengubah jumlah barang yang tersedia [bertambah setelah pengembalian] pada gadget.csv
    modify_datas(_gadget,locIDinArray(_gadget,idPengembalian),3,int(infoBarang(idPengembalian,'jumlah'))+jumlahPengembalian)
    overwrite_database('G')

# ALGORITMA UTAMA
userAktif = "bostang123" # user yang aktif akan disesuiakan dengan fungsionalitas login [ F02 ]
arrayBarangPinjam = [] # array berisi barang yang dipinjam dan jumlah barang yang dipinjam
arrayJumlahPinjam = [] # array berisi JUMLAH barang yang dipinjam
        # perhatikan bahwa elemen arrayBarangPinjam dan arrayJumlahPinjam saling berkorespondensi

    # mengakses database dalam bentuk array
g = open("gadget.csv","r")
u = open("user.csv","r")
gb = open("gadget_borrow_history.csv","r")
gr = open("gadget_return_history.csv","r")

raw_lines_g = g.readlines()
raw_lines_u = u.readlines()
raw_lines_gb = gb.readlines()
raw_lines_gr = gr.readlines()

g.close()
u.close()
gb.close()
gr.close()

lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]
lines_u = [raw_line.replace("\n", "") for raw_line in raw_lines_u]
lines_gb = [raw_line.replace("\n", "") for raw_line in raw_lines_gb]
lines_gr = [raw_line.replace("\n", "") for raw_line in raw_lines_gr]

_gadget = []
_user = []
_gadgetBorrowHistory = []
_gadgetReturnHistory = []

for line in lines_g:
    array_of_data = convert_line_to_data(line)
    _gadget.append(array_of_data)
for line in lines_u:
    array_of_data = convert_line_to_data(line)
    _user.append(array_of_data)
for line in lines_gb:
    array_of_data = convert_line_to_data(line)
    _gadgetBorrowHistory.append(array_of_data)
for line in lines_gr:
    array_of_data = convert_line_to_data(line)
    _gadgetReturnHistory.append(array_of_data)

    # menampilkan inventori [ daftar barang yang telah dipinjam ]
Inventory(userAktif)

    # skema pengembalian barang
        # validasi input pengembalian
kondisiLanjut = False
nomorPengembalian = int(input("Masukan nomor peminjaman: "))
if nomorPengembalian > 0 and nomorPengembalian <= len(arrayBarangPinjam):
    idPengembalian = arrayBarangPinjam[nomorPengembalian -1]
    tanggalPengembalian = input("Tanggal pengembalian: ")
    jumlahPengembalian = int(input(f"Masukkan jumlah {infoBarang(idPengembalian,'nama')} yang mau dikembalikan: "))
    if jumlahPengembalian > arrayJumlahPinjam[nomorPengembalian-1]: # jangan lupa aritmatika indeks -1
        print("Pengembalian item gagal! Jumlah barang yang ingin dikembalikan lebih dari yang dipinjam")
    elif jumlahPengembalian <= 0:
        print("Pengembalian item gagal! Jumlah barang yang ingin dikembalikan tidak valid! ")
    else: # input valid
        kondisiLanjut = True
else:
    print("nomor barang yang ingin dikembalikan tidak sesuai!")

if kondisiLanjut:
    kembalikanGadget()
