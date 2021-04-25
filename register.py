import os
#Membaca file user.csv dan menutup file user.csv
f = open("user.csv", "r")
raw_barisan = f.readlines()
f.close()
barisan = [raw_baris.replace("\n", "") for raw_baris in raw_barisan]

def bersih():
    # membuat efek clear screen pada Python
    os.system('cls' if os.name == 'nt' else 'clear')

for baris in barisan:
    def split(sentence):
        sentence = ''.join(baris)
        split_list = []
        tmp = ''
        for s in sentence:
            if s == ',':
                split_list.append(tmp)
                tmp = ''
            else:
                tmp += s
        if tmp:
            split_list.append(tmp)
        return split_list


def konversi_dari_baris_ke_data(baris):
    raw_array_dari_data = split(baris)
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

print(data_data)
def konversi_data_ke_string():
    string_data = ",".join(data_awal) + "\n"
    for arr_data in data_data:
        arr_data_semua_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_semua_string)
        string_data += "\n"
    return string_data

bersih()
#procedure register (input: username,nama,alamat,password berupa string, output: string_data)
# I.S : User memeasukkan input nama, username, pasword, dan alamat lalu menyimpan hasil input ke dalam database
# F.S. : Program mengeluarkan output dengan perintah 

#KAMUS
#username, password, nama, alamat, : string
#output : string       

#FUMGSI-FUNGSI TAMBAHAN
def add_item_to_database(register_indeks,username,nama,alamat,password):
    data_baru = f"{register_indeks},{username},{nama},{alamat},{password},user\n"
    f = open('user.csv', 'a')
    f.write(data_baru)
    f.close()

def user_list(nama_user,data_data):
    for element in data_data:
        if nama_user == element[1]:
            return True
    return False    

#ALGORITMA
def register():
    nama = input("Masukkan nama:")
    username = input('Masukkan username:')
    if not user_list(username,data_data):#Cek username yang sama   
        password = input('Masukkan password:')
        alamat = input('Masukkan alamat:')
        register_indeks = data_data[-1][0] + 1
        add_item_to_database(register_indeks,username,nama,alamat,password)
        print('User',username, "telah berhasil register ke dalam Kantong Ajaib")#user telah berhasil register
           
    else:
        print('Username sama. Gagal register!')
        

print(register())#fungsi register dijalankan
