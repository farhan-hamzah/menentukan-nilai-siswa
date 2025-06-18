class Kelas:
    def kelasSiswa(self, nama, nilai, idx):
        self.nama = nama
        self.nilai = nilai
        self.idx = idx
n = int(input())
x = str(input())
data = []
for i in range (n):
    nama = str(input())
    nilai = int(input())
    if nilai > 80:
        idx = "A"
    elif nilai <= 80 and nilai > 70:
        idx = "AB"
    elif nilai <= 70 and nilai >65:
        idx = "B"
    elif nilai <= 65 and nilai > 60:
        idx = "BC"
    elif nilai <= 60 and nilai > 50:
        idx = "C"
    elif nilai <=50 and nilai < 40:
        idx = "D"
    else:
        idx = "E"
    s = Kelas()
    s.kelasSiswa(nama, nilai, idx)
    data.append(s)
for i in data:
    if i.idx == x:
        print(i.nama, i.nilai, i.idx)