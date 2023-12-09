# Jawaban soal 2 bagian a

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

# Jawaban soal 2 bagian b
# Nama-nama siswa
siswa = ['Esra', 'Riski', 'Chris', 'Habel', 'Elisabeth']
# Nama siswa yang disorot
siswa_ranking = ['Esra', 'Habel', 'Elisabeth']

i=0
# melakukan loop while
while i < len(siswa):
	if siswa[i] in siswa_ranking:
		print(siswa[i],'adalah juara dikelas.')
	else:
		print (siswa[i], 'tidak mendapat juara.')
	i += 1