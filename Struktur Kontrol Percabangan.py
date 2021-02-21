#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program kalkulator sederhana untuk menjumlah,mengurang,mengkali dan membagi bilangan
Gunakan input 2 bilangan saja
Jika user salah memasukkan input atau tidak menggunakan bilangan berupa integer, 
maka output akan menampilkan "Anda salah memasukkan input!"
'''

'''
input : bilangan pertama, bilangan  kedua
proses : menjumlah, mengurang, mengkali, dan membagi
output : hasil jumlah,kurang,kali, bagi dari kedua bilangan
'''

print("-----KALKULATOR SEDERHANA-----")
print("Piih operasi")
print("1. Penjumlahan (+) \n2. Pengurangan (-) \n3.Perkalian (x) \n4. Pembagian (:)")
try :
    operasi = int(input("Masukkan pilihan anda :"))

    bilangan1 = float(input("Masukkan bilangan pertama : "))
    bilangan2 = float(input("Masukkan bilangan kedua :"))

    if operasi == 1 :
        hasil_jumlah = bilangan1 + bilangan2
        print("Hasil dari",bilangan1,"+",bilangan2,"=",hasil_jumlah)
    elif operasi == 2 :
        hasil_kurang = bilangan1 - bilangan2
        print("Hasil dari",bilangan1,"-",bilangan2,"=",hasil_kurang)
    elif operasi == 3 :
        hasil_kali = bilangan1 * bilangan2
        print("Hasil dari",bilangan1,"x",bilangan2,"=",hasil_kali)
    else :
        hasil_bagi = bilangan1 / bilangan2
        print("Hasil dari %f : %f = %.2f" % (bilangan1,bilangan2,hasil_bagi))
except :
    print("Anda salah memasukkan input!")