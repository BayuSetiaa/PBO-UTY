class Kucing:
    def __init__(self, nama , umur , warna, harga):
        self.nama = nama 
        self.umur = umur 
        self.warna = warna 
        self.harga = harga 

    def info(self):
        print("Nama Kucing : " + self.nama + ", Umur Kucing :" + str(self.umur) + "Tahun, Warnanya : " + (self.warna) + ", Harga :" + str(self.harga))

    def meong(self):
        print("miawww..")

    def lari(self):
        print("berlari lari")

kucing_1 = Kucing("miko", 3 , "Oren" , 500000)
kucing_2 = Kucing("ruby", 4 , "Putih" , 300000)
kucing_3 = Kucing("cici", 2 , "Abu-abu" , 400000)

print("Nama Kucing 1 :", kucing_1.nama)
print("Umur Kucing 1 :", kucing_1.umur)
print("Warna Kucing 1 :", kucing_1.warna)
print("Harga  Kucing 1 :", kucing_1.harga)
print()
kucing_1.meong()
kucing_1.info()