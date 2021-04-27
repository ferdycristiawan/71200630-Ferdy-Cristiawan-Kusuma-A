#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program sederhana berisi form untuk memasukkan nim,nama,dan asal. Program berisi perintah input data dari user. Bagian-bagian dari
input sebagai berikut :
- jika user menginput 1, maka input user berupa nim,nama,asal
- jika user menginput 2, maka tampilkan data yang telah kita tambahkan ke dalam dictionary
- jika user menginput 3, maka input user berupa nim dan program akan menghapus data sesuai nim
- jika user menginput 0, maka akan exit
Manfaatkan dictionary dalam program ini!
'''
'''
Input : Input data dari user, variabel list kosong
Proses : Percabangan, perulangan, dictionary utk menambah data
Output : Data yang diinputkan dari user
'''

nim = []
nama = []
asal = []

pilihan = 1
while pilihan != 0 :
    print("1. Masukkan data")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("0. Exit")

    pilihan = int(input("Masukkan pilihan anda :"))
    if pilihan == 1 :
        inp_nim = input("Masukkan NIM :")
        nim.append({'nim' : inp_nim})
        inp_nama = input("Masukkan Nama :")
        nama.append({'nama' : inp_nama})
        inp_asal = input("Masukkan Asal :")
        asal.append({'asal' : inp_asal})

    elif pilihan == 2 :
        show = True
        for i in range (len(nim)) :
            if show :
                print("NIM \t\t Nama \t\t Asal")
            print(nim[i]['nim'],'\t',nama[i]['nama'],'\t',asal[i]['asal'])
            show = False
            
    elif pilihan == 3 :
        inp_nim = input("Masukkan NIM :")
        for i in range(len(nim)) :
            if inp_nim == nim[i]['nim'] :
                print("Data berhasil dihapus.")
                del nim[i]
                del nama[i]
                del asal[i]
                break