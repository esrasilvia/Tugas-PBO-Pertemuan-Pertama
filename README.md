#Tugas-PBO-Pertemuan-Pertama

1. (perulangan hingga 100 menggunakan Python)
nama = "Esra Silvia Sihite"

for i in range(1, 101):
    if i % 10 == 0:
        for a in range(3):
            print (nama)
    else:
        print(i)


2. Buatlah program bebas, dengan menerapkan if else pada:
**a. For Loops**
#Jawaban soal 2 bagian a

nama = ('Esra', 'Surya', 'Pujha')
nama_siswa = 'Esra'
ada = False

for n in nama:
	if n == nama_siswa:
		ada = True
		break

if ada:
	print (nama_siswa, 'ada dalam data siswa.\n')
else:
	print (nama_siswa, 'tidak ada dalam data siswa.\n')
**b. While Loops**
  #Jawaban soal 2 bagian b
#Nama-nama siswa
siswa = ['Esra', 'Riski', 'Chris', 'Habel', 'Elisabeth']
#Nama siswa yang disorot
siswa_ranking = ['Esra', 'Habel', 'Elisabeth']

i=0
#melakukan loop while
while i < len(siswa):
	if siswa[i] in siswa_ranking:
		print(siswa[i],'adalah juara dikelas.')
	else:
		print (siswa[i], 'tidak mendapat juara.')
	i += 1

 3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for
#menampilkan nilai pada array menggunakan perulangan for
print ("+"*3, "Menampilkan Nilai Pada ARRAY menggunakan FOR", "+"*3)

#Membuat variabel array
nama=('Esra', 'Budianto', 'Citra')

#Menampilkan semua nilai dalam variabel menggunakan perulangan for
for n in nama:
	print(n)

    
