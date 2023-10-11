def penghasilan():
    uang = int(input("Masukan Penghasilan Anda = "))
    if uang >= 10000000:
        n = 3
    elif 5000000 <= uang < 10000000:
        n = 2
    elif 1000000 <= uang < 5000000:
        n = 1
    else:
        n = 0
        print("Penghasilan Anda Tidak Valid")
    return n

def inputPenghasilan(jumlah):
    total_cost = 0
    for i in range(1, jumlah + 1):
        print(f"Informasi Hewan ke-{i}:")
        nama = input('Nama Hewan = ')
        umur = input('Umur Hewan = ')
        jenis = input('Jenis Hewan = ')
        harga = int(input('Harga Adopsi = '))
        print()
        total_cost += harga

    print(f"Total Harga Adopsi untuk {jumlah} hewan adalah {total_cost}.")

def pembelian():
    jumlah = penghasilan()
    inputPenghasilan(jumlah)

pembelian()