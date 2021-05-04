#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program tentang data diri orang orang, program berupa input data dari user. Data akan dikumpulkan di sebuah list dan nanti akan
di eksekusi sebagai data yang telah disusun berdasarkan Nama,Asal dan Usia. Urutan dari program tersebut sebagai berikut :
1. Membuat input user dengan format nama,asal,usia dalam satu variabel
2. Buatlah input user lagi yaitu berupa pertanyaan, apakah user ingin memasukkan data diri lagi atau tidak
3. Jika user menginput yes, maka kembali ke no.1 yaitu input data diri
4. Jika user menginput no, maka output tertampil sebagai data diri yang sudah terkumpul selama user menginput data
Gunakan list dan tuple untuk menampung data tersebut.
'''
'''
Input : membuat input user, membuat list kosong
Proses : perulangan, percabangan, fungsi lsit dan fungsi tuple
Output : Daftar data diri yang telah dibuat
'''

data = []

while True :
    inp = input("Masukka data diri (nama,asal,usia) :")
    print("Data diri berhasil ditambahkan")
    ask = input("Tambah data diri? [yes/no] :")
    if ask == 'no' :
        for i in inp :
            ubah = list(inp)
            pisah = inp.split(',')
            tpl = tuple(pisah)
        data.append(tpl)
        break
    else :
        for i in inp :
            ubah = list(inp)
            pisah = inp.split(',')
            tpl = tuple(pisah)
        data.append(tpl)

for i in data :
    print("Nama :",i[0])
    print("Asal :",i[1])
    print("Usia :",i[2],'\n')