Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Saidah Nur Saputri'
>>> NIM = 'L200180163'
>>> X = '1' + NIM [7:] #Didalam string, digabungkan angka 1 dengan slicing NIM dari karakter ke 7 sampai dengan selesai
>>> print(X) #Menampilkan variabel x
1163
>>> a = int(X) #Konversi string ke integer
>>> print (a) #Menampilkan variabel a
1163
>>> b = len(Nama) #Konversi string dalam variabel Nama ke dalam angka
>>> print (b) #Menampilkan variabel b
18
>>> type (a) #Menampilkan tipe data dari variabel a
<class 'int'>
>>> #python menampilkan type dari variabel a yang merupakan integer
>>> type (b) #Menampilkan type data dari variabel b
<class 'int'>
>>> #python menampilkan type data dari variabel b yang berupa integer
>>> a / b #Operasi pembagian antara variabel a dan variabel b
64.61111111111111
>>> #python menampilkan hasil bagi antara vaariabel a dan variabel b
>>> a // b #Operasi pembagian antara variabel a dan variabel b dengan pembulatan ke bawah
64
>>> #python menampilkan hasil bagi antara varaibel a dan variabel b dengan pembulatan ke bawah
>>> 10 * (a - 999)
1640
>>> #python menampilkan hasil dari operasi diatas
>>> b ** 2 #Operasi b pangkat 2
324
>>> #python menampilkan hasil dari variabel b pangkat 2
>>> a % b #Operasi yang menghasilkan sisa bagi
11
>>> #Python menampilkan hasil sisa variabel a dibagi variabel b
>>> c = 12.5
>>> type (c) #Menampilkan type data dari variabel c
<class 'float'>
>>> #python menampilkan type data dari variabel c yang berupa float
>>> a / c  #Operasi pembagian antara variabel a dan variabel c
93.04
>>> #python menampilkan hasil bagi antara vaariabel a dan variabel c
>>> a // c #Operasi pembagian antara variabel a dan variabel c dengan pembulatan ke bawah
93.0
>>> #python menampilkan hasil bagi antara varaibel a dan variabel c dengan pembulatan ke bawah
>>> a % c #Operasi yang menghasilkan sisa bagi
0.5
>>> #Python menampilkan hasil sisa bagi variabel a dibagi variabel c
>>> c > b #Menyatakan bahwa variabel c lebih besar daripada variabel b
False
>>> #Hasilnya adalah false (salah) karena variabel c lebih kecil daripada variabel b
>>> type (c > b) #menampilkan type data
<class 'bool'>
>>> #tyoe data dari (c > b) adalah bool
>>> a > b and b > c #menyatakan bahwa variabel b lebih besar dari veriabel c dan lebih kecil dari variabel a
True
>>> #hasilnya adalah true (benar)
>>> a > 1100 or b < 10 #menyatakan bahwa variabel a lebih besar dari 1100 atau b lebih kecil dari 10
True
>>> #hasilnya adalah true (benar)
