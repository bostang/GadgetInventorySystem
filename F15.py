"""
Save Data

Prosedur ini digunakan untuk melakukan penyimpanan data ke dalam file setelah dilakukan
perubahan. Misalnya, setelah melakukan peminjaman atau pengembalian tanpa di-save, data tersebut
tidak akan tersimpan pada file.

Kontributor : Joshi Ryu Setiady (16520230)
"""

import os

def convert_data_to_list_string(array):
    _simpan = []
    for arr_data in array:
        if (len(arr_data) == 5):
            string = str(arr_data[0]+";"+arr_data[1]+";"+arr_data[2]+";"+arr_data[3]+";"+arr_data[4]+"\n")
        elif (len(arr_data) == 6):
            string = str(arr_data[0]+";"+arr_data[1]+";"+arr_data[2]+";"+arr_data[3]+";"+arr_data[4]+";"+arr_data[5]+"\n")
        _simpan.append(string)
    _simpan[len(_simpan)-1] = _simpan[len(_simpan)-1].replace("\n","")
    return _simpan

def file(_array, nama_file, tipe, path):
    x = open(os.path.join(path, nama_file), tipe)
    x.writelines(convert_data_to_list_string(_array))
    x.close()

def simpan(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user):
    folder = str(input("Masukkan nama folder penyimpanan : "))
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, folder)
    try:
        os.mkdir(path)
        print("Saving...")
        file(_consumable, "consumable.csv", "w+", path)
        file(_consumableHistory, "consumable_history.csv", "w+", path)
        file(_gadget, "gadget.csv", "w+", path)
        file(_gadgetBorrow, "gadget_borrow_history.csv", "w+", path)
        file(_gadgetReturn, "gadget_return_history.csv", "w+", path)
        file(_user, "user.csv", "w+", path)
        print(f"Data telah disimpan pada folder {folder}!")
        os.system('pause')
    except FileExistsError:
        print("Saving...")
        file(_consumable, "consumable.csv", "w", path)
        file(_consumableHistory, "consumable_history.csv", "w", path)
        file(_gadget, "gadget.csv", "w", path)
        file(_gadgetBorrow, "gadget_borrow_history.csv", "w", path)
        file(_gadgetReturn, "gadget_return_history.csv", "w", path)
        file(_user, "user.csv", "w", path)
        print(f"Data telah disimpan pada folder {folder}!")
        os.system('pause')

