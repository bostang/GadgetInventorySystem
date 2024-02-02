# Gadget Inventory System

Anggota:

1. Diffa' Shada 'Aqila(16520070)
2. Bostang palaguna (16520090)
3. Muhammad Daris Nurhakim (16520170)
4. Joshi Ryu Setiady(16520230)

## Deskripsi Sistem

Sistem inventarisasi gadget ini menggunakan metode simulasi dengan asumsi pengguna dapat menginput informasi sebebas-bebasnya. Informasi yang diinputkan oleh
pengguna disimpan dalam suatu folder tertentu dan file berformat CSV(Comma Separated
Values) untuk memisahkan input pengguna sesuai spesifikasi database simulator. Berikut adalah
spesifikasi dan ketentuan dari prosedur yang ada:

1. Prosedur `login`, Prosedur untuk meminta input dari pengguna sesuai dengan data yang
   diinputkan ke dalam sistem
2. Prosedur `register`, Prosedur untuk mendaftarkan keanggotaan pengguna ke dalam simulator
3. Prosedur `cari_rarity`, Prosedur untuk mencari kelangkaan sebuah item gadget dalam database
   simulator
4. Prosedur `cari_tahun`, Prosedur untuk mencari item gadget sesuai tahun yang diinputkan,
   tahun dapat diinputkan sesuai maupun tahun setelahnya dan tahun sebelumnya
5. Prosedur `tambah_item`, Prosedur untuk memasukkan item gadget baru ke dalam database
   simulator
6. Prosedur `hapus_item`, Prosedur untuk menghapus data item gadget di dalam database
   simulator
7. Prosedur `ubah_jumlah`, Prosedur untuk mengubah jumlah item gadget yang tersedia dalam
   database simulator8. Prosedur pinjam_gadget, Prosedur untuk meminjam item gadget dengan jumlah tertentu dan
   menginput tanggal peminjaman dari dalam database simulator
8. Prosedur `kembalikan_gadget`, Prosedur untuk mengembalikan item gadget dengan jumlah
   tertentu dan memasukkan tanggal pengembalian ke dalam database simulator
9. Prosedur `minta_consumable`, Prosedur untuk meminta item consumable dengan jumlah
   tertentu dan dan memasukkan tanggal permintaan ke dalam database simulator
10. Prosedur `riwayat_pinjam`, Prosedur untuk menampilkan data rekam jejak peminjaman item
    gadget dari dalam database simulator
11. Prosedur `riwayat_kembali`, Prosedur untuk menampilkan data rekam jejak pengembalian
    item gadget ke dalam database simulator
12. Prosedur `riwayat_ambil`, Prosedur untuk menampilkan data rekam jejak permintaan item
    consumable dari dalam database simulator
13. Prosedur `load_data`, Prosedur untuk menampilkan loading data ke dalam nama folder yang
    diinputkan untuk menjalankan program pertama kali
14. Prosedur `save_data`, Prosedur untuk menyimpan semua data input dari pengguna ke dalam
    masing-masing file bertipe CSV
15. Prosedur `help`, Prosedur untuk menampilkan perintah command bantuan untuk mengakses
    setiap fungsi dalam simulator
16. Prosedur `exit`, Prosedur untuk menghentikan seluruh aktivitas dalam sistem inventarisasi
    gadget sesuai input pengguna

## Desain *Command*

1. `$ register`

```
> Masukkan nama:
> Masukkan username:
> Masukkan password:
> Masukkan alamat:
> User {username} telah berhasil register ke dalam Kantong Ajaib.
```

2. `$ login`

```
> Masukkan username:
> Masukkan password:
> Halo {username}! Selamat datang di Kantong Ajaib.
```

3. `$ cari_rarity`

```
> Masukkan rarity:
> Hasil pencarian:
```

4. `$ cari_tahun`

```
> Masukkan tahun:
> Masukkan kategori:
> Hasil pencarian:
```

5. `$ tambah_item`

```
> Masukkan ID:> Masukkan Nama:
> Masukkan Deskripsi:
> Masukkan Jumlah:
> Masukkan Rarity:
> Masukkan Tahun Ditemukan:
```

6. `$ hapus_item`

```
> Masukkan ID item:
> Apakah Anda yakin ingin menghapus {nama item}? (y/n)
```

7. `$ ubah_jumlah`

```
> Masukkan ID:
> Masukkan Jumlah:
> {jumlah item} {nama item} berhasil {ditambahkan/dibuang}. Stok sekarang: {jumlah
> item yang baru}
```

8. `$ pinjam_gadget`

```
> Masukkan ID item:
> Tanggal peminjaman:
> Jumlah peminjaman:
> Item {nama gadget} (×{jumlah peminjaman}) berhasil dipinjam!
```

9. `$ kembalikan_gadget`

```
> {list nama gadget yang dipinjam}
> Masukkan nomor peminjaman:
> Tanggal pengembalian:
> Item {nama gadget} (×{jumlah peminjaman}) telah dikembalikan!
```

10. `$ minta_consumable`

```
> Masukkan ID item:
> Jumlah:
> Tanggal permintaan:
> Item {nama gadget} (×{jumlah peminjaman}) telah berhasil diambil!
```

11. `$ riwayat_pinjam`

```
> Riwayat peminjaman:
> Apakah Anda mau ke halaman selanjutnya? (y/n)
> Semua riwayat sudah ditampilkan
```

12. `$ riwayat_kembali`

```
> Riwayat pengembalian:
> Apakah Anda mau ke halaman selanjutnya? (y/n)
> Semua riwayat sudah ditampilkan
```

13. `$ riwayat_ambil`

```
> Riwayat pengambilan:
> Apakah Anda mau ke halaman selanjutnya? (y/n)> Semua riwayat sudah ditampilkan
```

14. `$ load_data`
15. `$ save_data`

```
> Masukkan nama folder penyimpanan:
> Saving…
> Data telah disimpan pada folder {nama folder}!
```

16. `$ help`

```
> {Penjelasan mengenai prosedur yang ada}
```

17. `$ exit`

```
> Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)
```

## Desain Kamus Data

### Desain Kamus Data Lokal untuk fungsi utama dalam program

```vb
function clear_screen
(
	cls: string_os -untuk membersihkan tampilan di program
)
```


```vb
function splitList
(
	database: array_of_string
	splitList: array_of_string -digunakan pemisah delimiter ;
)
```

```vb
function convert_line_to_data
(
	array_from_data: array_of_string
	array_from_data: splitList array_of_string
)
```

```vb
function convert_array_to_real_value
(
  array_of_data: array_of_string
  array:data: integer, array_of_string
)
```

```vb
function overwrite_database
(
  datas_as_string: string
  array_database from csv
)
```

### Desain Kamus Data Tambahan untuk tiap fungsi utama
```vb
Array_of_data:array of string
g: textIOwrapper
c: textIOwrapper
id_remove: string
kondisiLanjut: boolean
ArrayJumlahPinjam: array of integer
ArrayBarangPinjam: array of string
idUbah: string
idPinjam: string
idPengembalian: string
idConsumable: string
ubahJumlah: integer-
jumlahPengembalian: integer
tanggalPengembalian: string
tanggalPinjam: string
raw_lines_g: array of character
raw_lines_c: array of character
raw_lines_u: array of character
raw_lines_gb: array of character
_gadget: array_database from file csv
_consumable: array_database from file csv
_user: array_database from file csv
lines_g: array_of_character
lines_c : array_of_character
```
### Desain Kamus Data Lokal untuk setiap fungsi
#### F01
 
```vb
function add_item_to_database
(
    data_baru: list_of_string
    _user:array_of_string
)
```
```vb
function user_list
(
    nama_user: list_of_string,array_of_string
    output: boolean_of_array
)
```
```vb
function register
(
    username, nama,password,alamat: string
    output: string
)
```

#### F02
```vb
function user_list
(
    nama_user: list_of_string,array_of_string
    output: boolean_of_array
)
```
```vb
function password_list
(
    password: list_of_string,array_of_string
    output: boolean_of_array
)
```
```vb
function id_user
(
    id_user: list_of_string,array_of_string
    output: boolean_of_array
)
```
```vb
function login
(
    username,password:string
    output:string
)
```

#### F03
```vb
function isRarityinDatabase
(
    element:array of string
    output: array of boolean
)
```
```vb
function infoBarang
(
    arrayProcess:array of string
    output: baris:array of string
)
```
```vb
function cariRarity
(
    rarityitem:string
    output: string
)
```
#### F04
```vb
function IsTahuninDatabase
(
    element: array of string
    output: array of boolean
)
```
```vb
function infoBarang
(
    arrayProcess:array of string
    output: baris:array of string
)
```
```vb
procedure cariTahun
(
    tahun,kategori:string
    output: list of string
)
```

#### F05
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function add_item_to_database
(
    data_baru: list_of_string
    _user:array_of_string
)
```
```vb
function tambah_item
(
    id,nama,deskripsi,jumlah,rarity,tahuntemu:string
    output: string
)
```

#### F06
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoBarang
(
    arrayProcess:array_of_string
    baris:array_of_string
)
```
```vb
function hapusItem
(
    konfirmasi: string
    output: string
)
```

#### F07
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function convert_to_real
(
    array_salinan: array of array of integer
    kolom_jumlah: integer
    baris: array of string
    output: array of string
)
```
```vb
function change_quantity_in_database
(
    arrayProcess: array of array of integer
    baris: array of integer
    arrayProcess: array_of_string
)
```
```vb
function infoBarang
(
    arrayProcess: array of string
    baris: array of string
)
```
```vb
procedure ubahJumlah
(
    idUbah, jumlahUbah: string 
    hasilUbah: array of string
    output: string
)
```

#### F08
```vb
function modify_datas
(
    output: array of data
)
```
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function isUserinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoBarang
(
    arrayProcess:array_of_string
    baris:array_of_string
)
```
```vb
function isLocIDinArray
(
    k: integer
)
```
```vb
function infoUser
(
    baris: array_of_string
    baris: array_of_string,string
)
```
```vb
function infoPinjam
(
    arrayProcess: array_of_string
    baris: array_of_string dari arrayProcess
)
```
```vb
function pinjamGadget
(
    idPinjam, tanggalPinjam,JumlahPinjam: string, character
    output: string
    )
```
#### F09
```vb
function modify_datas
(
    output: array_of_datafunction isIDinDatabase
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function isUserinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoBarang
(
    arrayProcess:array_of_string
    baris:array_of_string
)
```
```vb
function isLocIDinArray
(
    k: integer
)
```
```vb
function infoUser
(
    baris: array_of_string
    baris: array_of_string,string
)
```
```vb
function inventory
(
    riwayat: array_of_string
    k: integer
)
```
```vb
function infoPinjam
(
    arrayProcess: array_of_string
    baris: array_of_string dari arrayProcess
)
```
```vb
function infoKembali
(
    arrayProcess: array_of_string
    baris: array_of_string dari arrayProcess
)
```
```vb
function kembalikanGadget
(
    dataKembali: string_to_database_csv
    output: array_of_string_from_database
)
```

#### F10
```vb
function modify_datas
(
    output: array_of_data
)
```
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function isUserinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoBarang
(
    arrayProcess:array_of_string
    baris:array_of_string
)
```
```vb
function isLocIDinArray
(
    k: integer
)
```
```vb
function infoUser
(
    baris: array_of_string
    baris: array_of_string,string
)
```
```vb
function mintaConsum
(
    idPeminta: string
    jumlahPermintaan: integer
    output : string
)
```
#### F11
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function isUserinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoBarang
(
    arrayProcess:array_of_string
    baris:array_of_string
)
```
```vb
function isLocIDinArray
(
    k: integer
)
```
```vb
function infoUser
(
    baris: array_of_string
    baris: array_of_string,string
)
```
```vb
function infoPinjam
(
    arrayProcess: array_of_string
    baris: array_of_string dari arrayProcess
)
```
```vb
procedure riwayatPinjam
(
    lanjut: string
    output: list_of_string, array_of_string
)
```
#### F12
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function isUserinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoBarang
(
    arrayProcess:array_of_stringbaris:array_of_string
)
```
```vb
function infoUser
(
    baris: array_of_string
    baris: array_of_string,string
)
```
```vb
function infoPinjam
(
    arrayProcess: array_of_string
    baris: array_of_string dari arrayProcess
)
```
```vb
function isPinjamInDatabase
(
    element: array_of_string
    output: boolean_of_array
)
```
```vb
function infoKembali
(
    arrayProcess: array_of_string
    baris: array_of_string dari arrayProcess
)
```
```vb
procedure riwayatKembali
(
    lanjut: string
    output: list_of_string, array_of_string
)
```

#### F13
```vb
function isIDinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function isUserinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoBarang
(
    arrayProcess:array_of_string
    Baris:array_of_string
)
```
```vb
function infoUser
(
    baris: array_of_string
    baris: array_of_string,string
)
```
```vb
function infoAmbil
(
    arrayProcess: array_of_string
    baris: array_of_string dari arrayProcess
)
```
```vb
function riwayatAmbil
(
    lanjut: string
    output: list_of_string, array_of_string
)
```

#### F15
```vb
function simpan
(
    folder : stringtype folder
    c: string
    ch: string
    gb: string
    g: string
    gr: string
    u: string
    Folder:
        SEQFILE of :
        (1) consumable.csv
        (2) gadget.csv
        (3) consumable_history.csv
        (4) gadget_borrow_history.csv
        (5) gadget_return_history.csv
        (6) user.csv
)
```

#### F16

```vb
function isUserinDatabase
(
    element:array_of_string
    output: boolean_of_array
)
```
```vb
function infoUser
(
    baris: array_of_string
    baris: array_of_string,string
)
```
```vb
function help
(
    output: string
)
```

#### F17
```vb
function keluar
(
    save : string
    output: string
)
```
