
#Membaca file user.csv dan menutup file user.csv
f = open("user.csv", "r")
raw_barisan = f.readlines()
f.close()
barisan = [raw_baris.replace("\n", "") for raw_baris in raw_barisan]

def konversi_dari_baris_ke_data(baris):
    raw_array_dari_data = baris.split(",")
    array_dari_data = [data.strip() for data in raw_array_dari_data]
    return array_dari_data

def konversi_array_data_ke_nilai_asli(array_data):
    arr_cpy = array_data[:]
    for i in range(6):
        if(i == 0):
            arr_cpy[i] = int(arr_cpy[i])   
        else:
            arr_cpy[i] = str(arr_cpy[i])
    return arr_cpy

raw_awal = barisan.pop(0)
data_awal = konversi_dari_baris_ke_data(raw_awal)
data_data = []

for baris in barisan:
    array_dari_data = konversi_dari_baris_ke_data(baris)
    nilai_asli = konversi_array_data_ke_nilai_asli(array_dari_data)
    data_data.append(nilai_asli)


def konversi_data_ke_string():
    string_data = ",".join(data_awal) + "\n"
    for arr_data in data_data:
        arr_data_semua_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_semua_string)
        string_data += "\n"
    return string_data

#procedure register (input: username,nama,alamat,password berupa string, output: string_data)
# I.S : User memeasukkan input nama, username, pasword, dan alamat lalu menyimpan hasil input ke dalam database
# F.S. : Program mengeluarkan output dengan perintah 

#KAMUS
#username, password, nama, alamat, : string
#output : string

#ALGORITMA
def register():
    register_indeks = data_data[-1][0] + 1
    nama = input("Masukkan nama:")
    username = input('Masukkan username:')
    password = input('Masukkan password:')
    alamat = input('Masukkan alamat:')
    user_baru = [register_indeks,username,nama,alamat,password,'']
    return user_baru
#ASUMSI: input data diasumsikan benar dengan input data berupa string

#Data input ditambahkan ke dalam data utama
data_data.append(register())
#Pencarian data username
data_username = data_data[-1][1]

#Data disimpan dalam file utama
data_sebagai_string = konversi_data_ke_string()
f = open("user.csv", "w")
f.write(data_sebagai_string)
f.close() 

#output sebagai tanda file telah berhasil diinputkan
print('User',data_username, "telah berhasil regoster ke dalam Kantong Ajaib")
