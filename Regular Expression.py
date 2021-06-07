#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah sebuah program regex untuk mencari email dalam sebuah file text dengan format sesuai yang kita inginkan.
Misal contoh email : regex_python@gmail.com
Maka contoh pola yang kita buat adalah :
  regex_python : huruf/angka
  @            : karakter '@'
  gmail        : huruf
  .            : karakter '.'
  com          : huruf 
Cari pola regex yang dapat menampilkan seperti pola diatas.
'''
'''
Input : menggunakan import re(mengimport module regex), menggunakan perintah open(membaca file)
Proses : perulangan(membaca setiap line di file text), percabangan(mencari pola)
Output : tampilkan baris yang berisi pola yang kita inginkan yaitu email
'''

import re

handle = open('contohEmail.txt')
count = 0
for line in handle :
  line = line.rstrip()
  if re.search('[^@]+@+[^@]+\.[^@]', line) :
    count = count + 1
    print (count,'.',line)
