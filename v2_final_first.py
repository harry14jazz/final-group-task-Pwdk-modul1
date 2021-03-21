import string


def email_checker(email):  # andre@gmail.com
    if ' ' in email:
        return'Format Email salah gak boleh ada spasi'
    elif not email[0].isalnum():
        return 'Format email salah, Awalan hanya alpha numerik'
    elif email.count('@') != 1: 
        return 'Format Email salah @ ngaco'
    else:
        index = email.index('@')   
        if not email[index+1].isalnum(): 
            return 'Format Email salah'
        else:
            email_split = email.split('@')
            username = email_split[0]
            hosting = email_split[1]
            for i in username:
                if not (i.isalnum() or i == '_' or i == '.'):
                    return "Sorry, only latter, numeric, underscores, and period allowed"
                    break
                else:
                    continue
            if '.' not in hosting:  # cek hosting [gmail][co][id][cc]
                return 'format hosting salah'
            else:
                split_hosting = hosting.split('.')
                ekstensi = split_hosting[1:]
                domain = split_hosting[0]
                if not domain.isalnum():
                    return "Domain salah cuma boleh alpha numerik"
                elif len(ekstensi) > 2:
                    return "ekstensi lebih dari 2"
                else:
                    for i in ekstensi:
                        if not i.isalpha() or len(i) > 5:
                            return "ekstensi salah bukan alphabet atau lebih dari 5"
                            break
        return False


def register(data):
    list_pass = []

    list_uid = []

    special_char = string.punctuation
    
    for mhs in data:
        list_pass.append(data[mhs]['password'])
        list_uid.append(data[mhs]['user_id'])

    try:
        status_uid = True
        incomplete = True
        index_mhs = 'mhs{}'.format(len(data)+1)
        data[index_mhs] = {}

        while status_uid:
            correctness = True
            user_id = input('Masukkan UserId: ') 
            for char in user_id: 
                if char in special_char:
                    correctness = False
                else:
                    pass 

            if correctness == False:
                print('Input Invalid')
            else:
                if user_id.isalpha() or user_id.isdigit(): 
                    print('Format user_id salah')
                elif len(user_id) > 20 or len(user_id) <= 6:
                    print('Tidak sesuai jumlah karakter') 
                elif user_id in list_uid:
                    print('UserId sudah ada')
                else:
                    data[index_mhs]['user_id'] = user_id
                    status_uid = False
                    # break

        while incomplete:
            ada_digit = False
            ada_alpha = False
            ada_spc = False
            ada_cap = False
            password = input('Masukkan Password: ')
            if len(password) < 8:
                print("minimal 8 karakter")
            else:
                for i in password:  
                    if i.isdigit():
                        ada_digit = True
                    elif i.isupper(): 
                        ada_cap = True
                    elif i.isalpha():
                        ada_alpha = True
                    elif i in special_char:
                        ada_spc = True
                    else:
                        continue
                if ada_spc == True and ada_alpha == True and ada_digit == True and ada_cap == True: 
                    data[index_mhs]['password'] = password
                    pass_status = False
                    break
                else:
                    print('harus mengandung capital, angka, alphabet dan special char')

        while incomplete:
            email = input('Masukkan Email: ')
            email_checking = email_checker(email) 
            if email_checking == False:
                data[index_mhs]['email'] = email
                break
            else:
                print(email_checker(email))

        while incomplete:
            phone = input('Masukkan No Hp (+62): ')
            if not phone.isdigit():
                print('Invalid Input')
            elif len(phone) < 11 or len(phone) > 13:
                print('Format No Hp salah')
            else:
                phone = int(phone)
                data[index_mhs]['phone'] = phone
                break

        while incomplete:
            name = input('Masukkan Nama: ')

            name_split = name.split(' ')   
            salah = 0  # salah = True
            for value in name_split:   
                if not value.isalpha():
                    salah = -1  # salah = False
                else:
                    pass
                
            if salah != 0:
                print('Input Invalid')
            else:
                data[index_mhs]['name'] = name
                break

        while incomplete:
            gender = input('Masukkan Gender: ')
            if not gender.isalpha():
                print('Format input salah')
            else:
                gender_check = gender.title()
                if gender_check == 'Male' or gender_check == 'Female':
                    data[index_mhs]['gender'] = gender_check
                    break
                else:
                    print('Format input salah')

        while incomplete:
            try:
                usia = int(input('Masukkan Usia: '))
                if usia < 17 or usia > 80:
                    print('Usia tidak sesuai dalam batas yang benar')
                else:
                    data[index_mhs]['age'] = usia
                    break
            except:
                print('Input Invalid!')

        while incomplete:
            job = input('Masukkan Pekerjaan: ')
            job_split = job.split(' ')
            salah = 0
            for i in job_split:
                if not i.isalpha():
                    salah += 1
                else:
                    continue
            if salah != 0:
                print('Input Invalid')
            else:
                data[index_mhs]['job'] = job
                break

        while incomplete:
            hobby = input('Masukkan Hobby: ') 
            hobby_data = hobby.split(',')
            hobby_list = []

            for value in hobby_data:
                hobby_list.append(value)

            data[index_mhs]['hobby'] = hobby_list
            break

        # print('Alamat:')
        data[index_mhs]['address'] = {}

        while incomplete:
            city = input('Masukkan Kota: ')
            
            city_split = city.split(' ')
            salah = 0  # salah = True
            for value in city_split:
                if not value.isalpha():
                    salah = -1  # salah = False
                else:
                    pass
            if salah != 0:
                print('Input Invalid')
            else:
                data[index_mhs]['address']['city'] = city
                break

        while incomplete:
            rt = input('Masukkan RT: ')
            if not rt.isdigit():
                print('Format input salah')
            else:
                data[index_mhs]['address']['rt'] = rt
                break

        while incomplete:
            rw = input('Masukkan RW: ')
            if not rw.isdigit():
                print('Format input salah')
            else:
                data[index_mhs]['address']['rw'] = rw
                break

        while incomplete:
            zip_c = input('Masukkan Zip Code: ')
            if not zip_c.isdigit():
                print('Format input salah')
            else:
                data[index_mhs]['address']['zip_c'] = zip_c
                break

        # print('Geo: ')
        data[index_mhs]['address']['geo'] = {}
        while incomplete:
            try:
                lat = float(input('Masukkan Latitude: '))
                data[index_mhs]['address']['geo']['lat'] = lat
                break
            except:
                print('Format input salah')

        while incomplete:
            try:
                longitude = float(input('Masukkan Longitude: '))
                data[index_mhs]['address']['geo']['longitude'] = longitude
                break
            except:
                print('Format input salah')

        try:
            save = input('Simpan Data (Y/N): ').lower()
            if not save.isalpha():
                print('Hanya menerima inputan karakter')
            elif save == 'y':
                print('User berhasil dibuat')
            elif save == 'n':
                print('User tidak dibuat')
                data.pop(index_mhs)
            else:
                print('Pilihan tidak tersedia')
        except:
            print('Inputan tidak valid')

    except:
        print('Inputan tidak valid!')


def menu():
    print('1. User Profile(Sesuai dengan Login)')
    print('2. Kalkulator')
    print('3. Konversi Romawi')
    print('4. Konversi Kode Morse')
    print('5. Hitung hari ... (masukkan hari ... masukkan angka ..) dst')
    print('6. Kamus Hari: Atau Project Bebas')
    print('7. Konversi Jumlah Hari ... (tahun, bulan, minggu, hari)')
    print('8. Nilai Faktorial')
    print('9. Jumlah dan Deret Fibonnaci')
    print('10. Caesar Cipher')
    print('11. Setting User: Akan keluar UserId, Password dan Email')
    print('12. CRUD == > Mini Apps v 1.0')
    print('13. Exit')
    print('=====================================')


def kalkulator():
    try:
        x = float(input("Masukkan angka 1 : "))
        y = float(input("Masukkan angka 2 : "))
        opr = input("Masukkan operator (hanya terbatas pada + / - * ): ")
        if opr == '+':
            hasil = x + y
            return f"Hasil dari {x} + {y} = {hasil}"
        elif opr == '-':
            hasil = x - y
            return f"Hasil dari {x} - {y} = {hasil}"
        elif opr == '*':
            hasil = x * y
            return f"Hasil dari {x} * {y} = {hasil}"
        elif opr == '/':
            hasil = x / y
            return f"Hasil dari {x} / {y} = {hasil}"
        else:
            return "Maaf, tidak menerima operator yang anda masukkan"

    except ValueError:
        return "Maaf, hanya menerima angka"


def konverterAR():
    Input = input("Silahkan masukkan angka Romawi : ")
    inputnya_arabic = True
    # Dictionary Arabic-Romawi
    ar_rom = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    # Pemeriksaan input berupa Arabic atau Romawi
    if Input.isdigit() == False:
        inputnya_arabic = False

    if inputnya_arabic == True:  # Translasi Arabic-Romawi
        # contohnya 00232 ==> tidak valid
        if Input[0] == '0' and len(Input) > 1:
            ret = "Angka Arabic yang anda masukkan tidak valid"
        else:  # Angka Arabic Valid
            inp = int(Input)
            if inp < 0 or inp > 4000:
                ret = "Angka Arabic melebihi jangkauan 0-4000"
            elif inp == 0:
                ret = "Sistem angka Romawi tidak mengenal angka nol"
            elif inp == 4000:
                ret = "Angka Romawi : MMMM"
            else:  # ---------- Mulai Konversi Arabic-Romawi
              # Mencari Digit Angka Input
                d4 = inp // 1000
                d3 = (inp - d4*1000) // 100
                d2 = (inp - d4*1000 - d3*100) // 10
                d1 = inp - d4*1000 - d3*100 - d2*10
                arabic = [d1, d2, d3, d4]
                romawi = []
                # Konversi dan simpan ke romawi=[]
                for i in range(4):  # 4=len(arabic)
                    if arabic[i] < 4:
                        romawi.append(arabic[i]*ar_rom[10**i])
                    elif 4 < arabic[i] < 9:
                        romawi.append(ar_rom[5*10**i] +
                                      (arabic[i]-5)*ar_rom[10**i])
                    else:
                        romawi.append(
                            ar_rom[10**i]+ar_rom[(arabic[i]+1)*10**i])
                 # Output Romawi
                    out = ""
                for i in range(3, -1, -1):
                    out += romawi[i]
                    ret = f"Angka Romawi : {out}"
    else:
        try:
            # Handling Error Input berupa angka negatif/float
            float_input = float(Input)
            ret = "Tidak menerima angka negatif maupun desimal"
        except:
            if Input.isalpha() == False:  # Handling error input yang bkan digit/float/pure alfabet
                return "Format angka yang dimasukkan salah. Input bukan angka Arabic ataupun angka Romawi"
            else:
                for i in Input:  # Handling error input bukan angka Romawi
                    if i not in ['M', 'D', 'C', 'L', 'X', 'V', 'I']:
                        ret = "Input alfabet yang dimasukkan tidak termasuk angka Romawi"
                        break
                else:  # Mulai Konversi Romawi-Arabic
                    # Dictionary Baru Romawi-Arabic dari Arabic Romawi
                    rom_ar = {}
                    for i, j in ar_rom.items():
                        rom_ar[j] = i
                    # Pengelompokkan Input (Romawi) ==> Hasilnya berupa variabel grup bertipe list
                        indx = [0]*4
                        G = [['M'], ['M', 'D', 'C'], [
                            'C', 'L', 'X'], ['X', 'V', 'I']]
                    for j in range(3):
                        for i in range(indx[j], len(Input)):
                            if Input[i] not in G[j]:
                                indx[j] = i
                                break
                        else:
                            indx[j] = len(Input)
                        indx[j+1] = indx[j]

                        m = Input[0:indx[0]]
                        mdc = Input[indx[0]:indx[1]]
                        clx = Input[indx[1]:indx[2]]
                        xvi = Input[indx[2]:len(Input)]
                        grup = [m, mdc, clx, xvi]
                        out = 0

                        # -------- Konversi Angka Romawi-Arabic Untuk Setiap Kelompok
                    for k in range(0, 4):
                        if k == 0:
                            if len(m) > 4:
                                ret = "Angka Romawi tidak valid"
                                break
                            else:
                                for i in m:
                                    out += rom_ar[i]
                        else:
                            if (set(grup[k]) - set(G[k])) != set():
                                ret = "Angka Romawi tidak valid"
                                break
                            elif G[k][0] in grup[k]:
                                if len(grup[k]) != 2 or grup[k] != G[k][2]+G[k][0]:
                                    ret = "Angka Romawi tidak valid"
                                    break
                                else:
                                    out += rom_ar[grup[k][1]] - \
                                        rom_ar[grup[k][0]]
                            elif G[k][1] not in grup[k]:
                                if len(grup[k]) > 3:
                                    ret = "Angka Romawi tidak valid"
                                    break
                                else:
                                    for i in grup[k]:
                                        out += rom_ar[i]
                            elif grup[k].count(G[k][1]) != 1 or grup[k].index(G[k][1]) > 1 or len(grup[k]) > 4:
                                ret = "Angka Romawi tidak valid"
                                break
                            else:
                                if grup[k].index(G[k][1]) == 1:
                                    if grup[k] != (G[k][2] + G[k][1]):
                                        ret = "Angka Romawi tidak valid"
                                        break
                                    else:
                                        out += rom_ar[grup[k][1]
                                                      ] - rom_ar[grup[k][0]]
                                else:
                                    for i in grup[k]:
                                        out += rom_ar[i]
                    else:
                        ret = f"Angka Arabic : {out}"
    return ret


def morse():
    kodemorse = {
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
        "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
        ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
    }
    tukar = ""
    kata = input("Masukkan kata : ")
    if "|" in kata:
        kode = kata.split("|")
        if '' in kode:
            kode.remove('')
        for a in kode:
            if a in kodemorse.values():
                for i, j in kodemorse.items():
                    if j == a:
                        tukar += str(i)
            else:
                print("Kode yang anda masukkan salah")
                break
        else:
            print(
                "Kode morse yang anda masukkan {} jika diubah menjadi kata-kata menjadi {}".format(kata, tukar))
    else:
        try:
            fl = float(kata)
            if fl.is_integer():
                katasplit = kata.split()
                for a in katasplit:
                    for b in a:
                        if b not in kodemorse.keys():
                            print("Tidak bisa dikonversi ke kode morse")
                            break
                        else:
                            tukar += kodemorse.get(b) + '|'
                else:
                    print("Kata yang anda masukkan adalah {} jika diubah menjadi kode morse menjadi {}".format(
                        kata, tukar))
            else:
                print("Tidak menerima angka pecahan")
        except:
            katasplit = kata.split()
            for a in katasplit:
                for b in a:
                    if b not in kodemorse.keys():
                        print("Tidak bisa dikonversi ke kode morse")
                        break
                    else:
                        tukar += kodemorse.get(b) + '|'
            else:
                print("Kata yang anda masukkan adalah {} jika diubah menjadi kode morse menjadi {}".format(
                    kata, tukar))


def hari():
    hari = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
    try:
        day = input("Masukan nama hari : ").lower()
        angka_input = int(input('Masukan jumlah hari: '))
        if day not in hari:
            return 'Tidak ada nama hari/Nama hari yang anda masukan salah'
        else:
            index_hari = hari.index(day)
            expected_index_day = (index_hari + angka_input) % 7
            expected_day = hari[expected_index_day]
            return f'hari ini hari{day}, {angka_input} hari lagi adalah hari {expected_day}'
    except:
        return "Jumlah tidak bisa desimal maupun string "


def hari1():
    hari = {'Senin': 'Monday',
            'Selasa': 'Tuesday',
            'Rabu': 'Wednesday',
            'Kamis': 'Thursday',
            'Jumat': 'Friday',
            'Sabtu': 'Saturday',
            'Minggu': 'Sunday',
            }

    pilih = str(input('Masukkan Nama Hari : '))
    pilih = pilih.title()
    if pilih.isalpha():  # or ' ':
        for i, j in hari.items():
            if i == pilih:
                return f"Hari yg anda pilih ({pilih}) dalam bahasa inggris adalah ({j})"
                break
            elif j == pilih:
                return f"The Day that you choose is ({pilih}) in Bahasa is ({i})"
                break
        else:
            return 'Nama Hari Tidak Ditemukan'
    else:
        return 'Hanya Menerima Alfabet'


def jumlahhari():
    try:
        x = int(input("Masukkan jumlah hari : "))
        if x > 4000:
            print("Jumlah hari diatas batas")
        elif x <= 4000 and x >= 0:
            tahun = int(x // 365)
            modtahun = int(x % 365)
            bulan = int(modtahun // 30)
            modbulan = int(modtahun % 30)
            minggu = int(modbulan // 7)
            hari = int(modbulan % 7)
            return f'{"{0:0=2d}".format(tahun)} Tahun {"{0:0=2d}".format(bulan)} Bulan {"{0:0=2d}".format(minggu)} Minggu {"{0:0=2d}".format(hari)} Hari'
        elif x < 0:
            return 'Jumlah Hari Dibawah Batas'
            # print("Jumlah hari dibawah batas")
    except:
        return 'Jumlah hari yang anda masukan salah'
        # print("Jumlah hari yg anda masukkan salah")


def faktorial():
    try:
        num = int(input("Masukan angka : "))
        f = 1
        if num < 0:
            return "angka faktorial harus diatass 0"
        elif num == 0:
            return "Faktorial 0 adalah 0"
        else:
            for i in range(1, num + 1):
                f = f*i
            return f"Faktorial {num} adalah {f}"
        print(faktorial(num))
    except:
        return "Input Invalid"


def fibo():
    try:
        angka = int(input("Masukkkan Angka : "))
        urutan = [1, 1]
        x = 2
        for i in range(2, angka):
            urutan.append(urutan[i - 2] + urutan[i - 1])
            x += urutan[i]
        print(urutan)
        print(f"{angka} deret angka pertama baris fibonacci dan jumlahnya"), fibo(
            angka)
    except:
        return x


def caesarcipher():
    alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    list_kosong = []
    try:
        input_kata = str(input("Masukan kata: ")). lower()
        angka = int(input("Masukan Angka:"))
        if input_kata.isalpha() == True:

            for x in input_kata:
                index_return = alfabet.index(x)
                converter = (index_return + angka) % 26
                accessing = alfabet[converter]
                list_kosong.append(accessing)
            else:
                list_kosong = "" . join(list_kosong)
                return "{} setelah di convert menjadi {}". format(input_kata, list_kosong)
        else:
            return "kata harus alfabet"
    except:
        return "angka harus integer"


def create(data):
    try:
        mhs_list = [k for k in data]  # get all mahasiswa in dict

        mhs_input = input('Masukkan Nama Mahasiswa: ').lower()
        nilai_input = int(input('Masukkan Nilai: '))

        if mhs_input in mhs_list:
            print('Nama sudah ada')

        name_split = mhs_input.split(' ')
        correct = True

        for value in name_split:
            if not value.isalpha():
                correct = False
            else:
                pass
        if correct != True:
            print('Input Nama Invalid')
        elif nilai_input < 0 or nilai_input > 100:
            print('Nilai di luar batas')
        else:
            key_mhs = mhs_input.replace(' ', '_')
            data[key_mhs] = nilai_input
            print('Data Mahasiswa berhasil dibuat')
    except:
        print('Tipe data input salah')


def update(data):
    print('===== Pilih Menu Update =====')
    print('1. Update Nama Mahasiswa')
    print('2. Update Nilai')
    try:
        mhs_list = [k for k in data]
        correctness = True

        choice = int(input('Masukkan pilihan menu update: '))
        if choice == 1:
            mhs_input = input(
                'Masukkan Nama Mahasiswa yg Dicari: ').lower()
            mhs_new = input('Masukkan Nama Mahasiwa yg Baru: ')

            if mhs_input not in mhs_list:
                correctness = False
            else:
                pass

            name_split = mhs_new.split(' ')

            for value in name_split:
                if not value.isalpha():
                    correctness = False
                else:
                    pass

            if correctness == True:
                get_nilai = data.get(mhs_input)
                data.pop(mhs_input)
                key_mhs = mhs_new.replace(' ', '_')
                data[key_mhs] = get_nilai
                print('Data berhasil diupdate')
            else:
                print('Input Mahasiswa Baru Invalid atau Matkul tidak ada')

        elif choice == 2:
            try:
                mhs_input = input(
                    'Masukkan Nama Mata Kuliah Yang Diganti: ')
                nilai_new = int(input('Masukkan Nilai Terbaru: '))
            except:
                print('Tipe data salah')

            if mhs_input not in mhs_list:
                correctness = False
            else:
                pass

            if correctness == True:
                data[mhs_input] += nilai_new
                if data[mhs_input] < 0:
                    data[mhs_input] = 0
                else:
                    pass
                print('Data berhasil diupdate')
            else:
                print('Matkul tidak ada2')

        else:
            print('Pilihan tidak tersedia')
    except:
        print('Tipe data inputan tidak valid')


def read(data):
    if len(data) == 0:
        print('Data tidak ada')
    else:
        print('Nama : Nilai')
        for k, v in data.items():
            print(k, ' : ', v)


def delete(data):
    print('1. Hapus Sebagian Data')
    print('2. Hapus Seluruh Data')
    print('------------------------')
    try:

        list_mhs = [k for k in data]

        found_status = False
        choice = int(input('Masukkan Pilihan: '))
        if choice == 1:
            mhs_input = input('Masukkan Nama Mahasiswa: ').lower() 
            for mhs in list_mhs:
                if mhs == mhs_input:
                    found_status = True
                    break
                else:
                    pass

            if found_status == True:
                data.pop(mhs_input)
                print('Data berhasil dihapus')
            else:
                print('Mahasiswa tidak ditemukan')
        elif choice == 2:
            data.clear()
            print('Seluruh Data berhasil dihapus')
    except:
        print('Tipe data inputan salah')


def user_profile(user, data):
    for index in data[user]:
        if index == 'user_id' or index == 'password':
            pass
        else:
            if isinstance(data[user][index], dict):
                print(f'{index}:')
                for key, value in data[user][index].items():
                    if isinstance(data[user][index][key], dict):
                        print(f'       {key}:')
                        for k2, v2, in data[user][index][key].items():
                            print('         {}: {}'.format(k2, v2))
                    else:
                        print('     {}: {}'.format(key, value))
            else:
                print('{}: {}'.format(index, data[user][index]))


def setting_user(user, data):
    for index in data[user]:
        if index == 'user_id' or index == 'password' or index == 'email':
            print(f'{index}: {data[user][index]}')
        else:
            pass


data = {
    'mhs1': {
        'user_id': 'uidmhs1',
        'name': 'Harry',
        'password': 'pWdK@121',
        'email': 'harry14jazz@gmail.com',
        'phone': '082226421332',
        'gender': 'Male',
        'age': 23,
        'job': 'Pengangguran',
        'hobby': ['listening podcast', 'listening jazz'],
        'address': {
            'city': 'Pekanbaru',
            'rt': '002',
            'rw': '003',
            'zip_c': 28282,
            'geo': {
                'lat': -1234.567,
                'long': 1234.567
            }
        }
    },
    'mhs2': {
        'user_id': 'uidmhs2',
        'name': 'Yonko Jek',
        'password': 'pWdK@122',
        'email': 'yonkojek@gmail.com',
        'phone': '082226421332',
        'gender': 'Male',
        'age': 28,
        'job': 'Pengangguran',
        'hobby': ['listening podcast', 'listening jazz'],
        'address': {
            'city': 'Bandung',
            'rt': '002',
            'rw': '003',
            'zip_c': 28141,
            'geo': {
                'lat': -1234.567,
                'long': 1234.567
            }
        }
    }
}

first_menu = True
login_status = False
while first_menu:
    print('### Selamat datang di XXYY Apps ###')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    print('------------------------------------')
    try:
        menu1_input = int(input('Masukkan Pilihan: '))

        if menu1_input == 1:
            register(data)
            first_menu = True

        elif menu1_input == 2:
            chance = 5
            login_try = 0
            # coba login

            # buat list kumpulan uid dan pass
            new_users = {}
            for mhs in data:
                new_users[data[mhs]['user_id']] = data[mhs]['password']

            list_uid = [k for k in new_users]

            while login_try < 5:
                uid = input('Masukkan UserID:')
                password = input('Masukkan Password: ')
                uidpass_input = (uid, password)
                login_try += 1

                pass_salah = False
                approve = False
                if uidpass_input[0] not in list_uid:
                    print('ID Tidak terdaftar')
                    if login_status == False:
                        if (chance - login_try) == 0:
                            print('Exit, bye')
                            break
                        elif chance - login_try == 1:
                            print('this is your last chance')
                        else:
                            print('Kesempatan anda tinggal {} kali lagi\n'.format(
                                chance - login_try))
                else:
                    for k, v in new_users.items():
                        if k == uidpass_input[0]:
                            if v == uidpass_input[1]:
                                approve = True
                                break
                            else:
                                pass_salah = True
                        else:
                            pass

                    if approve == True and pass_salah == False:
                        for index in data:
                            for k in data[index]:
                                if uidpass_input[0] == data[index][k]:
                                    user_login = index
                                else:
                                    pass
                        print('UserID dan Password benar, silakan masuk.\n')
                        login_status = True
                        first_menu = False
                        break
                    elif pass_salah == True and approve == False:
                        print("Password salah")
                        if login_status == False:
                            if (chance - login_try) == 0:
                                print('Exit, bye')
                                break
                            elif chance - login_try == 1:
                                print('this is your last chance')
                            else:
                                print('Kesempatan anda tinggal {} kali lagi\n'.format(
                                    chance - login_try))
                    else:
                        print("Kombinasi ID & Password salah")
                        if login_status == False:
                            if (chance - login_try) == 0:
                                print('Exit, bye')
                                break
                            elif chance - login_try == 1:
                                print('this is your last chance')
                            else:
                                print('Kesempatan anda tinggal {} kali lagi\n'.format(
                                    chance - login_try))

        elif menu1_input == 3:
            first_menu = False
        elif menu1_input == 8:
            print(data)
        else:
            print('Pilihan Menu tidak tersedia')
    except:
        print('Tipe Data Inputan Salah')

if first_menu == False and login_status == True:
    second_menu = True
    menu2_input = 0

    while second_menu:
        print('=========== Home Menu ===============')
        menu()
        try:
            menu2_input = int(input('Masukkan Pilihan Menu:'))
            if menu2_input == 1:
                user_profile(user_login, data)
            elif menu2_input == 2:
                print(kalkulator())
            elif menu2_input == 3:
                print(konverterAR())
            elif menu2_input == 4:
                print(morse())
            elif menu2_input == 5:
                print(hari())
            elif menu2_input == 6:
                print(hari1())
            elif menu2_input == 7:
                print(jumlahhari())
            elif menu2_input == 8:
                print(faktorial())
            elif menu2_input == 9:
                print(fibo())
            elif menu2_input == 10:
                print(caesarcipher())
            elif menu2_input == 11:
                setting_user(user_login, data)
            elif menu2_input == 12:
                mahasiswa = {
                    'mhsdeflt1': 75,
                    'mhsdeflt2': 80
                }
                while login_status:
                    popup = True
                    print('------- Menu Mini Aplikasi --------')
                    print('1. Cetak Isi daftar Mahasiswa (Read)')
                    print('2. Menambah Data Mahasiswa (Create)')
                    print('3. Mengubah Data Mahasiswa (Update)')
                    print('4. Menghapus Data Mahasiswa (Delete)')
                    print('5. Keluar Aplikasi (Exit)')
                    print('-----------------------------------')
                    try:
                        menu = int(input('Masukkan Pilihan Menu: '))
                        if menu == 1:
                            while popup:
                                read(mahasiswa)
                                # popup
                                print('1. Kembali ke Menu (yg sedang diakses)')
                                print('2. Kembali Ke Menu Utama')
                                try:
                                    popup_menu = int(
                                        input('Masukkan Pilihan Menu: '))
                                    if popup_menu == 1:
                                        continue
                                    elif popup_menu == 2:
                                        break
                                    else:
                                        print(
                                            'Angka yang anda input tidak tersedia dalam menu\n')
                                except:
                                    print('Tidak menerima String atau Desimal\n')
                        elif menu == 2:
                            while popup:
                                create(mahasiswa)
                                # popup
                                print('1. Kembali ke Menu (yg sedang diakses)')
                                print('2. Kembali Ke Menu Utama')
                                try:
                                    popup_menu = int(
                                        input('Masukkan Pilihan Menu: '))
                                    if popup_menu == 1:
                                        continue
                                    elif popup_menu == 2:
                                        break
                                    else:
                                        print(
                                            'Angka yang anda input tidak tersedia dalam menu\n')
                                except:
                                    print('Tidak menerima String atau Desimal\n')
                        elif menu == 3:
                            while popup:
                                update(mahasiswa)
                                # popup
                                print('1. Kembali ke Menu (yg sedang diakses)')
                                print('2. Kembali Ke Menu Utama')
                                try:
                                    popup_menu = int(
                                        input('Masukkan Pilihan Menu: '))
                                    if popup_menu == 1:
                                        continue
                                    elif popup_menu == 2:
                                        break
                                    else:
                                        print(
                                            'Angka yang anda input tidak tersedia dalam menu\n')
                                except:
                                    print('Tidak menerima String atau Desimal\n')
                        elif menu == 4:
                            while popup:
                                delete(mahasiswa)
                                # popup
                                print('1. Kembali ke Menu (yg sedang diakses)')
                                print('2. Kembali Ke Menu Utama')
                                try:
                                    popup_menu = int(
                                        input('Masukkan Pilihan Menu: '))
                                    if popup_menu == 1:
                                        continue
                                    elif popup_menu == 2:
                                        break
                                    else:
                                        print(
                                            'Angka yang anda input tidak tersedia dalam menu\n')
                                except:
                                    print('Tidak menerima String atau Desimal\n')
                        elif menu == 5:
                            menu2_input = 0
                            print('Exit Bye')
                            second_menu = False
                            break
                        else:
                            print('Menu tidak ada')
                    except:
                        print('Pilihan tidak tersedia')
            elif menu2_input == 13:
                print('Exit, Bye.')
                second_menu = False
            else:
                print('Pilihan tidak ada')
        except:
            print('Tipe Data Inputan salah!')
else:
    print('Exit, Bye.')



