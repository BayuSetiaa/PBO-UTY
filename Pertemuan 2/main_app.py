daftarMatkul = []

def menu():
    print(10*'=','MENU KRS',10*'=')
    print(5*' ','1. Input KRS')
    print(5*' ','2. Cetak KRS')
    print(5*' ','0. Exit')

def matkul():
    print(50 * '=')
    print(8 * ' ', 'MATAKULIAH KULIAH YANG TERSEDIA', ' ' * 8)
    print(50 * '=')
    print(5 * ' ', '1. Algoritma Pemrograman')
    print(5 * ' ', '2. Struktur dan Basis Data')
    print(5 * ' ', '3. Teknologi Berbasis Objek')
    print(5 * ' ', '4. Metodelogi Desain Perangkat Lunak')
    print(5 * ' ', '5. Pemrograman Berbasis Objek')
    print(5 * ' ', '6. Coding Machine Learning')

def user():
    print('MASUKAN DATA DIRI ANDA')
    nama = str(input("Nama : "))
    npm = int(input("Npm : "))
    jurusan = str(input("Jurusan : "))

while True:
    menu()
    pilih = int(input('Pilih Menu = '))

    if pilih == 1:
        user()
        ipk = float(input("Masukan IPK Anda = "))
        matkul()
        if 2.5 <= ipk <= 2.99:
            kondisi = 1
            while kondisi <= 3:
                try:
                    nomor_matkul = int(input(f'Pilih Nomor Matkul ke-{kondisi}: '))
                    if 1 <= nomor_matkul <= 6 and nomor_matkul not in daftarMatkul:
                        _daftarMatkul = [
                            'Algoritma Pemrograman',
                            'Struktur dan Basis Data',
                            'Teknologi Berbasis Objek',
                            'Metodelogi Desain Perangkat Lunak',
                            'Pemrograman Berbasis Objek',
                            'Coding Machine Learning'
                        ][nomor_matkul - 1]
                        daftarMatkul.append(_daftarMatkul)
                        kondisi += 1
                    else:
                        print('Nomor Matkul tidak valid atau sudah dipilih. Silakan masukkan nomor yang sesuai.')
                except ValueError:
                    print('Masukkan angka yang valid.')

        elif 3.0 <= ipk <= 3.49:
            kondisi = 1
            while kondisi <= 4:
                try:
                    nomor_matkul = int(input(f'Pilih Nomor Matkul ke-{kondisi}: '))
                    if 1 <= nomor_matkul <= 6 and nomor_matkul not in daftarMatkul:
                        _daftarMatkul = [
                            'Algoritma Pemrograman',
                            'Struktur dan Basis Data',
                            'Teknologi Berbasis Objek',
                            'Metodelogi Desain Perangkat Lunak',
                            'Pemrograman Berbasis Objek',
                            'Coding Machine Learning'
                        ][nomor_matkul - 1]
                        daftarMatkul.append(_daftarMatkul)
                        kondisi += 1
                    else:
                        print('Nomor Matkul tidak valid atau sudah dipilih. Silakan masukkan nomor yang sesuai.')
                except ValueError:
                    print('Masukkan angka yang valid.')

        elif 3.5 <= ipk <= 4.0:
            kondisi = 1
            while kondisi <= 6:
                try:
                    nomor_matkul = int(input(f'Pilih Nomor Matkul ke-{kondisi}: '))
                    if 1 <= nomor_matkul <= 6 and nomor_matkul not in daftarMatkul:
                        _daftarMatkul = [
                            'Algoritma Pemrograman',
                            'Struktur dan Basis Data',
                            'Teknologi Berbasis Objek',
                            'Metodelogi Desain Perangkat Lunak',
                            'Pemrograman Berbasis Objek',
                            'Coding Machine Learning'
                        ][nomor_matkul - 1]
                        daftarMatkul.append(_daftarMatkul)
                        kondisi += 1
                    else:
                        print('Nomor Matkul tidak valid atau sudah dipilih. Silakan masukkan nomor yang sesuai.')
                except ValueError:
                    print('Masukkan angka yang valid.')

        else:
            print("IPK anda tidak valid")

    elif pilih == 2:
        for count, ale in enumerate(daftarMatkul, 1):
            print(count, ale)

    elif pilih == 0:
        exit()

    else:
        print('Pilihan Anda Tidak terdaftar')
