# Program Inventarisasi Gadget

import os, argparse
from Basic_Procedure import *
from F01 import *  #done
from F02 import *  #done
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F15 import *  #done
from F16 import *  #done
from F17 import *  #done
# untuk F14 tidak diimport melainkan langsung diimplementasikan di program utama

exitprogram = False
loop = True

# Fungsi Load
# Untuk mencari file di folder tersebut
parser = argparse.ArgumentParser(usage='python kantongajaib.py <folder_name>')
parser.add_argument('folder_name', help="Masukkan nama folder tempat penyimpanan", default=None)
args = parser.parse_args()
if args.folder_name is not None:
    if __name__ == "__main__":
        for (root,dirs,files) in os.walk(args.folder_name, topdown=True):
            path = root
            nama_file = files
# Untuk mengubah file CSV menjadi array yg bisa dipakai di fungsi lain
try:
    c = open(path+"/"+nama_file[0],"r")
    ch = open(path+"/"+nama_file[1],"r")
    g = open(path+"/"+nama_file[2],"r")
    gb = open(path+"/"+nama_file[3],"r")
    gr = open(path+"/"+nama_file[4],"r")
    u = open(path+"/"+nama_file[5],"r")
    raw_lines_c = c.readlines()
    raw_lines_ch = ch.readlines()
    raw_lines_g = g.readlines()
    raw_lines_gb = gb.readlines()
    raw_lines_gr = gr.readlines()
    raw_lines_u = u.readlines()
    c.close()
    ch.close()
    g.close()
    gb.close()
    gr.close()
    u.close()
    lines_c = [raw_line.replace("\n", "") for raw_line in raw_lines_c]
    lines_ch = [raw_line.replace("\n", "") for raw_line in raw_lines_ch]
    lines_g = [raw_line.replace("\n", "") for raw_line in raw_lines_g]
    lines_gb = [raw_line.replace("\n", "") for raw_line in raw_lines_gb]
    lines_gr = [raw_line.replace("\n", "") for raw_line in raw_lines_gr]
    lines_u = [raw_line.replace("\n", "") for raw_line in raw_lines_u]
    _consumable = []
    _consumableHistory = []
    _gadget = []
    _gadgetBorrow = []
    _gadgetReturn = []
    _user = []
    for line in lines_c:
        array_of_data = splitList(line)
        _consumable.append(array_of_data)
    for line in lines_ch:
        array_of_data = splitList(line)
        _consumableHistory.append(array_of_data)
    for line in lines_g:
        array_of_data = splitList(line)
        _gadget.append(array_of_data)
    for line in lines_gb:
        array_of_data = splitList(line)
        _gadgetBorrow.append(array_of_data)
    for line in lines_gr:
        array_of_data = splitList(line)
        _gadgetReturn.append(array_of_data)
    for line in lines_u:
        array_of_data = splitList(line)
        _user.append(array_of_data)
except UnboundLocalError or NameError:
    print('Tidak ada nama folder yang diberikan!')
    print("Usage : python kantongajaib.py <nama_folder>")
    exit()
# Tampilan load
print("loading...")
print("Selamat Datang di 'Kantong Ajaib'!")
os.system('pause')

# Main Program
while not exitprogram:
    clear_screen()
    print("""Program Kantong Ajaib! : 
1. Login
2. Help
3. Exit
(Masukkan angka saja)
    """)
    menu_utama = str(input("Masukkan pilihan : "))
    if menu_utama == '1':
        clear_screen()
        user_aktif = login(_user)
        while loop:
            if user_aktif[5] == 'admin':
                clear_screen()
                print("""Menu Utama Admin :
1. Register akun baru
2. Pencarian gadget berdasarkan rarity
3. Pencarian gadget berdasarkan tahun ditemukan
4. Menambah item
5. Menghapus gadget / consumable
6. Mengubah jumlah gadget / consumable pada inventory
7. Melihat riwayat peminjaman gadget
8. Melihat riwayat pengembalian gadget
9. Melihat riwayat pengambilan consumable
10. Save
11. Help
12. Exit
(Masukkan angka saja)
                """)
                menu_admin = str(input("Masukkan pilihan : "))
                if menu_admin == '1':
                    clear_screen()
                    register(_user)
                elif menu_admin == '2':
                    test # untuk F03
                elif menu_admin == '3':
                    test # untuk F04
                elif menu_admin == '4':
                    test # untuk F05
                elif menu_admin == '5':
                    test # untuk F06
                elif menu_admin == '6':
                    test # untuk F07
                elif menu_admin == '7':
                    test # untuk F11
                elif menu_admin == '8':
                    test # untuk F12
                elif menu_admin == '9':
                    test # untuk F13
                elif menu_admin == '10':
                    clear_screen()
                    simpan(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user)
                elif menu_admin == '11':
                    clear_screen()
                    bantuan_dalam(user_aktif[5])
                elif menu_admin == '12':
                    keluar(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user)
                else:
                    clear_screen()
                    print("Masukkan salah. Mohon ulangi")
                    os.system('pause')
            if user_aktif[5] == 'user':
                clear_screen()
                print("""Menu Utama User :
1. Pencarian gadget berdasarkan rarity
2. Pencarian gadget berdasarkan tahun ditemukan
3. Meminjam gadget
4. Mengembalikan gadget
5. Meminta consumable
6. Save
7. Help
8. Exit
(Masukkan angka saja)
                """)
                menu_user = str(input("Masukkan pilihan : "))
                if menu_user == '1':
                    test # untuk F03
                elif menu_user == '2':
                    test # untuk F04
                elif menu_user == '3':
                    test # untuk F08
                elif menu_user == '4':
                    test # untuk F09
                elif menu_user == '5':
                    test # untuk F10
                elif menu_user == '6':
                    clear_screen()
                    simpan(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user)
                elif menu_user == '7':
                    clear_screen()
                    bantuan_dalam(user_aktif[5])
                elif menu_user == '8':
                    clear_screen()
                    keluar(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user)
                else:
                    clear_screen()
                    print("Masukkan salah. Mohon ulangi")
                    os.system('pause')
    elif menu_utama == '2':
        clear_screen()
        bantuan_luar()
    elif menu_utama == '3':
        exit()
    else:
        clear_screen()
        print("Masukkan salah. Mohon ulangi")
        os.system('pause')
