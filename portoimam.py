
import random

# Sebuah list kata-kata untuk dipilih
KATA = ['python', 'pemrograman', 'komputer', 'ilmu', 'data', 'mesin', 'belajar','kopi','science','pocong','motor','jokowidodo',
        'coklat','agaklaen','tolong','milea','dilan','purwadhika','rumahsakit','stasiun']

# Memilih sebuah kata secara acak dari list
kata_yang_ditebak = random.choice(KATA)

# Membuat list kosong untuk mewakili kata yang ditebak
tebakan_kata = ['_'] * len(kata_yang_ditebak)

# Mengatur jumlah tebakan yang diperbolehkan
jumlah_tebakan = 10

# Menampilkan pesan pengantar
print('Selamat datang di permainan menebak kata!')
print('Anda memiliki', jumlah_tebakan, 'tebakan untuk menebak kata.')
print('Kata tersebut terdiri dari', len(kata_yang_ditebak), 'huruf.')

# Melacak jumlah tebakan yang digunakan
jumlah_tebakan_digunakan = 0

# Perulangan permainan
while '_' in tebakan_kata and jumlah_tebakan_digunakan < jumlah_tebakan:
    # Menampilkan kata yang sudah ditebak
    print('Kata yang sudah ditebak:', ' '.join(tebakan_kata))

    # Mendapatkan tebakan dari pengguna
    tebakan = input('Masukkan tebakan Anda (satu huruf): ').lower()

    # Memeriksa apakah huruf yang ditebak ada dalam kata
    if tebakan in kata_yang_ditebak:
        # Memperbarui kata yang sudah ditebak dengan huruf yang benar
        for i, huruf in enumerate(kata_yang_ditebak):
            if huruf == tebakan:
                tebakan_kata[i] = tebakan
    else:
        # Menambah jumlah tebakan yang digunakan
        jumlah_tebakan_digunakan += 1
        print('Tebakan salah. Anda memiliki', jumlah_tebakan - jumlah_tebakan_digunakan, 'tebakan tersisa.')

# Menampilkan hasil akhir
if '_' not in tebakan_kata:
    print('Selamat! Anda berhasil menebak kata:', kata_yang_ditebak)
else:
    print('Maaf, Anda kehabisan tebakan. Kata yang benar adalah:', kata_yang_ditebak)