kartu_mahasiswa = True
kartu_perpustakaan = False

# LOGIKA
if kartu_mahasiswa or kartu_perpustakaan:
    boleh_masuk = True
else:
    boleh_masuk = False

# OUTPUT
if boleh_masuk:
    print("Boleh masuk perpustakaan")
else:
    print("Tidak boleh masuk perpustakaan")