#NAMA : FERDY CRISTIAWAN KUSUMA
#NIM  : 71200630

'''
Buatlah sebuah program untuk membantu mahasiswa melihat jadwal kuliahnya. Gunakan list untuk membuat jadwal mata kuliah di hari senin - jumat.
Ada 6 sesi dalam 1 hari perkuliahan
Berikut jadwal dan sesi yang ada :
senin = ["AlPro","PrakAlPro"," ","ICE"," "," "]
selasa = ["JarKom","PrakJarKom"," ","ArOrKom"," "," "]
rabu = ["MaDis","PKN"," "," "," "," "]
kamis = [" "," "," ","Statistik","PrakAlpro 2"]
jumat = [" "," "," "," "," "," "]
Pada hari jumat, jadwal kuliah kosong
'''
'''
Input : input dari user
Proses : membuat list jadwal dari senin-jumat, membuat percabangan
Output : jadwal kuliah dan sesi ke berapa pada hari yang telah ditentukan
'''

senin = ["AlPro","PrakAlPro"," ","ICE"," "," "]
selasa = ["JarKom","PrakJarKom"," ","ArOrKom"," "," "]
rabu = ["MaDis","PKN"," " ," "," "," "]
kamis = [" "," "," ","Statistik","PrakAlpro 2"]
jumat = [" "," "," "," "," "," "]

sesi = 1
hari = input("Silakan masukkan hari yang ingin anda telusuri :")

if hari == 'senin' :
    for i in range(6) :
        if senin[i] == ' ' :
            pass
        else :
            print("Sesi ke-%d" % (i+1),senin[i])
elif hari == 'selasa' :
    for i in range(6) :
        if selasa[i] == ' ' :
            pass
        else :
            print("Sesi ke-%d" % (i+1),selasa[i])
elif hari == 'rabu' :
    for i in rabu :
        if i != ' ' :
            print("Sesi ke-" + str(sesi),i)
        sesi = sesi + 1
elif hari == 'kamis' :
    for i in kamis :
        if i != ' ' :
            print("Sesi ke-" + str(sesi),i)
        sesi = sesi + 1
elif hari == 'jumat' :
    print("Hari jumat anda tidak ada kelas")
