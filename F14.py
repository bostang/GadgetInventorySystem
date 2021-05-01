"""
Load Data

Prosedur ini digunakan untuk melakukan loading data ke dalam sistem. Prosedur ini akan otomatis
dijalankan ketika sistem mulai pertama kali bila diberikan input nama folder yang berisi file
penyimpanan. Semua file penyimpanan dijamin ada dan memiliki nama yang fixed, seperti yang tertera
pada bagian struktur data eksternal.

Kontributor : Joshi Ryu Setiady (16520230)
"""
# UNTUK SEMENTARA, LANGSUNG DIIMPLEMENTASIKAN KE PROGRAM UTAMA KANTONGAJAIB.PY
import argparse
import os
from Basic_Procedure import *

def load():
    # Untuk mencari file di folder tersebut
    parser = argparse.ArgumentParser(usage='python kantongajaib.py <folder_name>')
    parser.add_argument('folder_name', help="Masukkan nama folder tempat penyimpanan", default=None)
    args = parser.parse_args()
    if args.folder_name is not None:
        try:
            if __name__ == "__main__":
                for (root,dirs,files) in os.walk(args.folder_name, topdown=True):
                    path = root
                    nama_file = files
        except SyntaxError:
            print('Tidak ada nama folder yang diberikan!')
            print("Usage : python kantongajaib.py <nama_folder>")
    else:
        print('Tidak ada nama folder yang diberikan!')    # In case kepake (harusnya engga)
        print("Usage : python kantongajaib.py <nama_folder>")

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
        # Menyimpan array dari file csv untuk dipakai di fungsi lain
    except UnboundLocalError:
        print('Tidak ada nama folder yang diberikan!')
        print("Usage : python kantongajaib.py <nama_folder>")

    
    