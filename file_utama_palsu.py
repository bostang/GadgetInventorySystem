# Program rancangan menu utama

# gambaran besar skema penggabungan file

from test1 import tambah2



aksi = int(input())

while True:
    if aksi == 1:
        from F05 import *
    elif aksi == 2:
        from F06 import *
    elif aksi == 3:
        print('gabut')
        ##aksi = int(input())

    elif aksi == 4:
        print("goodbye boi")
        break
    elif aksi == 5:
        print("mantap")

    aksi = int(input())
