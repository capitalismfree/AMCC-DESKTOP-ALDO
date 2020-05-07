class suhu:
    hasil = ()
    celcius = ()
    kelvin = ()
    reamur = ()
    farenheit = ()

    def konversi_celcius_ke_Kelvin(self,celcius):
        self.celcius = celcius
        hasil = celcius + 273
        print("konversi dari {0} celcius ke kelvin : {1}".format(celcius,hasil))
    
    def konversi_celcius_ke_reamur(self,celcius):
        self.celcius = celcius
        hasil = (4 / 5) * celcius
        print("konversi dari {0} celcius ke reamur : {1}".format(celcius,hasil))
    
    def konversi_celcius_ke_farenheit(self,celcius):
        self.celcius = celcius
        hasil = ((9 / 5) * celcius) + 32
        print("konversi dari {0} celcius ke farenheit : {1}".format(celcius,hasil))

    def konversi_kelvin_ke_celcius(self,kelvin):
        self.kelvin = kelvin
        hasil = kelvin - 273
        print("konversi dari {0} kelvin ke celcius : {1}".format(kelvin,hasil))
    
    def konversi_kelvin_ke_reamur(self,kelvin):
        self.kelvin = kelvin
        hasil = (4/5) * (kelvin - 273)
        print("konversi dari {0} kelvin ke reamur : {1}".format(kelvin,hasil))

    def konversi_kelvin_ke_farenheit(self,kelvin):
        self.kelvin = kelvin
        hasil = ((9 / 5) * (kelvin - 273)) + 32
        print("konversi dari {0} kelvin ke farenheit : {1}".format(kelvin,hasil))
    
    def konversi_reamur_ke_celcius(self,reamur):
        self.reamur = reamur
        hasil = (5 / 4) * reamur
        print("konversi dari {0} reamur ke celcius : {1}".format(reamur,hasil))

    def konversi_reamur_ke_kelvin(self,reamur):
        self.reamur = reamur
        hasil = (5 / 4) * reamur + 273
        print("konversi dari {0} reamur ke kelvin : {1}".format(reamur,hasil))

    def konversi_reamur_ke_farenheit(self,reamur):
        self.reamur = reamur
        hasil = (9 / 4) * reamur + 32
        print("konversi dari {0} reamur ke farenheit : {1}".format(reamur,hasil))

    def konversi_farenheit_ke_celcius(self,farenheit):
        self.farenheit = farenheit
        hasil = (5 / 9) * (farenheit - 32)
        print("konversi dari {0} farenheit ke celcius : {1}".format(farenheit,hasil))

    def konversi_farenheit_ke_kelvin(self,farenheit):
        self.farenheit = farenheit
        hasil = (5 / 9) * (farenheit - 32) + 273
        print("konversi dari {0} farenheit ke kelvin : {1}".format(farenheit,hasil))

    def konversi_farenheit_ke_reamur(self,farenheit):
        self.farenheit = farenheit
        hasil = (4 / 9) * (farenheit - 32)
        print("konversi dari {0} farenheit ke reamur : {1}".format(farenheit,hasil))

class bentuk:
    segitiga = ""
    baris = ()
    kolom = ()
    tinggi = ()

    def segitiga_siku_siku(self,tinggi):
        self.tinggi = tinggi
        segitiga = ""
        baris = 1
        while(baris <= tinggi):
            kolom = baris
            while(kolom > 0):
                segitiga += "*"
                kolom -= 1
            segitiga += "\n"
            baris += 1
        print(segitiga)
    
    def segitiga_siku_siku_terbalik(self,tinggi):
        self.tinggi = tinggi
        segitiga = ""
        baris = 1
        while(baris <= tinggi):
            kolom = baris
            while(kolom > 1):
                segitiga += " "
                kolom -= 1
            kanan = 0
            while(kanan <= (tinggi - baris)):
                segitiga += "*"
                kanan += 1
            segitiga += "\n"
            baris += 1
        print(segitiga)
    
    def segitiga_sama_sisi(self,tinggi):
        self.tinggi = tinggi
        segitiga = ""
        baris = tinggi
        while(baris >= 0):
            kolom = baris
            while(kolom >= 1):
                segitiga += " "
                kolom -= 1
            kiri = 1
            while(kiri < (tinggi - (baris - 1))):
                segitiga += "*"
                kiri += 1
            kanan = 1
            while(kanan < kiri-1):
                segitiga += "*"
                kanan += 1
            segitiga += "\n"
            baris -= 1
        print(segitiga)

    def segitiga_sama_sisi_terbalik(self,tinggi):
        self.tinggi = tinggi
        segitiga = ""
        baris = 1
        while(baris <= tinggi):
            kolom = baris
            while(kolom > 1):
                segitiga += " "
                kolom -= 1
            kiri = 0
            while(kiri <= (tinggi - baris)):
                segitiga = "*"
                kiri += 1
            kanan = kiri
            while(kanan > 1):
                segitiga = "*"
                kanan -= 1
            segitiga += "\n"
            baris += 1
        print(segitiga) 

class bilangan:
    hasil = ()
    tampilan = ""
    temp = []
    hasilbiner = 0
    biner = ""
    pembalik = []
    hasloktal = 0
    desimal = ()
    oktal = ""
    hasilheksadesimal = 0

    def konversi_desimal_ke_biner(self,desimal):
        self.desimal = desimal
        temp = []
        tampilan = ""
        while(desimal != 0):
            hasil = desimal % 2
            temp.insert (0,str(hasil))
            desimal = desimal//2
            if(desimal == 0):
                for i in range (0,len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)

    def konversi_desimal_ke_oktal(self,desimal):
        self.desimal = desimal
        temp = []
        tampilan = ""
        while(desimal != 0):
            hasil = desimal % 8
            temp.insert (0,str(hasil))
            desimal = desimal // 8
            if(desimal == 0):
                for i in range (len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)
    
    def konversi_desimal_ke_heksadesimal(self,desimal):
        self.desimal = desimal
        temp = []
        tampilan = ""
        while(desimal != 0):
            hasil = desimal % 16
            if(hasil == 10):
                hasil = "A"
            elif(hasil == 11):
                hasil = "B"
            elif(hasil == 12):
                hasil = "C"
            elif(hasil == 13):
                hasil = 'D'
            elif(hasil == 14):
                hasil = "E"
            elif(hasil == 15):
                hasil = "F"
            temp.insert (0,str(hasil))
            desimal = desimal // 16
            if(desimal == 0):
                for i in range (len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)

    def konversi_biner_ke_desimal(self,biner):
        self.biner = biner
        pembalik = []
        hasilbiner = 0
        for i in range(len(biner)):
            pembalik.insert(0,biner[i])
        for i in range(len(pembalik)):
            hasilbiner += int(pembalik[i])*(2**i)
        print("hasil konversi : ",hasilbiner)
    
    def konversi_biner_ke_oktal(self,biner):
        self.biner = biner
        temp = []
        hasilbiner = 0
        tampilan = ""
        pembalik = []
        hasil = 0
        for i in range(len(biner)):
            pembalik.insert(0,biner[i])
        for i in range(len(pembalik)):
            hasilbiner += int(pembalik[i])*(2**i)
        
        while(hasilbiner != 0):
            hasil = hasilbiner % 8
            temp.insert(0,str(hasil))
            hasilbiner = hasilbiner//8
            if(hasilbiner == 0):
                for i in range(len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)
    
    def konversi_biner_ke_heksadesimal(self,biner):
        self.biner = biner
        temp = []
        tampilan = ""
        hasilbiner = 0
        pembalik = []
        for i in range(len(biner)):
            pembalik.insert(0,biner[i])
        for i in range(len(pembalik)):
            hasilbiner += int(pembalik[i])*(2**i)
        
        while(hasilbiner != 0):
            hasil = hasilbiner % 16
            if(hasil == 10):
                hasil = "A"
            elif(hasil == 11):
                hasil = "B"
            elif(hasil == 12):
                hasil = "C"
            elif(hasil == 13):
                hasil = "D"
            elif(hasil == 14):
                hasil = "E"
            elif(hasil == 15):
                hasil = "F"
            temp.insert(0,str(hasil))
            hasilbiner = hasilbiner // 16
            if(hasilbiner == 0):
                for i in range (len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)

    def konversi_oktal_ke_desimal(self,oktal):
        self.oktal = oktal
        hasiloktal = 0
        pembalik = []
        for i in range(len(oktal)):
            pembalik.insert(0,oktal[i])
        for i in range(len(pembalik)):
            hasiloktal += int(pembalik[i])*(8**i)
        print("hasil konversi : ",hasiloktal)
    
    def konversi_oktal_ke_biner(self,oktal):
        self.oktal = oktal
        hasiloktal = 0
        pembalik = []
        tampilan = ""
        temp = []
        for i in range(len(oktal)):
            pembalik.insert(0,oktal[i])
        for i in range(len(pembalik)):
            hasiloktal += int(pembalik[i])*(8**i)
        
        while(hasiloktal != 0):
            hasil = hasiloktal % 2
            temp.insert(0,str(hasil))
            hasiloktal = hasiloktal // 2
            if(hasiloktal == 0):
                for i in range(len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)

    def konversi_oktal_ke_heksadesimal(self,oktal):
        self.oktal = oktal
        tampilan = ""
        temp = []
        pembalik = []
        hasiloktal = 0
        for i in range(len(oktal)):
            pembalik.insert(0,oktal[i])
        for i in range(len(pembalik)):
            hasiloktal += int(pembalik[i])*(8**i)
        
        while(hasiloktal != 0):
            hasil = hasiloktal % 16
            if(hasil == 10):
                hasil = "A"
            elif(hasil == 11):
                hasil = "B"
            elif(hasil == 12):
                hasil = "C"
            elif(hasil == 13):
                hasil = "D"
            elif(hasil == 14):
                hasil = "E"
            elif(hasil == 15):
                hasil = "F"
            temp.insert(0,str(hasil))
            hasiloktal = hasiloktal // 16
            if(hasiloktal == 0):
                for i in range(len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)

    def konversi_heksadesimal_ke_desimal(self,heksadesimal):
        self.heksadesimal = heksadesimal
        hasilheksadesimal = 0
        hasil = 0
        pembalik = []
        for i in range(len(heksadesimal)):
            pembalik.insert(0,heksadesimal[i])
        for i in range(len(pembalik)):
            if(pembalik[i] == "a" or pembalik[i] == "A"):
                hasil = 10
            elif(pembalik[i] == "b" or pembalik[i] == "B"):
                hasil = 11
            elif(pembalik[i] == "c" or pembalik[i] == "C"):
                hasil = 12
            elif(pembalik[i] == "d" or pembalik[i] == "D"):
                hasil = 13
            elif(pembalik[i] == "e" or pembalik[i] == "E"):
                hasil = 14
            elif(pembalik[i] == "f" or pembalik[i] == "F"):
                hasil = 15
            else:
                hasil = int(pembalik[i])
            hasilheksadesimal += hasil*(16**i)
        print("hasil konversi : ",hasilheksadesimal)

    def konversi_heksadesimal_ke_biner(self,heksadesimal):
        self.heksadesimal = heksadesimal
        hasilheksadesimal = 0
        hasil = 0
        pembalik = []
        tampilan = ""
        temp = []
        for i in range(len(heksadesimal)):
            pembalik.insert(0,heksadesimal[i])
        for i in range(len(pembalik)):
            if(pembalik[i] == "a" or pembalik[i] == "A"):
                hasil = 10
            elif(pembalik[i] == "b" or pembalik[i] == "B"):
                hasil = 11
            elif(pembalik[i] == "c" or pembalik[i] == "C"):
                hasil = 12
            elif(pembalik[i] == "d" or pembalik[i] == "D"):
                hasil = 13
            elif(pembalik[i] == "e" or pembalik[i] == "E"):
                hasil = 14
            elif(pembalik[i] == "f" or pembalik[i] == "F"):
                hasil = 15
            else:
                hasil = int(pembalik[i])
            hasilheksadesimal += hasil*(16**i)

        while(hasilheksadesimal != 0):
            hasil = hasilheksadesimal % 2
            temp.insert(0,str(hasil))
            hasilheksadesimal = hasilheksadesimal // 2
            if(hasilheksadesimal == 0):
                for i in range(len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)

    def konversi_heksadesimal_ke_oktal(self,heksadesimal):
        self.heksadesimal = heksadesimal
        hasilheksadesimal = 0
        hasil = 0
        pembalik = []
        temp = []
        tampilan = ""
        for i in range(len(heksadesimal)):
            pembalik.insert(0,heksadesimal[i])
        for i in range(len(pembalik)):
            if(pembalik[i] == "a" or pembalik[i] == "A"):
                hasil = 10
            elif(pembalik[i] == "b" or pembalik[i] == "B"):
                hasil = 11
            elif(pembalik[i] == "c" or pembalik[i] == "C"):
                hasil = 12
            elif(pembalik[i] == "d" or pembalik[i] == "D"):
                hasil = 13
            elif(pembalik[i] == "e" or pembalik[i] == "E"):
                hasil = 14
            elif(pembalik[i] == "f" or pembalik[i] == "F"):
                hasil = 15
            else:
                hasil = int(pembalik[i])
            hasilheksadesimal += hasil*(16**i)
        
        while(hasilheksadesimal != 0):
            hasil = hasilheksadesimal % 8
            temp.insert(0,str(hasil))
            hasilheksadesimal = hasilheksadesimal // 8
            if(hasilheksadesimal == 0):
                for i in range(len(temp)):
                    tampilan += temp[i]
        print("hasil konversi : ",tampilan)

def menu():
    print("==========================================")
    print("a.konversi suhu")
    print("b.konversi bilangan")
    print("c.perulangan bentuk")
    print("d.keluar")
    print("==========================================")
    pilihan = input("pilihan : ")    
    if(pilihan == "a" or pilihan == "A"):
        menu_konversi_suhu()
    elif(pilihan == "b" or pilihan == "B"):
        menu_konversi_bilangan()
    elif(pilihan == "c" or pilihan == "C"):
        menu_perulangan_bentuk()
    elif(pilihan == "d" or pilihan == "D"):
        exit()
    else:
        print("perintah tidak ada")
        menu()

def menu_konversi_suhu():
    print("==============konversi dari===============")
    print("a.celcius")
    print("b.kelvin")
    print("c.reamur")
    print("d.farenheit")
    print("e.kembali ke menu utama")
    print("==========================================")
    pilihan = input("pilihan : ")
    if(pilihan == "a" or pilihan == "A"):
        menu_konversi_suhu_pilihan_A()
    elif(pilihan == "b" or pilihan == "B"):
        menu_konversi_suhu_pilihan_B()
    elif(pilihan == "c" or pilihan == "C"):
        menu_konversi_suhu_pilihan_C()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_suhu_pilihan_D()
    elif(pilihan == "e" or pilihan == "E"):
        menu()
    else:
        print("perintah tidak ada")
        menu_konversi_suhu()
        
def menu_konversi_suhu_pilihan_A():
    s = suhu()
    print("=============konversikan ke===============")
    print("a.kelvin")
    print("b.reamur")
    print("c.farenheit")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("pilihan = ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_celcius_ke_Kelvin(a)
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_celcius_ke_reamur(a)
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_celcius_ke_farenheit(a)
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_suhu()
    else:
        print("perintah yg anda masukkan salah")
        menu_konversi_suhu_pilihan_A()

def menu_konversi_suhu_pilihan_B():
    s = suhu()
    print("=============konversikan ke===============")
    print("a.celcius")
    print("b.reamur")
    print("c.farenheit")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("pilihan = ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_kelvin_ke_celcius(a)
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_kelvin_ke_reamur(a)
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_kelvin_ke_farenheit(a)
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_suhu()
    else:
        print("perintah yg anda masukkan salah")
        menu_konversi_suhu_pilihan_B()

def menu_konversi_suhu_pilihan_C():
    s = suhu()
    print("=============konversikan ke===============")
    print("a.celcius")
    print("b.kelvin")
    print("c.farenheit")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("pilihan = ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_reamur_ke_celcius(a)
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_reamur_ke_kelvin(a)
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_reamur_ke_farenheit(a)
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_suhu()
    else:
        print("perintah tidak ada")
        menu_konversi_suhu_pilihan_C()

def menu_konversi_suhu_pilihan_D():
    s = suhu()
    print("=============konversikan ke===============")
    print("a.celcius")
    print("b.kelvin")
    print("c.reamur")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("pilihan = ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_farenheit_ke_celcius(a)
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_farenheit_ke_kelvin(a)
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                a = int(input("masukkan besar suhu : "))
                break
            except ValueError:
                print("tidak boleh huruf!")
        s.konversi_farenheit_ke_reamur(a)
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_suhu()
    else:
        print("perintah tidak ada")
        menu_konversi_suhu_pilihan_D()

def menu_perulangan_bentuk():
    b = bentuk()
    print("===========perulangan bentuk==============")
    print("a.segitiga siku siku")
    print("b.segitiga siku siku terbalik")
    print("c.segitiga sama sisi")
    print("d.segitiga sama sisi terbalik")
    print("e.kembali ke menu utama")
    print("==========================================")
    pilihan = input("masukkan pilihan : ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                tinggi = int(input("masukkan tinggi : "))
                break
            except ValueError:
                print("harus angka!")
        b.segitiga_siku_siku(tinggi)
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                tinggi = int(input("masukkan tinggi : "))
                break
            except ValueError:
                print("harus angka!")
        b.segitiga_siku_siku_terbalik(tinggi)
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                tinggi = int(input("masukkan tinggi : "))
                break
            except ValueError:
                print("harus angka!")
        b.segitiga_sama_sisi(tinggi)
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        while True:
            try:
                tinggi = int(input("masukkan tinggi : "))
                break
            except ValueError:
                print("harus angka!")
        b.segitiga_sama_sisi_terbalik(tinggi)
        konfirmasi()
    elif(pilihan == "e" or pilihan == "E"):
        menu()
    else:
        "perintah tidak ada"
        menu_perulangan_bentuk()

def menu_konversi_bilangan():
    print("==============konversi dari===============")
    print("a.desimal")
    print("b.biner")
    print("c.oktal")
    print("d.heksadesimal")
    print("e.kembali ke menu utama")
    print("==========================================")
    pilihan = input("masukkan pilihan : ")
    if(pilihan == "a" or pilihan == "A"):
        menu_konversi_bilangan_pilihan_A()
    elif(pilihan == "b" or pilihan == "B"):
        menu_konversi_bilangan_pilihan_B()
    elif(pilihan == "c" or pilihan == "C"):
        menu_konversi_bilangan_pilihan_C()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_bilangan_pilihan_D()
    elif(pilihan == "e" or pilihan == "E"):
        menu()
    else:
        print("perintah tidak ada")
        menu_konversi_bilangan()

def menu_konversi_bilangan_pilihan_A():
    b = bilangan()
    print("=============konversikan ke===============")
    print("a.biner")
    print("b.oktal")
    print("c.heksadesimal")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("masukkan pilihan : ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                desimal = int(input("masukkan nilai(desimal) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_desimal_ke_biner(desimal)
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                desimal = int(input("masukkan nilai(desimal) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_desimal_ke_oktal(desimal)
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                desimal = int(input("masukkan nilai(desimal) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_desimal_ke_heksadesimal(desimal)
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_bilangan()
    else:
        print("perintah tidak ada")
        menu_konversi_bilangan_pilihan_A()

def menu_konversi_bilangan_pilihan_B():
    b = bilangan()
    print("=============konversikan ke===============")
    print("a.desimal")
    print("b.oktal")
    print("c.heksadesimal")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("masukkan pilihan : ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                biner = int(input("masukkan nilai(biner) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_biner_ke_desimal(str(biner))
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                biner = int(input("masukkan nilai(biner) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_biner_ke_oktal(str(biner))
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                biner = int(input("masukkan nilai(biner) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_biner_ke_heksadesimal(str(biner))
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_bilangan()
    else:
        print("perintah tidak ada")
        menu_konversi_bilangan_pilihan_B()

def menu_konversi_bilangan_pilihan_C():
    b = bilangan()
    print("=============konversikan ke===============")
    print("a.desimal")
    print("b.biner")
    print("c.heksadesimal")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("masukkan pilihan : ")
    if(pilihan == "a" or pilihan == "A"):
        while True:
            try:
                oktal = int(input("masukkan nilai(oktal) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_oktal_ke_desimal(str(oktal))
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        while True:
            try:
                oktal = int(input("masukkan nilai(oktal) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_oktal_ke_biner(str(oktal))
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        while True:
            try:
                oktal = int(input("masukkan nilai(oktal) : "))
                break
            except ValueError:
                print("harus angka!")
        b.konversi_oktal_ke_heksadesimal(str(oktal))
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_bilangan()
    else:
        print("perintah tidak ada")
        menu_konversi_bilangan_pilihan_C()

def menu_konversi_bilangan_pilihan_D():
    b = bilangan()
    print("=============konversikan ke===============")
    print("a.desimal")
    print("b.biner")
    print("c.oktal")
    print("d.kembali ke menu pilihan")
    print("==========================================")
    pilihan = input("masukkan pilihan : ")
    if(pilihan == "a" or pilihan == "A"):
        heksadesimal = input("masukkan nilai(heksadesimal) : ")
        b.konversi_heksadesimal_ke_desimal(heksadesimal)
        konfirmasi()
    elif(pilihan == "b" or pilihan == "B"):
        heksadesimal = input("masukkan nilai(heksadesimal) : ")
        b.konversi_heksadesimal_ke_biner(heksadesimal)
        konfirmasi()
    elif(pilihan == "c" or pilihan == "C"):
        heksadesimal = input("masukkan nilai(heksadesimal) : ")
        b.konversi_heksadesimal_ke_oktal(heksadesimal)
        konfirmasi()
    elif(pilihan == "d" or pilihan == "D"):
        menu_konversi_bilangan()
    else:
        print("perintah tidak ada")
        menu_konversi_bilangan_pilihan_D()

def konfirmasi():
    k = input("apakah anda ingin kembali ke menu utama?(y/n) : ")
    if(k == "y" or k == "Y"):
        menu()           
    elif(k == "n" or k == "N"):
        exit()
    else:
        print("perintah tidak ada")
        konfirmasi()

menu()