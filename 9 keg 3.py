import shelve
a = open("L200180163.txt", "r")
NIM = a.readline()
Tanggal_lahir = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Saidah")
a["b"] = [NIM, Tanggal_lahir, Nama, Kota]
a.close
