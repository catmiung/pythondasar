#periksa resiko COVID-19 
#cat@miung.kucing
nama = input('nama: ')
usia = int(input('usia: '))

print('\napakah kamu memiliki tanda dan gejala berikut?')
demam = int(input('demam (0= tidak, 1= ya): '))
batuk = int(input('batuk (0= tidak, 1= ya): '))
sob = int(input('kesulitan bernapas (0= tidak, 1= ya): '))
sore = int(input('tenggorokan sakit atau hidung beringus/ meler (0= tidak, 1= ya): '))
muntah = int(input('ada muntah (0= tidak, 1= ya): '))
sakit = int(input('ada riwayat diabetes, ginjal, atau penyakit jantung (0= tidak, 1= ya): '))
epi = int(input('Apakah kamu sehabis berpergian dari zona epidemik atau kontak dengan seseorang dari zona epidemik atau yang dicurigai COVID-19, dalam 14 hari terakhir (0= tidak, 1= ya): '))

risk = demam*2 + batuk*2 + sob*2 + sore + muntah + sakit

print('\nHallo', nama)
if epi ==0:
    if risk > 4: print("Kamu tidak punya risiko tinggi terhadap COVID-19, tidak perlu panik, mungkin hanya flu biasa,")
    else: print("Tenang, kamu  tidak punya risiko terhadap COVID-19, tetap jaga kesehatan dan kebersihan ya")
if epi ==1:
    if risk > 4: print('Kamu punya risiko tinggi infeksi COVID-19, kamu diwajibkan memakai masker, segeralah ke dokter untuk pemeriksaan lanjut dan isolasi')
    else: print("Kamu tidak memiliki gejala COVID 19, tetapi hati-hati mungkin kamu membawa risiko, karena terpapar wilayah epidemi, ")

if 0<usia<40: rate = "0.2 %"
if 40<usia<50: rate = "0.4 %"
if 50<usia<60: rate = '1.3 %'
if 60<usia<70: rate = "3.6 %"
if 70<usia<80: rate = '8 %'
if 80<usia: rate = '14.8 %'
print('Berdasarkan usiamu, kalau benar kamu terinfeksi, tingkat fatalitasnya sebesar:', rate)
if 0<usia<60: potensi = "Normal"
if 60<usia<70: potensi = "Rata-rata"
if 70<usia: potensi = "Berat"
print('potensi:', potensi)
