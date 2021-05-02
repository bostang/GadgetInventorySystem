"""
Save Data

Prosedur ini digunakan untuk melakukan penyimpanan data ke dalam file setelah dilakukan
perubahan. Misalnya, setelah melakukan peminjaman atau pengembalian tanpa di-save, data tersebut
tidak akan tersimpan pada file.

Kontributor : Joshi Ryu Setiady (16520230)
"""

import os

def convert_data_to_string(array):
    for arr_data in array:
        arr_data_to_string = [str(text) for text in arr_data]
        string_data = ",".join(arr_data_to_string)
        string_data += "\n"
    return string_data

def simpan(_consumable,_consumableHistory,_gadget,_gadgetBorrow,_gadgetReturn,_user):
    folder = str(input("Masukkan nama folder penyimpanan : "))
    parent_dir = os.getcwd()
    print(parent_dir)
    path = os.path.join(parent_dir, folder)
    try:
        os.mkdir(path)
        c = open(os.path.join(path, "consumable.csv"),"w+")
        ch = open(os.path.join(path, "consumable_history.csv"),"w+")
        g = open(os.path.join(path, "gadget.csv"),"w+")
        gb = open(os.path.join(path, "gadget_borrow_history.csv"),"w+")
        gr = open(os.path.join(path, "gadget_return_history.csv"),"w+")
        u = open(os.path.join(path, "user.csv"),"w+")
        c.write(convert_data_to_string(_consumable))
        ch.write(convert_data_to_string(_consumableHistory))
        g.write(convert_data_to_string(_gadget))
        gb.write(convert_data_to_string(_gadgetBorrow))
        gr.write(convert_data_to_string(_gadgetReturn))
        u.write(convert_data_to_string(_user))
        c.close()
        ch.close()
        g.close()
        gb.close()
        gr.close()
        u.close()
    except FileExistsError:
        c = open(os.path.join(path, "consumable.csv"),"w")
        ch = open(os.path.join(path, "consumable_history.csv"),"w")
        g = open(os.path.join(path, "gadget.csv"),"w")
        gb = open(os.path.join(path, "gadget_borrow_history.csv"),"w")
        gr = open(os.path.join(path, "gadget_return_history.csv"),"w")
        u = open(os.path.join(path, "user.csv"),"w")
        c.write(convert_data_to_string(_consumable))
        ch.write(convert_data_to_string(_consumableHistory))
        g.write(convert_data_to_string(_gadget))
        gb.write(convert_data_to_string(_gadgetBorrow))
        gr.write(convert_data_to_string(_gadgetReturn))
        u.write(convert_data_to_string(_user))
        c.close()
        ch.close()
        g.close()
        gb.close()
        gr.close()
        u.close()