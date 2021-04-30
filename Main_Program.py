# Program Inventarisasi Gadget

from Basic_Procedure import *
from F01 import *
from F02 import *
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
from F14 import *
from F15 import *
from F16 import *
from F17 import *


exitprogram = False
loop = True
while not exitprogram:
    print("""
Program Inventarisasi Gadget Doraemonangis : 
1. Login
2. Help
3. Exit
(Masukkan angka saja)
    """)
    menu_utama = str(input("Masukkan pilihan : "))
    if menu_utama == '1':
        login()
        while loop:
            if role == 'admin':
                print("""
Menu Utama Admin :
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
                    test # untuk F01
                    loop = False
                elif menu_admin == '2':
                    test # untuk F03
                    loop = False
                elif menu_admin == '3':
                    test # untuk F04
                    loop = False
                elif menu_admin == '4':
                    test # untuk F05
                    loop = False
                elif menu_admin == '5':
                    test # untuk F06
                    loop = False
                elif menu_admin == '6':
                    test # untuk F07
                    loop = False
                elif menu_admin == '7':
                    test # untuk F11
                    loop = False
                elif menu_admin == '8':
                    test # untuk F12
                    loop = False
                elif menu_admin == '9':
                    test # untuk F13
                    loop = False
                elif menu_admin == '10':
                    test # untuk F15
                    loop = False
                elif menu_admin == '11':
                    test # untuk F16
                    loop = False
                elif menu_admin == '12':
                    test # untuk F17
                    loop = False
                else:
                    clear_screen()
                    print("Masukkan salah. Mohon ulangi")
                    os.system('pause')
            if role == 'user':
                print("""
Menu Utama User :
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
                    loop = False
                elif menu_user == '2':
                    test # untuk F04
                    loop = False
                elif menu_user == '3':
                    test # untuk F08
                    loop = False
                elif menu_user == '4':
                    test # untuk F09
                    loop = False
                elif menu_user == '5':
                    test # untuk F10
                    loop = False
                elif menu_user == '6':
                    test # untuk F15
                    loop = False
                elif menu_user == '7':
                    test # untuk F16
                    loop = False
                elif menu_user == '8':
                    test # untuk F17
                    loop = False
                else:
                    clear_screen()
                    print("Masukkan salah. Mohon ulangi")
                    os.system('pause')
    elif menu_utama == '2':
        bantuan() # untuk F16
    elif menu_utama == '3':
        exit()
    else:
        clear_screen()
        print("Masukkan salah. Mohon ulangi")
        os.system('pause')
