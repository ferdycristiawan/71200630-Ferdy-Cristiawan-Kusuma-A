#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program chat otomatis berupa daftar menu untuk membantu pelanggan agar tidak perlu mengantri panjang. Program berupa daftar menu
yang ada di KFC. Ada beberapa fitur yang ada di chat tersebut yaitu :
1. Menu untuk pesan Ayam, Makanan lain selain ayam, Minuman
2. Fitur melihat daftar pesanan kita yang telah kita pesan
3. Fitur logout
Jika pelanggan telah logout dan sudah memesan suatu menu yg telah disediakan, maka otomatis daftar pesanan yang telah dibuat akan dirubah
dalam bentuk file txt dan akan dikirim ke kasir untuk diproses pesanannya. Adapun syarat dalam pilihan2 tersebut yaitu :
- Jika pilihan 1(ayam), maka user diminta untuk menginputkan jenis ayam, jumlah ayam dan akan keluar output pesanan berhasil
- jika pilihan 2(makanan lain), maka user diminta menginputkan jenis makanan,jumlah makanan dan akan keluar output pesanan berhasil
- Jika pilihan 3(Minuman),maka user diminta menginputkan jenis minuman,jumlah minuman dan akan keluar output pesanan berhasil
- Jika pilihan 4(Melihat daftar pesanan), maka output akan menampilkan daftar pesanan yang telah kita buat
- Jika pilihan 5(Exit), maka akan keluar dari menu
- Jika pilihan bukan 1,2,3,4,5 maka akan menampilkan pesan bahwa input salah dan kembali ke menu
'''

'''
Input : input pilihan, input pesanan dalam pilihan, input fungsi open file mode append
Proses : membuat daftar menu, perintah write file,perintah close file, perintah readlines
Output : daftar pesanan dalam bentuk file txt
'''

yes = True

while yes :
    print("Selamat datang di KFC. Berikut pilihan menunya")
    print("1.Ayam")
    print("2.Makanan lain")
    print("3.Minuman")
    print("4.Lihat Daftar pesanan")    
    print("5.Exit")
    inp = int(input("Masukkan pilihan Anda :"))
    if inp == 1 :
        menu = open("DaftarPesanan.txt",'a')
        jenisAyam = input("Jenis Ayam :")
        jumlahAyam = input("Masukkan berapa banyak potong ayam :")
        menu.write(jenisAyam+" | "+jumlahAyam)
        menu.write("\n")
        print(jenisAyam,"sebanyak",jumlahAyam,"telah ditambahkan ke daftar pesanan")
        menu.close()

    elif inp == 2 :
        menu2 = open("DaftarPesanan.txt",'a')
        jenisMakanan = input("Jenis Makanan :")
        jumlahMakanan = input("Jumlah Makanan:")
        menu2.write(jenisMakanan+" | "+jumlahMakanan)
        menu2.write("\n")
        print(jenisMakanan,"sebanyak",jumlahMakanan,"telah ditambahkan ke daftar pesanan")
        menu2.close()
    
    elif inp == 3 :
        menu3 = open("DaftarPesanan.txt",'a')
        minuman = input("Jenis Minuman :")
        jumlah = input("Berapa banyak ?")
        print(minuman,"sebanyak",jumlah,"telah ditambahkan ke daftar pesanan")
        menu3.write(minuman+" | "+jumlah)
        menu3.close()

    elif inp == 4 :
        lihat = open("DaftarPesanan.txt",'r')
        baca = lihat.readlines()
        for i in baca :
            kata = i
            nama,jml = kata.split("|",2)
            print("Makanan/Minuman \t Jumlah")
            print(nama+" \t \t "+jml)
        lihat.close()

    elif inp == 5 :
        print("Berhasil keluar")
        yes = False
    else :
        print("Pesanan anda tidak ada di menu. Silakan pesan lagi")