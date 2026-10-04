wifi_aktif = True
data_aktif = True

# LOGIKA
if wifi_aktif ^ data_aktif:
    koneksi = True
else:
    koneksi = False

# OUTPUT
if koneksi:
    print("Satu koneksi internet aktif")
else:
    print("Tidak tepat satu koneksi yang aktif")