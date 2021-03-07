#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program menghitung jumlah dan rata-rata dari bilangan-bilangan yang telah ditentukan. Program berupa nilai-nilai siswa di suatu
kelas jika disuatu kelas memiliki sejumlah siswa. Jumlah siswa dan nilai-nilai berupa inputan user. Output yang dihasilkan berupa nilai total
dari suatu kelas dan rata-rata nilai tersebut. Gunakan kontrol perulangan.
'''

'''
Input : jumlah siswa(dari user), data_nilai = [], jumlah = 0  
Proses : memasukkan nilai menggunakan rumus append, menghitung rata-rata
Output : total nilai, rata-rata
'''
print("=====PROGRAM HITUNG RATA-RATA=====")

siswa = int(input("Masukkan jumlah siswa :"))

data_nilai = []
jumlah = 0

for i in range (0,siswa) :
    nilai = int(input("Masukkan nilai ke-%d :" % (i+1)))
    data_nilai.append(nilai)
    jumlah = jumlah + data_nilai[i]
    rata_rata = jumlah / siswa
    nilai_total = jumlah
print("Total nilai\t: %.2f" % (nilai_total))
print("Rata - rata\t: %.2f" % (rata_rata))