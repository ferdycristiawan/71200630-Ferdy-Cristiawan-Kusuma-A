#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah program membuat bangun datar bintang. Beri pilihan untuk user memasukkan bentuk bangun datar :
1. Segitiga
2. Kotak
3. Kotak bolong(lubang)
jika user memilih 1 maka masukkan nilai alas, jika memilih 2 masukkan nilai sisi, jika memlih 3 masukkan nilai x dan y sebagai panjang dan
lebarnya, gunakan output "Input salah. Masukkan dengan benar!" sebagai hasil dari input user yang salah atau tidak sesuai nilai yang dimasukkan.
Gunakan kontrol percabangan dan perulangan.
'''

'''
Input : membuat pilihan utk ketiga bangun datar
        jika no.1 = input alas
        jika no.2 = input sisi
        jika no.3 = x, y
Proses : percabangan= pilihan 1,2,3
        perulangan = pola bintang
Output : bentuk bangun datar bintang
'''

print("=====PROGRAM BENTUK BANGUN DATAR=====")

print("Bentuk Bangun Datar")
print("1. Segitiga \n2. Kotak \n3. Kotak Lubang")

pilihan = int(input("Masukkan pilihan :"))

if pilihan == 1 :
    alas = int(input("Masukkan alas :"))
    x = alas - 1
    for i in range (0,alas) :
        for j in range (0,x) :
            print(' ', end='')
        x = x - 1
        for j in range (0,i + 1) :
            print('* ', end='')
        print('')
elif pilihan == 2 :
    sisi = int(input("Masukkan sisi :"))
    for i in range (sisi) :
        for j in range (sisi) :
            print('*', end=' ')
        print('')
elif pilihan == 3 :
    x = int(input("Masukkan nilai x :"))
    y = int(input("Masukkan nilai y :"))
    for i in range (x) :
        if i==0 or i==x-1 :
            print('*' * y)
        else :
            print('*' + ' ' * (y-2) + '*')
else :
    print("Input salah. Masukkan dengan benar!")