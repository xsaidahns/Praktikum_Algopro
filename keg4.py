Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Saidah Nur Saputri'
>>> NIM = 163
>>> Tinggi = 1.60 #dalam satuan meter
>>> Berat = 45 #dalam satuan kilogram
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama) #membuat tuple, yang ditandai dengan adanya data yang berada dalam tanda kurung
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama] #membuat list, yang ditandai dengan adanya data yang berada dalam tanda kurung siku
>>> type (Aku)
<class 'tuple'>
>>> #menampilkan type variabel "Aku" yaitu tuple
>>> Aku [0] #menampilkan data ke 0 dari "Aku"
2000
>>> a = NIM % 4; Aku [a] #menampilkan data ke a, dengan a adalah 3 maka data ke tiga adalah NIM
163
>>> type (Aku[a])
<class 'int'>
>>> #type dari data tersebut adalah integer
>>> Aku [a:4]
(163,)
>>> #menampilkan data ke 3
>>> type Aku [a:4]
SyntaxError: invalid syntax
>>> type (Aku[a:4])
<class 'tuple'>
>>> #type dari data tersebut adalah tuple
>>> Aku [0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Aku [0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #perintah yang diketikkan akan error karena tuplr tidak bisa diubah ubah
>>> type (Data)
<class 'list'>
>>> #menampilkan type dari Data yaitu list
>>> type (Data[4])
<class 'str'>
>>> #menampilkan bahwa tipe data ke empat pada variabel Data adalah string
>>> Data [4] [5]
'h'
>>> #menampilkan karakter ke 5 dari lis ke 4
>>> Data [4] [a:6]
'dah'
>>> #menampilkan karakter ke a sampai dengan ke 5
>>> Data [0] = 'ok' ; Data
['ok', 45, 1.6, 163, 'Saidah Nur Saputri']
>>> #merubah list pada indeks 0 yang diubah menjadi ok
>>> Data [-a]
1.6
>>> #menampilkan data pada angka / huruf sebelum a yang dibaca dari list dari belakang
>>> range (a)
range(0, 3)
>>> #python menampilkan daftar atau koleksi indeks
