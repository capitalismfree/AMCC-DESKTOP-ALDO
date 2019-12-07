angka1 = int(input("masukkan angka pertama : "))
angka2 = int(input("masukkan angka kedua : "))
print("operator : \n1.penjumlahan\n2.pengurangan"
        "\n3.perkalian\n4.pembagian\n")
pilihan = int(input("masukkan pilihan : "))
while(konfirmasi != 'n' | konfirmasi != 'N'):
    if pilihan == 1:
        jawaban = angka1+angka2
        print("hasilnya adalah ",jawaban)
        konfirmasi = str(input("apakah anda ingin mengulang (y/n) : "))
    elif pilihan == 2:
        jawaban = angka1-angka2
        print("hasilnya adalah ",jawaban)
        konfirmasi = str(input("apakah anda ingin mengulang (y/n) : "))
    elif pilihan == 3:
        jawaban = angka1*angka2
        print("haslnya adalah ",jawaban)
        konfirmasi = str(input("apakah anda ingin mengulang (y/n) : "))
    elif pilihan == 4:
        jawaban = angka1/angka2
        print("hasilnya adalah ",jawaban)
        konfirmasi = str(input("apakah anda ingin mengulang (y/n) : "))
    else:
        print("operator tidak ada")