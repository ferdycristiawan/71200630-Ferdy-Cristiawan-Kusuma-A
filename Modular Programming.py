#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program untuk mengukur persentase rugi dan untung dalam penjualan. Ini merupakan program sederhana. User cukup memasukkan
input harga beli dan harga jual dan output akan mengeluarkan persentase rugi atau untung. Gunakan dua fungsi dan percabangan
sebagai keluaran apakah akan keluar untung atau rugi dengan satuan persen.
'''
'''
Input : harga beli dan harga jual
Proses : rumus fungsi persentase harga beli dan harga jual, percabangan antara harga beli dan harga jual
Output : keluaran persentase untung atau rugi 
'''

def rugi(harga_beli,harga_jual) :
    persen_rugi = ((harga_beli-harga_jual)*100) / harga_beli
    return persen_rugi
def untung(harga_beli,harga_jual) :
    persen_untung = ((harga_jual-harga_beli)*100) / harga_beli
    return persen_untung

print("-----PERSENTASE PENJUALAN-----")
harga_beli = int(input("Masukkan harga beli : Rp."))
harga_jual = int(input("Masukkan harga jual : Rp."))

if harga_beli > harga_jual :
    print("Persentase rugi :",rugi(harga_beli,harga_jual),"%")
elif harga_beli < harga_jual :
    print("Persentase untung :",untung(harga_beli,harga_jual),"%")