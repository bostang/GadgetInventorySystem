#Fungsi help untuk menampilkan command input dari user/admin
#kemudian mereturn print sesuai command yang user/admin butuhkan

#User/admin tidak perlu login untuk menggunakan fitur ini

def help(): 
    #Akses : admin
    print('COMMAND TEXT HELP UNTUK AKSES ADMIN')  
    print('============= HELP ===========')#tampilan help untuk akses admin
    print('register - untuk melakukan registrasi user baru')
    print('login - untuk melakukan login ke dalam sistem')
    print('tambahitem - untuk melakukan penambahan item')
    print('carirarity - untuk mencari item berdasarkan tingkat rarity suatu item')
    print('caritahun - untuk mencari item berdasarkan input tahun yang diberikan')
    print('hapusitem - untuk menghapus suatu item dari database')
    print('ubahjumlah - untuk mengubah jumlah suatu item dalam database')
    print('riwayatpinjam - untuk menampilkan riwayat peminjaman suatu item dalam gadget')
    print('riwayatkembali - untuk menampilkan riwayat pemngembalian suatu item dalam gadget')
    print('riwayatambil - untuk menampilkan riwayat pengambilan consumable suatu item dalam database')
    print('save - untuk menyimpan data ke dalam suatu file setelah diubah')
    print('help - untuk menampilkan command sesuai kebutuhan user/admin')
    #Akses : user
    print('COMMAND TEXT HELP UNTUK AKSES USER')   
    print('============= HELP ===========')#tampilan help untuk akses user
    print('login - untuk melakukan login ke dalam sistem')
    print('carirarity - untuk mencari item berdasarkan tingkat rarity suatu item')
    print('caritahun - untuk mencari item berdasarkan input tahun yang diberikan')
    print('pinjam - untuk meminjam suatu item gadget dalam database')
    print('kembalikan - untuk mengembalikan suatu item gadget yang dipinjam')
    print('minta - untuk memingta consumable yang tersedia dalam database')
    print('save - untuk menyimpan data ke dalam suatu file setelah diubah')
    print('help - untuk menampilkan command sesuai kebutuhan user/admin')  

help() 



