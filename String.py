#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program olah kalimat sederhana. Buatlah kalimat tanya secara berulang ulang (pilih yes/no). Pertama, mbuatlah input user sebagai
sebagai string yang nantinya akan diolah ke berbagai bentuk. Program yang ditanyakan yaitu :
1. Mengitung jumlah kalimat
2. Mengubah ke huruf besar semua
3. Membalik kalimat
4. Menampilkan angka saja
Tanyakan keempat pilihan tersebut, jika "yes" maka nanti output keempat pilihan tersebut akan di eksekusi secara bersama, jika "no" maka
akan menampilkan beberapa output saja yang telah dijawab yes. Tetapi jika "no" semua maka output tidak menampilkan apa-apa.
'''

'''
Input  :input user -> masukkan kalimat, hitung kalimat, upeercase,membalik kalimat, menampilkan angka
Proses :fungsi def untuk membuat -> uppercase, membalik kalimat, menampilkan angka
        kontrol percabangan untuk membuat pilihan yes/no
Output : hasil dari program -> masukkan kalimat, hitung kalimat, upeercase,membalik kalimat, menampilkan angka
'''

def besar_kalimat(kalimat) :
    kalimat = kalimat.upper()
    return kalimat

def balik_kalimat(kalimat) :
    str = ''
    for i in kalimat :
        str = i + str
    return str

def tampilan_angka(kalimat) :
    kalimat = kalimat.lower()
    kalimat = ''.join([i for i in kalimat if i.isdigit()])
    return kalimat

print("=====PROGRAM OLAH STRING=====")
kalimat = str(input("Masukkan kalimat : "))

jumlah = str(input("Hitung jumlah kalimat? [yes/no] : "))
besar = str(input("Jadikan huruf besar semua? [yes/no] : "))
balik = str(input("Balik kalimat? [yes/no] : "))
angka = str(input("Tampilkan angka? [yes/no] :"))

if jumlah == "yes" :
    print("Jumlah kalimat :", len(kalimat))
    if besar == "yes" :
        print("Kalimat huruf besar :",besar_kalimat(kalimat))
        if balik == "yes" :
            print("kalimat dibalik :",balik_kalimat(kalimat))
            if angka == "yes" :
                print("Menampilkan angka :",tampilan_angka(kalimat))
