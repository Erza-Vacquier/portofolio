data =[
    {'No':'','emp_id': '', 'Name':'Andika Ryan', 'Gender': 'Male','Age': 24 , 'Department': 'Data', 'email': ''},
    {'No':'','emp_id': '','Name': 'Jennifer Smith','Gender': 'Female','Age': 32,'Department': 'Marketing', 'email': ''},
    {'No':'','emp_id': '','Name': 'Michael Johnson','Gender': 'Male', 'Age': 45, 'Department': 'Finance', 'email': ''},
    {'No':'','emp_id': '', 'Name': 'Emily Brown', 'Gender': 'Female', 'Age': 28, 'Department': 'Human Resources'},
    {'No':'','emp_id': '', 'Name': 'David Martinez', 'Gender': 'Male', 'Age': 37, 'Department': 'IT', 'email': ''}
    ]

from tabulate import tabulate

def read_data(data):
    print(tabulate(data, headers='keys', tablefmt='pretty'))

def errorOutput():
    print(''' 
    ====================================================
    Data yang anda input tidak valid! Silahkan coba lagi
    ====================================================
''')

def addData():
    while True:
        print('''
        Please input data!
        ''')
        while True:
            name = input("Masukan nama lengkap: ").title()
            if name.replace(' ','').isalpha() == True and len(name.split()) > 1 :
                break
            else:
                errorOutput()
        while True: 
            gender = input("Masukan gender (Male/Female): ").capitalize()
            if gender.isalpha() == True and (gender == 'Male' or gender == 'Female' ):
                break
            else:
                errorOutput()
        while True:
            try:
                age = int(input("Masukan umur: "))
                break
            except:
                errorOutput()
        while True:
            department = input("Masukan Departemen: ").capitalize()
            if department.replace(' ','').isalpha() == True:
                break
            else:
                errorOutput()
        break
    while True:
        konfirmasi = input(f'''
Berikut adalah data yang diinput: 
"Name: " {name} || "Gender: " {gender} || "Age: " {age} || "Department: " {department}

==========================================================
Apakah anda yakin untuk menambah data (y/n):          ''')
        if konfirmasi.lower() == 'y':
            new_data = {"Name": name, "Gender": gender, "Age": age, "Department": department}
            data.append(new_data)
            print('''
                  ====================Data berhasil ditambahkan!===================
                  ''')
            showData()
            break
        else:
            print('''
            ====================Data tidak jadi ditambahkan!====================
                  ''')
            showData()
            break

def showData():
    print(''' 
                                ==============================================================
                                            DAFTAR KARYAWAN PT. MIKROPOST INDONESIA
                                ==============================================================
''')
    for i in range(len(data)): #Kolom NO
        data[i]['No'] = i + 1
    for i in range(len(data)): #Kolom emp_id
        data[i]['emp_id'] = f"{data[i]['Department'][0:2].upper()}00{i+1}{data[i]['Name'].split()[0][0].upper()}{data[i]['Name'].split()[1][0].upper()}"
    for i in range(len(data)): #Kolom email
        data[i]['email'] = f"{data[i]['Name'].split()[0].lower()}.{data[i]['Name'].split()[1].lower()}@mikropost.co"
    print(tabulate(data,headers='keys',tablefmt='fancy_grid'))

def updateData():
    showData()
    while True:
        no_up = int(input("Masukan No. urut yang akan diupdate: "))
        if  0 < no_up <= len(data):
            print(f''' 
----------> Berikut data yang diakses {data[no_up -1]}
''')
            print('''' 
======================== Perubahan dan Pembaruan Data Karyawan ========================
    Kolom      1: Name         2. Gender       3. Age      4. Department
    
                    *Masukan Kategori Data yang akan diupdate
                    ''')
            while True:
                ubah = input('Ketik Kategori yang ingin diubah : ')
                if ubah == '1':
                    ubahKolom = input('Ketikkan nama baru terdiri dari nama depan dan nama belakang: ').title()
                    if ubahKolom == '' and ubahKolom.isalpha() == False and len(ubahKolom.split()) < 1:
                        print("============ Nama hanya mengandung huruf dan tidak boleh kosong, silakan ketikkan kembali============")
                    else:
                        data[no_up-1]['Name'] = ubahKolom.capitalize()
                        break
                elif ubah == '2':
                    gender_up = ['Male','Female']
                    ubahKolom = input('Ketikkan gender baru: ').capitalize()
                    if ubahKolom not in gender_up:
                        print("============ Gender terdiri dari male atau female dan tidak boleh kosong. Silakan ketikk kembali")
                    else:
                        data[no_up-1]['Gender'] = ubahKolom
                        break
                elif ubah == '3':
                    try:
                        ubahKolom = int(input("Masukan umur: "))
                        data[no_up-1]['Age'] = ubahKolom
                        break
                    except:
                        errorOutput()
                elif ubah == '4':
                    ubahKolom = input('Ketikkan departemen baru: ').upper()
                    if ubahKolom == '' or ubahKolom.isalpha() == False:
                        print("============ Departemen hanya mengandung huruf dan tidak boleh kosong, silakan ketikkan kembali============")
                    else:
                        data[no_up-1]['Department'] = ubahKolom.capitalize()
                        break
            showData()
            print('Data yang baru sudah berhasil ter-update ke dalam database')
            break
        else:
            print("Masukan Nomor yang sesuai!")
    
def deleteData():
    showData()
    try:
        while True:
            no = int(input("Masukan No. urut yang akan dihapus: "))
            if 0 < no <= len(data):
                konfirmasi = input(f'''
======== Apakah anda yakin untuk menghapus data (y/n): ''')
                if konfirmasi.isalpha() and konfirmasi.lower() == 'y':
                    del data[no-1]
                    print("Data berhasil dihapus!")
                    showData()
                    break
                elif konfirmasi.lower() == 'n':
                    print('''
                          
                          ===============Tidak ada data yang dihapus. Silahkan cek kembali==============
                          
                          ''')
                    showData()
                    break
                else:
                    errorOutput()
            else:
                print("===============Tidak ada karyawan dengan nomor tersebut. Silahkan masukan kembali ==============")
    except:
        errorOutput()

def featureData():
    showData()
    while True:
        pilihan = input('''
================ Menu Fitur Karyawan ================
    1. Filter Data
    2. Sorting Data
    3. Kembali ke Menu Utama  

    Pilih Nno menu: ''')
        if pilihan == '1':
            print('''' 
==================
Filter Berdasarkan:
a. Gender
b. Umur 
            ''')
            filtergpil = input('Ketik value yang menjadi filter : ')
            if filtergpil == 'a':
                pilu = input("Masukan filter gender (Male/Female): ").capitalize()
                gender = ('Male', 'Female')
                if pilu not in gender:
                    errorOutput()
                else:
                    filtered_data = [entry for entry in data if entry['Gender'] == pilu]
                    read_data(filtered_data)
                    break
            elif filtergpil == 'b':
                try:
                    filter_umur = int(input("Masukan batas ambang umur:"))
                    filtered_data = [entry for entry in data if entry['Age'] > filter_umur]
                    read_data(filtered_data)
                    break
                except ValueError:
                    print("Masukan umur berupa angka: ")
            else:
                errorOutput()
        elif pilihan == '2':
            print('''' 
==================
Sorting Berdasarkan:
a. Nama
b. Umur 
            ''')
            sortpil = input('Ketik value yang menjadi target sorting : ')
            if sortpil == 'a':
                sorted_data = sorted(data, key=lambda x: x['Name'])
                read_data(sorted_data)
                break
            elif sortpil == 'b':
                sorted_data = sorted(data, key=lambda x: x['Age'])
                read_data(sorted_data)
                break
            else:
                break
        else:
            mainData()

def mainData():
    while True:
        print('''
Menu Utama
1. Data Dashboard Karyawan Perusahaan
2. Tambah Karyawan Baru
3. Ubah Data Karyawan
4. Fitur Data
5. Hapus Data Karyawan
6. Logout
        ''')

        opsi = input("============== Pilih menu: ")
        if opsi == '1':
            showData()
        elif opsi == '2':
            addData()
        elif opsi == '3':
            updateData()
        elif opsi =='4':
            featureData()
        elif opsi =='5':
            deleteData()
        elif opsi == '6':
            print('''
==== Anda telah berhasil logout! ===
                  ''')
            exit()
        else:
            print("Input anda invalid!")

def authenticate():
    username = ['admin','Emily Brown']
    password = ['admin','HU004EB']
    while True:
        input_user = input('''
================== Selamat Datang ===================
Untuk dapat mengakses data silahkan masukan data anda
                           
Masukan Username: ''')
        if input_user in username:
            index = username.index(input_user)
            input_password = input('''
Masukan Password: ''')
            if input_password in password[index]:
                print(f'''
================== Login Berhasil =====================
Hello {input_user}!
            ''')
                mainData()
                break
            else:
                print("Incorrect Password!")
        elif input_user.isalpha() and input_user not in username:
            print("Incorrect Username")
        else:
            print("invalid username")      
authenticate()
