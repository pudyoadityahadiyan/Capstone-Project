list_siswa = {
    "Anggun" :{ "NIM" : 18922002,
                "Pelajaran" :{
    
        "Matematika" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            },
        "Bahasa Inggris" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            },
        "Bahasa Indonesia" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            }
    }},
    "Jono" : {"NIM" : 18922001,
            "Pelajaran" :{
        "Matematika" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            },
        "Bahasa Inggris" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            },
        "Bahasa Indonesia" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            },
    }},
    "Joko" : {"NIM" : 18922003,
    "Pelajaran" :{
        "Matematika" :
            {
                "UTS" : 0,
                "UAS" : 10,
                "Praktikum" : 10,
                "Tugas" : 10,
                "index" : "E"
            },
        "Bahasa Inggris" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            },
        "Bahasa Indonesia" :
            {
                "UTS" : 100,
                "UAS" : 100,
                "Praktikum" : 100,
                "Tugas" : 100,
                "index" : "A"
            },
    }}
}

def rekap_nilai():
    # mata_pelajaran = 'Matematika'
    while True:
        a =  ('''List Mata Pelajaran

Matematika
Bahasa Inggris
Bahasa Indonesia        
        ''')
        print (a)
        mata_pelajaran = str.title(input('Masukan Pelajaran : '))
        try:
            list_siswa
            index()
            a = b = c = 0
            p =  "NIM"+ " "*9 + "|" + " Nama Siswa"+" "*(24-len("Nama Siswa"))+"|"+ " UTS"+" "*4 + "|" + " UAS"+" "*4 + "|" + " Praktikum"+" |"+ " Tugas"+" |"+" Index Siswa"+" |"
            p2 = "NIM"+ " "*9 + "|" + " Nama Siswa"+" "*(24-len("Nama Siswa"))
            print (p)
            print("="*(len(p)+10))
            for i,j in  enumerate(list_siswa.items()):
                print (j[1]['NIM'], " "*(10-len(str(j[1]['NIM']))), "|", j[0], " "*(22-len(j[0])),"|", 
                    j[1]["Pelajaran"][mata_pelajaran]["UTS"], " "*(5-len(str(j[1]["Pelajaran"][mata_pelajaran]["UTS"]))),"|",
                    j[1]["Pelajaran"][mata_pelajaran]["UAS"], " "*(5-len(str(j[1]["Pelajaran"][mata_pelajaran]["UAS"]))),"|", 
                    j[1]["Pelajaran"][mata_pelajaran]["Praktikum"], " "*(8-len(str(j[1]["Pelajaran"][mata_pelajaran]["Praktikum"]))),"|", 
                    j[1]["Pelajaran"][mata_pelajaran]["Tugas"], " "*(4-len(str(j[1]["Pelajaran"][mata_pelajaran]["Tugas"]))),"|",
                    j[1]["Pelajaran"][mata_pelajaran]["index"]," "*(10-len(str(j[1]["Pelajaran"][mata_pelajaran]["index"]))),"|" )
                a += j[1]["Pelajaran"][mata_pelajaran]["UTS"]
                b += j[1]["Pelajaran"][mata_pelajaran]["UAS"]
                c += j[1]["Pelajaran"][mata_pelajaran]["Praktikum"]
            rata1 = round(a/(i+1),2)
            rata2 = round(b/(i+1),2)
            rata3 = round(c/(i+1),2)
            print("="*(len(p)+10))
            print("Rata - Rata", " "*(len(p2)-13),"|",
            rata1, " "*(5-len(str(rata1))),"|" ,
            rata2, " "*(5-len(str(rata2))),"|" ,
            rata3, " "*(8-len(str(rata3))),"|" ,
                    )
            print("="*(len(p)+10))
            break
        except:
            print(f"Tidak ada mata pelajaran {mata_pelajaran}")
            break

def raport():
    global nama_siswa
    while True:
        nama_siswa = str.title(input("Masukan Nama Siswa : "))
        IP()
        index()
        if nama_siswa in list_siswa:
            print("="*(50))
            print (f'Raport {nama_siswa} NIM {list_siswa[nama_siswa]["NIM"]} \nSemester Ganjil Tahun ajaran 2022 - 2023')
            print("="*(50))
        
            for i,j in list_siswa[nama_siswa]["Pelajaran"].items():
                print (i," "*(20-len(i)),"|" ,j["index"])
            print("="*(50))
            print(f'Index Prestasi {nama_siswa} adalah {round(ip1,2)}')
            print("="*(50))
            break
        else:
            print(f'\nTidak ada siswa bernama {nama_siswa}\n')

def kemahasiswaan():
    
        while True:
            point = ["Daftar Siswa","Tambah Siswa", "Ganti Nama Siswa", "Hapus Siswa", "Keluar" ]
            print ('Menu Kemahasiswaan : ')
            for i,j in enumerate(point):
                print (f'{i+1}. {j}')
            pilih = input('Pilihan Anda : ')
            try:
                if int(pilih) == 2:
                    mahasiswa_baru()
                elif int(pilih) == 3:
                    ganti_nama()
                elif int(pilih) == 4:
                    hapus_mahasiswa()
                elif int(pilih) == 1:
                    daftar_mahasiswa()
                elif int(pilih) == 5:
                    break
                
            except :
                print ('Pilih dengan Teliti')
   
def mahasiswa_baru():
    global list_siswa
    input_mahasiswa = str.title(input("Masukan Nama Siswa Baru : "))
    for i,j in list_siswa.items():
        nim = 0
        a = list_siswa[i]['NIM']
        if a > nim:
            nim = a
    mahasiswa_baru = {input_mahasiswa: {"NIM" : nim+1,
                "Pelajaran" :{
            "Matematika" :
                {
                    "UTS" : 0,
                    "UAS" : 0,
                    "Praktikum" : 0,
                    "Tugas" : 0,
                    "index" : None
                },
            "Bahasa Inggris" :
                {
                    "UTS" : 0,
                    "UAS" : 0,
                    "Praktikum" : 0,
                    "Tugas" : 0,
                    "index" : None
                },
            "Bahasa Indonesia" :
                {
                    "UTS" : 0,
                    "UAS" : 0,
                    "Praktikum" : 0,
                    "Tugas" : 0,
                    "index" : None
                }}}}

    list_siswa.update(mahasiswa_baru)

def daftar_mahasiswa():
    print("\n")
    print("NIM\t\t| Nama Siswa")
    print("="*30)
    for i,j in list_siswa.items():
        print(j["NIM"],"\t|",i)
    print("="*30)
    print("\n")


def ganti_nama():
    global list_siswa
    input_mahasiswa = str.title(input("Masukan Nama Siswa : "))
    try:
        list_siswa[input_mahasiswa]
        input_mahasiswa2 = str.title(input("Masukan Nama Baru Siswa Baru : "))
        list_siswa[input_mahasiswa] = list_siswa.pop(input_mahasiswa2)
    except:
        print(f'Tidak ada siswa bernama {input_mahasiswa}')

def hapus_mahasiswa():
    global list_siswa
    hapus_mahasiswa = str.title(input("Masukan Nama Siswa Keluar : "))
    try:
        del list_siswa[hapus_mahasiswa]
    except:
        print(f'Tidak ada siswa bernama {hapus_mahasiswa}')  

def nilai():
    global ket
    while True:
        Nilai = '''
Sistem Penilaian Siswa

List Menu:
1. Input Nilai
2. Ganti Nilai
3. Hapus Nilai
4. Rekap Nilai Mahasiswa
5. Kembali
        '''
        print(Nilai)
        masuk = (input('Masukan Nomer Menu : '))
        try:
            if int(masuk) == 5:
                break
            if int(masuk) == 1:
                ket = "Input"
                input_nilai()
                break
            if int(masuk) == 2:
                ket = "Edit"
                input_nilai()
            if int(masuk) == 4:
                rekap_nilai()
                break
            if int(masuk) == 3:
                ket = "Hapus"
                input_nilai()
                break
            else:
                print("="*(40))
                print("Masukan Nomer Menu Dengan Benar")
                print("="*(40))
        except:
            print("="*(40))
            print("Masukan Nomer Menu Dengan Benar")
            print("="*(40))

def input_nilai():
    while True:
        global list_siswa
        nama = str.title(input('Masukan Nama Siswa : '))
        if nama in list_siswa:
            pelajaran = str.title(input('Masukan Nama Pelajaran : '))
            if pelajaran in list_siswa[nama]["Pelajaran"]:
                option = ["UTS",'UAS', 'Praktikum', 'Tugas', "Kembali"]
                for i, j in enumerate(option):
                    print(f'{i+1}. {j}')
                opsi = input(f'Masukan nilai yang akan di {ket} : ')
                try:
                    if option[int(opsi)-1] == "Kembali":
                        break
                    else:

                        if ket == "Input" and list_siswa[nama]["Pelajaran"][pelajaran][option[int(opsi)-1]] !=0:
                            print("\nData Sudah di Input\n")
                        elif ket == "Hapus" :
                            if list_siswa[nama]["Pelajaran"][pelajaran][option[int(opsi)-1]] ==0:
                                print("\nData Kosong\n")
                            else:
                                list_siswa[nama]["Pelajaran"][pelajaran][option[int(opsi)-1]] = 0
                                break                        
                        else:
                            nilai = input(f'Masukan Nilai Siswa : ')
                            try :
                                list_siswa[nama]["Pelajaran"][pelajaran][option[int(opsi)-1]] = float(nilai)
                                break
                            except :
                                print("Masukan Nilai Siswa dengan Benar")
                except :
                    print("\nPilih Opsi dengan Teliti\n")
                    print (opsi)
                    print(option[int(opsi)-1])
                    print(list_siswa[nama]["Pelajaran"][pelajaran][option[int(opsi)-1]])
            else:
                print(f'\nTidak ada pelajaran {pelajaran}\n')

        else:
            print(f'\nTidak ada siswa bernama {nama}\n')

def IP():
    global ip1

    ip1 = 0
    f =0
    b= 0
    for i,j in list_siswa[nama_siswa]["Pelajaran"].items():
        a = (list_siswa[nama_siswa]["Pelajaran"][i]["index"])
        if a == 'A':
            f = 4
        elif a == "B":
            f = 3
        elif a == "C":
            f = 2
        elif a == "D":
            f = 1
        ip1 += f
        b += 1
    ip1 = ip1/b

def index():
    global list_siswa
    for i,j in list_siswa.items():
        for k,l in (j['Pelajaran'].items()):
            total1 = (list_siswa[i]["Pelajaran"][k]["UTS"]*30/100) + (list_siswa[i]["Pelajaran"][k]["UAS"]*30/100) + (list_siswa[i]["Pelajaran"][k]["Praktikum"]*30/100) + (list_siswa[i]["Pelajaran"][k]["Tugas"]*10/100)
            ip1 = total1/25
            if ip1 >= 3.5:
                index = 'A'
            elif ip1 < 3.5 and ip1 >= 2.5:
                index = 'B'
            elif ip1 < 2.5 and ip1 >= 2:
                index = 'C'
            elif ip1 < 2 and ip1 >= 1:
                index = 'D'
            else:
                index = 'E'
            list_siswa[i]["Pelajaran"][k]["index"] = index

while True:
    laman_utama = '''
Selamat Datang di Database Siswa Semester Genap Tahun Ajaran 2002 - 2003

Menu Utama:
1. Raport Mahasiswa
2. Kemahasiswaan
3. Editor Nilai Mahasiswa
4. Keluar    
'''
    print(laman_utama)
    pilihan = input('Pilihan Menu : ')
    try:
        if int(pilihan) == 4:
            break
        elif int(pilihan) == 1:
            raport()
        elif int(pilihan) == 2:
            kemahasiswaan()
        elif int(pilihan) == 3:
            nilai()
    except:
        print("Masukan Nilai dengan Teliti")
        
