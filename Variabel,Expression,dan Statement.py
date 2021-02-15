#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM : 71200630

'''
Ilham adalah seorang mahasiswa, dan sekarang dia bekerja sampingan menjadi barista. Gaji yang diterima adalah gaji per jam.
Total pajak yang harus Ilham bayarkan selama 1 minggu adalah 10%. Setelah membayar pajak, Ilham selalu mengambil 20%
dari pendapatan bersihnya untuk membeli kuota, setelah membeli kuota, 25% lagi Ilham gunakan untuk belanja selama 1 minggu.
Sisanya akan Ilham tabung di bank. Buatlah program dengan input :
1. Input gaji per jam
2. Input jumlah jam kerja selama 1 minggu
Output :
1. Pendapatan kotor sebelum membayar pajak
2. Pendapatan bersih setelah membayar pajak
3. Jumlah uang dihabiskan untuk membeli kuota
4. Jumlah uang dihabiskan untuk belanja
5. Jumlah uang yang ditabung di bank
'''

'''
Input : gaji per jam, jumlah jam kerja, pajak 10%, kuota 20%, belanja 25%

Proses :cek gaji per jam, cek jumlah jam kerja, cari pendapatan kotor, cari pendapatan bersih, cari jumlah uang untuk membeli kuota
        cari jumlah uang untuk belanja, cari jumlah uang untuk ditabung di bank

Output : pendapatan kotor, pendapatan bersih, uang kuota, uang belanja, uang untuk ditabung di bank

'''

gaji_per_jam = int(input("Masukkan gaji per jam : Rp."))
jumlah_jam_kerja = int(input("Masukkan jumlah jam kerja :"))

pajak = 0.1
pendapatan_kotor = gaji_per_jam * jumlah_jam_kerja
uang_pajak = pendapatan_kotor * pajak

pendapatan_bersih = pendapatan_kotor - uang_pajak

kuota = 0.2
uang_kuota = pendapatan_bersih * kuota
sisa_uang = pendapatan_bersih - uang_kuota

belanja = 0.25
uang_belanja = sisa_uang * belanja

uang_bank = sisa_uang - uang_belanja

print("Pendapatan kotor Ilham adalah Rp.%d" % (pendapatan_kotor))
print("Pendapatan bersih Ilham adalah Rp.%d" % (pendapatan_bersih))
print("Jumlah uang untuk membeli kuota adalah Rp.%d" % (uang_kuota))
print("Jumlah uang untuk belanja adalah Rp.%d" % (uang_belanja))
print("Jumlah uang untuk ditabung di bank adalah Rp.%.2f" % (uang_bank))