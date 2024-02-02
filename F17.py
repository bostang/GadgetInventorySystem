"""
Exit

Seperti namanya, fungsi ini adalah fungsi untuk keluar dari aplikasi. Fungsi dapat menerima huruf
kapital maupun huruf kecil. Pastikan masukan valid.

Kontributor : Joshi Ryu Setiady (16520230)
"""

from F15 import *
from Basic_Procedure import clear_screen
import os

def keluar(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user):
    loop = True
    while loop:
        clear_screen()
        save = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if (save == 'y') or (save == 'Y'):
            simpan(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user)
            exit()
        elif (save == 'n') or (save == 'N'):
            exit()
        else:
            print("Masukkan salah. Mohon ulangi")
            os.system('pause')
